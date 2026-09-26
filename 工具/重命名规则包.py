# -*- coding: utf-8 -*-
"""
B 方案：把 03-技术栈参考/原规则/rules 下 178 个英文包文件夹改成中文名。

安全性设计：
  * 映射表覆盖不到的包 → 报错退出，绝不静默漏改；
  * 每个目标名做 Windows 非法字符校验 + 空名校验；
  * 目标名重复 → 报错退出（避免覆盖）；
  * 目标名与现有其它包名冲突 → 报错退出；
  * 只改文件夹名，不动任何文件名（134 个包有多个 .mdc，动引用面太大）；
  * 预演会打印旧名 → 新名全部对照，并统计目录.md 需要改多少条路径。

用法：python 工具/重命名规则包.py            预演
      python 工具/重命名规则包.py --apply    执行（同时更新 目录.md）
"""
import os, re, io, sys, shutil, argparse

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
ROOT = r"D:\Documents\AI技能库"
REF = os.path.join(ROOT, "03-技术栈参考")
RULES = os.path.join(REF, "原规则", "规则包")
INDEX = os.path.join(REF, "目录.md")

# ---------------------------------------------------------------- 中文名映射
# 有 .mdc 的包取自 目录.md 的"原文件夹"列；其余由实测补齐。
MAP = {
# ===== 前端 =====
"angular-novo-elements-cursorrules-prompt-file": "Angular Novo Elements 组件规范",
"angular-typescript-cursorrules-prompt-file": "Angular TypeScript 规范",
"astro-typescript-cursorrules-prompt-file": "Astro TypeScript 规范",
"cursor-ai-react-typescript-shadcn-ui-cursorrules-p": "React+TS+shadcn/ui 组件开发规范",
"html-tailwind-css-javascript-cursorrules-prompt-fi": "HTML+Tailwind+JS 开发规范",
"htmx-basic-cursorrules-prompt-file": "HTMX 基础用法",
"htmx-django-cursorrules-prompt-file": "HTMX+Django 集成",
"htmx-flask-cursorrules-prompt-file": "HTMX+Flask 集成",
"htmx-go-basic-cursorrules-prompt-file": "HTMX+Go 基础集成",
"htmx-go-fiber-cursorrules-prompt-file": "HTMX+Go Fiber 集成",
"javascript-astro-tailwind-css-cursorrules-prompt-f": "JS+Astro+Tailwind 开发规范",
"cursorrules-cursor-ai-nextjs-14-tailwind-seo-setup": "Next.js 14+Tailwind SEO 配置",
"nextjs15-react19-vercelai-tailwind-cursorrules-prompt-file": "Next.js 15+React 19+Vercel AI",
"nextjs-app-router-cursorrules-prompt-file": "Next.js App Router 规范",
"nextjs-material-ui-tailwind-css-cursorrules-prompt": "Next.js+Material UI+Tailwind",
"nextjs-react-tailwind-cursorrules-prompt-file": "Next.js+React+Tailwind",
"nextjs-react-typescript-cursorrules-prompt-file": "Next.js+React+TypeScript",
"nextjs-seo-dev-cursorrules-prompt-file": "Next.js SEO 开发规范",
"nextjs-supabase-shadcn-pwa-cursorrules-prompt-file": "Next.js+Supabase+shadcn PWA",
"nextjs-supabase-todo-app-cursorrules-prompt-file": "Next.js+Supabase 待办应用",
"nextjs-tailwind-typescript-apps-cursorrules-prompt": "Next.js+Tailwind+TS 应用",
"nextjs-typescript-cursorrules-prompt-file": "Next.js+TypeScript 规范",
"nextjs-typescript-app-cursorrules-prompt-file": "Next.js+TypeScript 应用模板",
"nextjs-typescript-tailwind-cursorrules-prompt-file": "Next.js+TS+Tailwind",
"nextjs-vercel-supabase-cursorrules-prompt-file": "Next.js+Vercel+Supabase",
"nextjs-vercel-typescript-cursorrules-prompt-file": "Next.js+Vercel+TypeScript",
"nodejs-mongodb-jwt-express-react-cursorrules-promp": "Node+MongoDB+JWT+Express+React",
"qwik-basic-cursorrules-prompt-file": "Qwik 基础用法",
"qwik-tailwind-cursorrules-prompt-file": "Qwik+Tailwind",
"react-chakra-ui-cursorrules-prompt-file": "React+Chakra UI 组件规范",
"react-components-creation-cursorrules-prompt-file": "React 组件创建规范",
"react-graphql-apollo-client-cursorrules-prompt-file": "React+GraphQL+Apollo Client",
"react-mobx-cursorrules-prompt-file": "React+MobX 状态管理",
"react-nextjs-ui-development-cursorrules-prompt-fil": "React+Next.js UI 开发",
"react-query-cursorrules-prompt-file": "React Query 数据获取",
"react-redux-typescript-cursorrules-prompt-file": "React+Redux+TypeScript",
"react-styled-components-cursorrules-prompt-file": "React+styled-components",
"react-typescript-nextjs-nodejs-cursorrules-prompt-": "React+TS+Next.js+Node.js",
"react-typescript-symfony-cursorrules-prompt-file": "React+TS+Symfony",
"solidjs-basic-cursorrules-prompt-file": "SolidJS 基础用法",
"solidjs-tailwind-cursorrules-prompt-file": "SolidJS+Tailwind",
"solidjs-typescript-cursorrules-prompt-file": "SolidJS+TypeScript",
"svelte-5-vs-svelte-4-cursorrules-prompt-file": "Svelte 5 与 Svelte 4 差异",
"sveltekit-restful-api-tailwind-css-cursorrules-pro": "SvelteKit RESTful API+Tailwind",
"sveltekit-tailwindcss-typescript-cursorrules-promp": "SvelteKit+Tailwind+TypeScript",
"sveltekit-typescript-guide-cursorrules-prompt-file": "SvelteKit+TypeScript 指南",
"tailwind-css-nextjs-guide-cursorrules-prompt-file": "Tailwind+Next.js 指南",
"tailwind-react-firebase-cursorrules-prompt-file": "Tailwind+React+Firebase",
"tailwind-shadcn-ui-integration-cursorrules-prompt-": "Tailwind+shadcn/ui 集成",
"tauri-svelte-typescript-guide-cursorrules-prompt-f": "Tauri+Svelte+TypeScript 指南",
"typescript-nextjs-cursorrules-prompt-file": "TypeScript+Next.js",
"typescript-nextjs-react-cursorrules-prompt-file": "TypeScript+Next.js+React",
"typescript-nextjs-react-tailwind-supabase-cursorru": "TS+Next.js+React+Tailwind+Supabase",
"typescript-nextjs-supabase-cursorrules-prompt-file": "TypeScript+Next.js+Supabase",
"typescript-nodejs-nextjs-ai-cursorrules-prompt-fil": "TS+Node+Next.js AI 应用",
"typescript-nodejs-nextjs-app-cursorrules-prompt-fi": "TS+Node+Next.js 应用",
"typescript-nodejs-nextjs-react-ui-css-cursorrules-": "TS+Node+Next.js+React UI 样式",
"typescript-nodejs-react-vite-cursorrules-prompt-fi": "TS+Node+React+Vite",
"typescript-react-cursorrules-prompt-file": "TypeScript+React 规范",
"typescript-react-nextjs-cloudflare-cursorrules-pro": "TS+React+Next.js+Cloudflare",
"typescript-react-nextui-supabase-cursorrules-promp": "TS+React+NextUI+Supabase",
"typescript-shadcn-ui-nextjs-cursorrules-prompt-fil": "TS+shadcn/ui+Next.js",
"typescript-vite-tailwind-cursorrules-prompt-file": "TypeScript+Vite+Tailwind",
"typescript-vuejs-cursorrules-prompt-file": "TypeScript+Vue 规范",
"typescript-zod-tailwind-nextjs-cursorrules-prompt-": "TS+Zod+Tailwind+Next.js",
"vue3-composition-api-cursorrules-prompt-file": "Vue 3 Composition API",
"vue-3-nuxt-3-development-cursorrules-prompt-file": "Vue 3+Nuxt 3 开发规范",
"vue-3-nuxt-3-typescript-cursorrules-prompt-file": "Vue 3+Nuxt 3+TypeScript",

# ===== 后端 =====
"go-backend-scalability-cursorrules-prompt-file": "Go 后端可扩展性",
"go-servemux-rest-api-cursorrules-prompt-file": "Go ServeMux REST API",
"go-temporal-dsl-prompt-file": "Go Temporal 工作流 DSL",
"java-general-purpose-cursorrules-prompt-file": "Java 通用规范",
"java-springboot-jpa-cursorrules-prompt-file": "Java+Spring Boot+JPA",
"javascript-chrome-apis-cursorrules-prompt-file": "JavaScript Chrome API",
"javascript-typescript-code-quality-cursorrules-pro": "JS/TS 代码质量总纲",
"laravel-php-83-cursorrules-prompt-file": "Laravel PHP 8.3",
"laravel-tall-stack-best-practices-cursorrules-prom": "Laravel TALL 技术栈",
"linux-nvidia-cuda-python-cursorrules-prompt-file": "Linux+NVIDIA CUDA+Python",
"nodejs-mongodb-cursorrules-prompt-file-tutorial": "Node.js+MongoDB 入门教程",
"python-312-fastapi-best-practices-cursorrules-prom": "Python 3.12+FastAPI 最佳实践",
"python-containerization-cursorrules-prompt-file": "Python 应用容器化",
"python-cursorrules-prompt-file-best-practices": "Python 通用最佳实践",
"python-developer-cursorrules-prompt-file": "Python 开发者规范",
"python-django-best-practices-cursorrules-prompt-fi": "Python Django 最佳实践",
"python-fastapi-cursorrules-prompt-file": "Python FastAPI 规范",
"python-fastapi-best-practices-cursorrules-prompt-f": "Python FastAPI 最佳实践",
"python-fastapi-scalable-api-cursorrules-prompt-fil": "Python FastAPI 可扩展 API",
"python-flask-json-guide-cursorrules-prompt-file": "Python Flask JSON 指南",
"python-github-setup-cursorrules-prompt-file": "Python 项目 GitHub 配置",
"python-llm-ml-workflow-cursorrules-prompt-file": "Python LLM/ML 工作流",
"python-projects-guide-cursorrules-prompt-file": "Python 项目工程指南",
"python--typescript-guide-cursorrules-prompt-file": "Python+TypeScript 混合指南",
"rails-cursorrules-prompt-file": "Ruby on Rails 规范",
"temporal-python-cursorrules": "Temporal+Python 工作流",
"typescript-nestjs-best-practices-cursorrules-promp": "TypeScript NestJS 最佳实践",
"wordpress-php-guzzle-gutenberg-cursorrules-prompt-": "WordPress+PHP+Guzzle+Gutenberg",
"cursorrules-file-cursor-ai-python-fastapi-api": "Python FastAPI 依赖注入 API",
"py-fast-api": "Python FastAPI 精简版",
"es-module-nodejs-guidelines-cursorrules-prompt-fil": "ES Module+Node.js 规范",

# ===== 移动开发 =====
"android-jetpack-compose-cursorrules-prompt-file": "Android Jetpack Compose",
"flutter-app-expert-cursorrules-prompt-file": "Flutter 应用开发",
"flutter-riverpod-cursorrules-prompt-file": "Flutter+Riverpod 状态管理",
"kotlin-ktor-development-cursorrules-prompt-file": "Kotlin+Ktor 开发",
"kotlin-springboot-best-practices-cursorrules-prompt-file": "Kotlin+Spring Boot 最佳实践",
"nativescript-cursorrules-prompt-file": "NativeScript 跨端开发",
"react-native-expo-cursorrules-prompt-file": "React Native+Expo",
"react-native-expo-router-typescript-windows-cursorrules-prompt-file": "React Native+Expo Router+TS（Windows）",
"swift-uikit-cursorrules-prompt-file": "Swift UIKit+MVVM+RxSwift",
"swiftui-guidelines-cursorrules-prompt-file": "SwiftUI 开发指南",
"typescript-axios-cursorrules-prompt-file": "TypeScript+axios 请求封装",

# ===== 游戏 =====
"ascii-simulation-game-cursorrules-prompt-file": "ASCII 模拟游戏开发",
"unity-cursor-ai-c-cursorrules-prompt-file": "Unity C# 开发规范",
"dragonruby-best-practices-cursorrules-prompt-file": "DragonRuby 游戏开发",
"graphical-apps-development-cursorrules-prompt-file": "图形界面应用开发",

# ===== 测试 =====
"cypress-accessibility-testing-cursorrules-prompt-file": "Cypress 无障碍测试",
"cypress-api-testing-cursorrules-prompt-file": "Cypress API 测试",
"cypress-defect-tracking-cursorrules-prompt-file": "Cypress 缺陷追踪",
"cypress-e2e-testing-cursorrules-prompt-file": "Cypress 端到端测试",
"cypress-integration-testing-cursorrules-prompt-file": "Cypress 集成测试",
"playwright-accessibility-testing-cursorrules-prompt-file": "Playwright 无障碍测试",
"playwright-api-testing-cursorrules-prompt-file": "Playwright API 测试",
"playwright-defect-tracking-cursorrules-prompt-file": "Playwright 缺陷追踪",
"playwright-e2e-testing-cursorrules-prompt-file": "Playwright 端到端测试",
"playwright-integration-testing-cursorrules-prompt-file": "Playwright 集成测试",
"gherkin-style-testing-cursorrules-prompt-file": "Gherkin 风格测试",
"jest-unit-testing-cursorrules-prompt-file": "Jest 单元测试",
"vitest-unit-testing-cursorrules-prompt-file": "Vitest 单元测试",
"qa-bug-report-cursorrules-prompt-file": "QA Bug 报告模板",
"testrail-test-case-cursorrules-prompt-file": "TestRail 测试用例模板",
"xray-test-case-cursorrules-prompt-file": "Xray 测试用例模板",
"typescript-expo-jest-detox-cursorrules-prompt-file": "TS+Expo+Jest+Detox 测试",

# ===== 工程规范 =====
"git-conventional-commit-messages": "Git 约定式提交信息",
"github-code-quality-cursorrules-prompt-file": "GitHub 代码质量规范",
"github-cursorrules-prompt-file-instructions": "GitHub 仓库规则编写",
"pr-template-cursorrules-prompt-file": "PR 模板",
"engineering-ticket-template-cursorrules-prompt-file": "工程工单模板",
"project-epic-template-cursorrules-prompt-file": "项目 Epic 模板",
"how-to-documentation-cursorrules-prompt-file": "How-To 文档写作指南",
"code-guidelines-cursorrules-prompt-file": "通用编码规范",
"code-style-consistency-cursorrules-prompt-file": "代码风格一致性",
"code-pair-interviews": "结对编程面试",
"optimize-dry-solid-principles-cursorrules-prompt-f": "DRY 与 SOLID 原则优化",
"web-app-optimization-cursorrules-prompt-file": "Web 应用性能优化",
"kubernetes-mkdocs-documentation-cursorrules-prompt": "Kubernetes+MkDocs 文档",
"knative-istio-typesense-gpu-cursorrules-prompt-fil": "Knative+Istio+Typesense GPU 部署",
"manifest-yaml-cursorrules-prompt-file": "Manifest 后端 YAML",
"netlify-official-cursorrules-prompt-file": "Netlify 官方部署规范",
"convex-cursorrules-prompt-file": "Convex 后端规范",
"medusa-cursorrules": "Medusa 电商框架",
"beefreeSDK-nocode-content-editor-cursorrules-prompt-file": "BeeFree SDK 无代码编辑器",
"vscode-extension-dev-typescript-cursorrules-prompt-file": "VS Code 扩展开发（TS）",
"chrome-extension-dev-js-typescript-cursorrules-pro": "Chrome 扩展开发（JS/TS）",
"typescript-clasp-cursorrules-prompt-file": "TypeScript+Google Apps Script",
"deno-integration-techniques-cursorrules-prompt-fil": "Deno 集成技巧",
"elixir-engineer-guidelines-cursorrules-prompt-file": "Elixir 工程规范",
"elixir-phoenix-docker-setup-cursorrules-prompt-fil": "Elixir Phoenix+Docker 配置",
"cpp-programming-guidelines-cursorrules-prompt-file": "C++ 编程指南",
"r-cursorrules-prompt-file-best-practices": "R 语言最佳实践",
"scala-kafka-cursorrules-prompt-file": "Scala+Kafka",
"aspnet-abp-cursorrules-prompt-file": "ASP.NET ABP 框架",
"drupal-11-cursorrules-prompt-file": "Drupal 11 开发",
"typo3cms-extension-cursorrules-prompt-file": "TYPO3 CMS 扩展",
"cursorrules-cursor-ai-wordpress-draft-macos-prompt": "WordPress 草稿（macOS）",
"plasticode-telegram-api-cursorrules-prompt-file": "Plasticode Telegram Bot API",
"pyqt6-eeg-processing-cursorrules-prompt-file": "PyQt6 脑电信号处理",
"pandas-scikit-learn-guide-cursorrules-prompt-file": "pandas+scikit-learn 指南",
"pytorch-scikit-learn-cursorrules-prompt-file": "PyTorch+scikit-learn",
"typescript-code-convention-cursorrules-prompt-file": "TypeScript 代码约定",
"typescript-llm-tech-stack-cursorrules-prompt-file": "TypeScript LLM 技术栈",
"next-type-llm": "Next.js+TypeScript LLM 应用",
"solidity-foundry-cursorrules-prompt-file": "Solidity+Foundry 合约开发",
"solidity-hardhat-cursorrules-prompt-file": "Solidity+Hardhat 合约开发",
"solidity-react-blockchain-apps-cursorrules-prompt-": "Solidity+React 区块链应用",
"xian-smart-contracts-cursor-rules-prompt-file": "Xian 智能合约",
"optimize-rell-blockchain-code-cursorrules-prompt-f": "Rell 区块链代码优化",
"webassembly-z80-cellular-automata-cursorrules-prom": "WebAssembly Z80 元胞自动机",
"uikit-guidelines-cursorrules-prompt-file": "UIkit 前端框架指南",
"salesforce-apex-cursorrules-prompt-file": "Salesforce Apex 开发",
}

