# UTF-8. Deploy skills from AI技能库 into Cursor user skills and target projects.
[CmdletBinding()]
param(
    [switch]$Force
)

$ErrorActionPreference = 'Stop'
$utf8 = New-Object System.Text.UTF8Encoding $false
$toolDir = $PSScriptRoot
$hub = Split-Path -Parent $toolDir
$configPath = Join-Path $toolDir '配置.json'
$catalogPath = Join-Path $hub '目录.json'

if (-not (Test-Path $configPath)) { throw "找不到配置: $configPath" }
if (-not (Test-Path $catalogPath)) { throw "找不到目录: $catalogPath" }

$config = Get-Content -Raw $configPath -Encoding UTF8 | ConvertFrom-Json
$catalog = Get-Content -Raw $catalogPath -Encoding UTF8 | ConvertFrom-Json

function Write-Utf8([string]$Path, [string]$Text) {
    $dir = Split-Path -Parent $Path
    if (-not (Test-Path $dir)) {
        New-Item -ItemType Directory -Path $dir -Force | Out-Null
    }
    [System.IO.File]::WriteAllText($Path, $Text, $utf8)
}

function Get-ManagedSkills([string[]]$Groups) {
    $catalog.skills | Where-Object { $Groups -contains $_.group }
}

function Publish-SkillFolder {
    param(
        [object]$Skill,
        [string]$TargetRoot
    )
    $src = Join-Path $hub ($Skill.folder -replace '/', '\')
    $skillFile = Join-Path $src 'SKILL.md'
    if (-not (Test-Path $skillFile)) { throw "缺少 $skillFile" }
    $destDir = Join-Path $TargetRoot $Skill.title
    New-Item -ItemType Directory -Path $destDir -Force | Out-Null
    Copy-Item $skillFile (Join-Path $destDir 'SKILL.md') -Force
    $full = Join-Path $src '完整版.md'
    if (Test-Path $full) {
        Copy-Item $full (Join-Path $destDir '完整版.md') -Force
    }
}

function Publish-ClineRule {
    param(
        [object]$Skill,
        [string]$TargetRoot
    )
    $src = Join-Path $hub (($Skill.folder -replace '/', '\') + '\SKILL.md')
    $body = [System.IO.File]::ReadAllText($src)
    Write-Utf8 (Join-Path $TargetRoot ($Skill.title + '.md')) $body
}

function Publish-CursorRule {
    param(
        [object]$Skill,
        [string]$TargetRoot
    )
    if ($Skill.kind -ne 'rule') { return }
    $src = Join-Path $hub (($Skill.folder -replace '/', '\') + '\SKILL.md')
    $body = [System.IO.File]::ReadAllText($src)
    if ($body -notmatch '^---') {
        $body = @"
---
description: $($Skill.description)
globs: "*"
alwaysApply: true
---

$body
"@
    }
    Write-Utf8 (Join-Path $TargetRoot ($Skill.id + '.mdc')) $body
}

Write-Host '========== AI技能库 同步 =========='
Write-Host "源目录: $hub"

$cursorUser = $config.cursorUserSkills
if ($cursorUser -and $cursorUser.enabled) {
    $dest = Join-Path $env:USERPROFILE '.cursor\skills'
    $skills = @(Get-ManagedSkills $cursorUser.groups)
    Write-Host ""
    Write-Host "[Cursor 用户技能] $dest"
    New-Item -ItemType Directory -Path $dest -Force | Out-Null
    foreach ($skill in $skills) {
        Publish-SkillFolder -Skill $skill -TargetRoot $dest
        Write-Host ("  " + $skill.title)
    }
}

foreach ($project in @($config.projects)) {
    if (-not $project.enabled) { continue }
    $projectPath = [string]$project.path
    if (-not (Test-Path $projectPath)) {
        Write-Host ""
        Write-Host "[跳过] 项目不存在: $projectPath"
        continue
    }
    $skills = @(Get-ManagedSkills $project.groups)
    $tools = @($project.tools)
    Write-Host ""
    Write-Host "[项目] $projectPath"
    Write-Host ("  工具: " + ($tools -join ', '))

    if ($tools -contains 'agents' -or $tools -contains 'kimi') {
        $root = Join-Path $projectPath '.agents\skills'
        New-Item -ItemType Directory -Path $root -Force | Out-Null
        foreach ($skill in $skills) {
            Publish-SkillFolder -Skill $skill -TargetRoot $root
            Write-Host ("  [agents] " + $skill.title)
        }
    }

    if ($tools -contains 'kimi') {
        $root = Join-Path $projectPath '.kimi\skills'
        New-Item -ItemType Directory -Path $root -Force | Out-Null
        foreach ($skill in $skills) {
            Publish-SkillFolder -Skill $skill -TargetRoot $root
            Write-Host ("  [kimi] " + $skill.title)
        }
    }

    if ($tools -contains 'claude') {
        $root = Join-Path $projectPath '.claude\skills'
        New-Item -ItemType Directory -Path $root -Force | Out-Null
        foreach ($skill in $skills) {
            Publish-SkillFolder -Skill $skill -TargetRoot $root
            Write-Host ("  [claude] " + $skill.title)
        }
    }

    if ($tools -contains 'cursor') {
        $skillRoot = Join-Path $projectPath '.cursor\skills'
        $ruleRoot = Join-Path $projectPath '.cursor\rules'
        New-Item -ItemType Directory -Path $skillRoot -Force | Out-Null
        New-Item -ItemType Directory -Path $ruleRoot -Force | Out-Null
        foreach ($skill in $skills) {
            Publish-SkillFolder -Skill $skill -TargetRoot $skillRoot
            Publish-CursorRule -Skill $skill -TargetRoot $ruleRoot
            Write-Host ("  [cursor] " + $skill.title)
        }
    }

    if ($tools -contains 'cline') {
        $root = Join-Path $projectPath '.clinerules'
        New-Item -ItemType Directory -Path $root -Force | Out-Null
        foreach ($skill in $skills) {
            Publish-ClineRule -Skill $skill -TargetRoot $root
            Write-Host ("  [cline] " + $skill.title)
        }
    }
}

Write-Host ""
Write-Host '========== 同步完成 =========='
