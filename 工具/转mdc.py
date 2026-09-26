# -*- coding: utf-8 -*-
"""
A 方案：把 规则包/ 下 103 个 .cursorrules 统一转成 Cursor 现行格式 .mdc。

统一规则：
  * 目标文件名用英文（延续"文件夹中文名 / 文件英文名"约定）；
  * description 用中文（从中文标题改写）；
  * globs 按技术栈推断，写进 frontmatter（决定规则何时生效）；
  * 已有 frontmatter 的 6 个文件：保留其按语义写好的 globs，只补/换中文 description；
  * 正文一字不动。

不转、另行处理的 3 个：
  - Go Temporal 工作流 DSL：正文 0 字符，是索引入口，真正的规则已在同包 5 个 .mdc 里；
  - Solidity+React 区块链应用、Vue 3+Nuxt 3+TypeScript 规范：正文是 AI 的道歉语，内容已损坏。

用法：python 工具/转mdc.py [--apply]
"""
import os, re, io, sys, ast, argparse

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
ROOT = r"D:\Documents\AI技能库"
RULES = os.path.join(ROOT, "03-技术栈参考", "原规则", "规则包")
sys.path.insert(0, os.path.join(ROOT, "工具"))
from 包路径 import REVERSE  # noqa: E402

# ---------------------------------------------------------------- 特殊处理
SKIP_INDEX = {"Go Temporal 工作流 DSL"}          # 空索引，不转
SKIP_CORRUPT = {"Solidity+React 区块链应用", "Vue 3+Nuxt 3+TypeScript 规范"}

# 已有 frontmatter 的包：必须保留其语义化 globs，不能重写
KEEP_GLOBS = {
    "BeeFree SDK 无代码编辑器",
    "C++ 编程指南",
    "Convex 后端规范",
    "Go Temporal 工作流 DSL",
    "Manifest 后端 YAML",
    "Netlify 官方部署规范",
}

# 兜底：从中文标题推断 globs（顺序敏感，先具体后笼统）
GLOB_RULES = [
    (r"Cypress", "**/*.cy.{ts,tsx,js,jsx}"),
    (r"Playwright", "**/*.spec.{ts,tsx,js,jsx}"),
    (r"Jest|Vitest", "**/*.{test,spec}.{ts,tsx,js,jsx}"),
    (r"Flutter|Dart", "**/*.dart"),
    (r"ASP\.NET", "**/*.{cs,csproj,sln}"),
    (r"C\+\+", "**/*.{c,cpp,h,hpp,cc,cxx}"),
    (r"Java\b|Kotlin", "**/*.{java,kt,kts}"),
    (r"Swift", "**/*.swift"),
    (r"R 语言", "**/*.{r,R,Rmd}"),
    (r"Drupal|TYPO3", "**/*.{php,twig,yml,yaml}"),
    (r"Solidity|Xian", "**/*.sol"),
    (r"Gherkin", "**/*.feature"),
    (r"Rell", "**/*.rell"),
    (r"VS Code 扩展", "**/*.ts"),
    (r"UIkit", "**/*.{html,css,js}"),
    (r"Python|Temporal|CUDA", "**/*.py"),
    (r"Go\b", "**/*.go"),
    (r"DRY 与 SOLID", "**/*.{ts,tsx,js,jsx,py}"),
    (r"Git 约定式提交|GitHub|PR 模板|工单|Epic 模板|How-To|文档|结对编程|代码风格一致性|通用编码规范",
     "**/*"),
    (r"Medusa|Convex|BeeFree|Netlify|Chrome|Lambda|Deno", "**/*.{ts,tsx,js,jsx}"),
    (r"TypeScript|TS\+|Next|React|Astro|Angular|Vue|Svelte|Solid|Qwik|HTMX|HTML|Node|NestJS|Remix",
     "**/*.{ts,tsx,js,jsx}"),
]