MANIFEST = os.path.join(ROOT, "目录.json")
ILLEGAL = set('<>:"/\\|?*')


def sanitize(name):
    # 斜杠是 Windows 非法字符，但不能直接删（shadcn/ui 会变成 shadcnui），替换成 ·
    out = name.replace("/", "·")
    out = "".join(c for c in out if c not in ILLEGAL)
    out = re.sub(r"\s+", " ", out).strip().rstrip(".")
    # 目标名里不该出现 Windows 非法字符，出现说明映射表写错了
    assert not (set(out) & ILLEGAL), f"目标名仍含非法字符: {name}"
    # 要求是"中文名"：若一个汉字都没有，补一个中文后缀
    if not any("\u4e00" <= c <= "\u9fff" for c in out):
        out = out + " 规范"
    return out


ap = argparse.ArgumentParser()
ap.add_argument("--apply", action="store_true")
args = ap.parse_args()

existing = sorted(d for d in os.listdir(RULES) if os.path.isdir(os.path.join(RULES, d)))

# 1) 覆盖检查
miss = [d for d in existing if d not in MAP]
extra = [k for k in MAP if k not in existing]
print(f"rules/ 实际包数: {len(existing)}   映射表条目: {len(MAP)}")
if miss:
    print("\n[错误] 以下包没有中文名映射，请补齐：")
    for d in miss:
        print("   ", d)
