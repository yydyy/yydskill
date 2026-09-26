@echo off
if /i "%~1"=="__cp936__" goto :main
chcp 936 >nul
cmd /c "%~f0" __cp936__ %*
exit /b
:main
shift
cd /d "%~dp0"
pwsh -NoLogo -NoProfile -File "%~dp0同步到项目.ps1" %*
if errorlevel 1 pause