# 英文目标文件名（用英文名保持"文件夹中文 / 文件英文"约定）
FNAME_OVERRIDE = {
    "github-cursorrules-prompt-file-instructions": "github-rules-instructions",
    "go-temporal-dsl-prompt-file": "go-temporal-dsl",
    "optimize-dry-solid-principles-cursorrules-prompt-f": "optimize-dry-solid-principles",
    "deno-integration-techniques-cursorrules-prompt-fil": "deno-integration-techniques",
    "typescript-code-convention-cursorrules-prompt-file": "typescript-code-convention",
    "typescript-llm-tech-stack-cursorrules-prompt-file": "typescript-llm-tech-stack",
    "kubernetes-mkdocs-documentation-cursorrules-prompt": "kubernetes-mkdocs-documentation",
    "nodejs-mongodb-jwt-express-react-cursorrules-promp": "nodejs-mongodb-jwt-express-react",
    "nextjs-material-ui-tailwind-css-cursorrules-prompt": "nextjs-material-ui-tailwind",
    "cursorrules-cursor-ai-nextjs-14-tailwind-seo-setup": "nextjs-14-tailwind-seo-setup",
    "cursorrules-file-cursor-ai-python-fastapi-api": "python-fastapi-api",
    "cursorrules-cursor-ai-wordpress-draft-macos-prompt": "wordpress-draft-macos",
    "solidity-react-blockchain-apps-cursorrules-prompt-": "solidity-react-blockchain-apps",
    "typescript-nextjs-react-tailwind-supabase-cursorru": "typescript-nextjs-react-tailwind-supabase",
    "javascript-typescript-code-quality-cursorrules-pro": "javascript-typescript-code-quality",
    "python-cursorrules-prompt-file-best-practices": "python-best-practices",
    "r-cursorrules-prompt-file-best-practices": "r-best-practices",
}
_SUFFIXES = ("-cursorrules-prompt-file", "-cursorrules-prompt-", "-cursorrules-promp",
             "-cursorrules-prompt", "-cursorrules-pro", "-cursorrules-p", "-cursorrules-", "-cursorrules")
# 上游有些包名被截断（如 -cursorrules-prompt-fi / -cursorrules-prompt-fil），正则统一收尾
_TRUNC = re.compile(r"-cursorrules(-prompt(-file)?)?(-(prom|promp|prompt-f|prompt-fi|prompt-fil|p|pro))?$")


def target_name(en):
    if en in FNAME_OVERRIDE:
        return FNAME_OVERRIDE[en] + ".mdc"
    stem = en
    for s in _SUFFIXES:
        if stem.endswith(s):
            stem = stem[: -len(s)]
            break
    stem = _TRUNC.sub("", stem)
    stem = stem.rstrip("-")          # 去掉残留的尾横线
    return (stem or en) + ".mdc"


def guess_globs(cn_title):
    for pat, g in GLOB_RULES:
        if re.search(pat, cn_title):
            return g
    return "**/*"


def make_desc(cn_title, globs):
    """description 没有单一出处，改写成明确指向 globs 的中文说明，避免空泛。"""
    if globs == "**/*":
        return f"{cn_title}：适用于项目内所有文件的通用约定。"
    if globs.endswith("*.py"):
        return f"{cn_title}：作用于 Python 源文件（{globs}）。"
    if globs.endswith("*.go"):
        return f"{cn_title}：作用于 Go 源文件（{globs}）。"
    if globs.endswith("*.swift"):
        return f"{cn_title}：作用于 Swift 源文件（{globs}）。"
    if globs.endswith("*.sol"):
        return f"{cn_title}：作用于 Solidity 合约文件（{globs}）。"
    if globs.endswith("*.dart"):
        return f"{cn_title}：作用于 Dart 源文件（{globs}）。"
    if globs.endswith("*.rell"):
        return f"{cn_title}：作用于 Rell 合约文件（{globs}）。"
    if globs.endswith("*.feature"):
        return f"{cn_title}：作用于 Gherkin 特性文件（{globs}）。"
    if globs.endswith("*.cy.{ts,tsx,js,jsx}"):
        return f"{cn_title}：作用于 Cypress 测试文件（{globs}）。"
    if globs.endswith("*.spec.{ts,tsx,js,jsx}"):
        return f"{cn_title}：作用于 Playwright 测试文件（{globs}）。"
    if "{test,spec}" in globs:
        return f"{cn_title}：作用于单元测试文件（{globs}）。"
    if globs.endswith("{c,cpp,h,hpp,cc,cxx}"):
        return f"{cn_title}：作用于 C/C++ 源文件与头文件（{globs}）。"
    if globs.endswith("{java,kt,kts}"):
        return f"{cn_title}：作用于 Java/Kotlin 源文件（{globs}）。"
    if globs.endswith("{cs,csproj,sln}"):
        return f"{cn_title}：作用于 C# 源文件与工程文件（{globs}）。"
    if globs.endswith("{php,twig,yml,yaml}"):
        return f"{cn_title}：作用于 PHP/Twig/配置文件（{globs}）。"
    if globs.endswith("{html,css,js}"):
        return f"{cn_title}：作用于 HTML/CSS/JS（{globs}）。"
    if globs.endswith("{r,R,Rmd}"):
        return f"{cn_title}：作用于 R 源文件与 Rmd（{globs}）。"
    if globs.endswith("{ts,tsx,js,jsx}"):
        return f"{cn_title}：作用于 TypeScript/JavaScript 源文件（{globs}）。"
    return f"{cn_title}：作用于 {globs}。"