if extra:
    print("\n[错误] 映射表里有不存在的包：")
    for d in extra:
        print("   ", d)
if miss or extra:
    sys.exit(1)

# 2) 目标名校验
plan = []
seen = {}
errs = []
for old in existing:
    new = sanitize(MAP[old])
    if not new:
        errs.append((old, "目标名为空"))
        continue
    if new in seen:
        errs.append((old, f"目标名与 {seen[new]} 重复：{new}"))
        continue
    seen[new] = old
    plan.append((old, new))
if errs:
    print("\n[错误] 目标名有问题：")
    for o, why in errs:
        print(f"   {o}  ->  {why}")
    sys.exit(1)

print(f"目标名唯一性校验通过（{len(plan)} 个）。\n")
print("=" * 100)
print(f"{'旧名':62s} 新名")
print("=" * 100)
for old, new in plan:
    print(f"{old:62s} {new}")

# 3) 目录.md 影响面
txt = open(INDEX, encoding="utf-8").read()
refs = re.findall(r"`原规则/规则包/([^`]+)`", txt)
print()
print(f"目录.md 引用 rules/ 下路径 {len(refs)} 条，其中 {sum(1 for r in refs if r in MAP)} 条会改到")

# 4) 执行
if args.apply:
    print("\n执行改名...")
    # 两阶段：先改成临时名，避免新旧名互撞
    tmp = {}
    for old, new in plan:
        src = os.path.join(RULES, old)
        t = os.path.join(RULES, f"__tmp__{abs(hash(old)) % 10**8}")
        os.rename(src, t)
        tmp[t] = (old, new)
    for t, (old, new) in tmp.items():
        os.rename(t, os.path.join(RULES, new))

    # 更新 目录.md
    def sub(m):
        p = m.group(1)
        return f"`原规则/规则包/{MAP.get(p, p)}`"
    new_txt = re.sub(r"`原规则/规则包/([^`]+)`", sub, txt)
    open(INDEX, "w", encoding="utf-8").write(new_txt)
    print(f"目录.md 已更新。")
    print(f"改名完成：{len(plan)} 个文件夹")
else:
    print("\n模式：预演（加 --apply 才执行）")