ap = argparse.ArgumentParser()
ap.add_argument("--apply", action="store_true")
args = ap.parse_args()

plan, skip = [], []
for cn in sorted(os.listdir(RULES)):
    d = os.path.join(RULES, cn)
    if not os.path.isdir(d):
        continue
    crs = sorted(f for f in os.listdir(d) if f.startswith(".cursorrules"))
    if not crs:
        continue
    if cn in SKIP_INDEX or cn in SKIP_CORRUPT:
        skip.append((cn, crs))
        continue
    en = REVERSE.get(cn, cn)
    tgt = target_name(en)
    existing = sorted(f for f in os.listdir(d) if f.endswith((".mdc", ".mdx")))
    if tgt in existing:
        print(f"[冲突] {cn}: 目标 {tgt} 已存在，跳过")
        continue
    plan.append((cn, crs[0], tgt, guess_globs(cn), cn in KEEP_GLOBS))

print("=" * 104)
print(f"{'包（中文名）':44s} {'原文件':16s} -> {'目标 .mdc':46s} globs")
print("=" * 104)
for cn, cr, tgt, g, keep in plan:
    flag = " [保留原globs]" if keep else ""
    print(f"{cn:44s} {cr:16s} -> {tgt:46s} {g}{flag}")

print()
print(f"将转换 {len(plan)} 个")
print(f"不转换 {len(skip)} 个：")
for cn, crs in skip:
    why = "空索引（规则已在同包 .mdc）" if cn in SKIP_INDEX else "正文已损坏（AI 道歉语）"
    print(f"   {cn}  —  {why}")

if not args.apply:
    print("\n模式：预演（加 --apply 才执行）")
    sys.exit(0)

FIELD = re.compile(r"^\s*---\s*\n(.*?)\n---\s*\n?", re.S)
done = 0
for cn, cr, tgt, g, keep in plan:
    d = os.path.join(RULES, cn)
    raw = open(os.path.join(d, cr), encoding="utf-8", errors="replace").read()
    m = FIELD.match(raw)
    if m:
        fm, body = m.group(1), raw[m.end():]
        gm = re.search(r"^globs:\s*(.*)$", fm, re.M)
        if keep and gm and gm.group(1).strip():
            globs = gm.group(1).strip()
        else:
            globs = g
        # 清掉原有的（可能是空白的）description/globs 行，再统一重建
        fm_lines = [ln for ln in fm.split("\n")
                    if not re.match(r"^(description|globs)\s*:", ln)]
        rest = "\n".join(fm_lines).strip()
    else:
        body, globs, rest = raw, g, ""
    head = f"---\ndescription: {make_desc(cn, globs)}\nglobs: {globs}\n"
    if rest:
        head += rest + "\n"
    head += "---\n"
    out = head + body.lstrip("\n")
    open(os.path.join(d, tgt), "w", encoding="utf-8").write(out)
    os.remove(os.path.join(d, cr))
    done += 1

print(f"\n完成：转换 {done} 个，删除对应 .cursorrules {done} 个")
