# -*- coding: utf-8 -*-
"""
第三批：把"正文只在 .cursorrules 里"的 A 类包中、与常见工程实践相关且量小的先译掉。

覆盖：Conventional Commits 规范、Manifest 后端 YAML、Next.js+Supabase Todo、
      Medusa 框架约定。

`.cursorrules` 前带 YAML frontmatter 的（manifest）保留其 frontmatter 结构，
只翻其中的 prose。

用法：python 工具/翻译规则3.py [--apply]
"""
import os, re, io, sys, argparse

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
ROOT = r"D:\Documents\AI技能库"
RULES = os.path.join(ROOT, "03-技术栈参考", "原规则", "rules")
sys.path.insert(0, os.path.join(ROOT, "工具"))
from 包路径 import MAP as _PKGMAP, pkg_dir as _pkg_dir


def P(pkg):
    """英文包名 -> 改名后的绝对路径"""
    return _pkg_dir(pkg)

MDC = {
"nextjs-supabase-todo-app-cursorrules-prompt-file": {
 "todo-app-general-rules.mdc": (
  "整个 Todo Web 应用项目的通用规则，涵盖适用于所有文件的规格与约定。",
  """- 按项目规格与约定构建 Todo 应用。
- Todo 是一个用来管理待办事项的 Web 应用。"""),
},
}

CR = {}

CR["git-conventional-commit-messages/.cursorrules"] = """使用 Conventional Commits 规范生成提交信息。

提交信息的结构如下：

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```
--------------------------------

提交信息包含以下结构元素，用于向库的使用者传达意图：

  - fix：类型为 fix 的提交修复代码库中的 bug（对应语义化版本中的 PATCH）。
  - feat：类型为 feat 的提交为代码库引入新功能（对应语义化版本中的 MINOR）。
  - BREAKING CHANGE：带 BREAKING CHANGE: 页脚，或在类型/范围后加 ! 的提交，引入破坏性 API 变更（对应语义化版本中的 MAJOR）。BREAKING CHANGE 可以出现在任何类型的提交中。
  - 除 fix: 与 feat: 外还允许其它类型，例如 @commitlint/config-conventional（基于 Angular 约定）推荐 build:、chore:、ci:、docs:、style:、refactor:、perf:、test: 等。
  - 除 BREAKING CHANGE: <description> 外，也可以提供其它页脚，遵循类似 git trailer 格式的约定。
  - Conventional Commits 规范并未强制要求额外类型，它们在语义化版本中也没有隐含效果（除非包含 BREAKING CHANGE）。范围可以加在提交类型后，用于提供额外上下文，写在圆括号内，例如 feat(parser): add ability to parse arrays。



### 规范细节

本文档中的关键词 "MUST"、"MUST NOT"、"REQUIRED"、"SHALL"、"SHALL NOT"、"SHOULD"、"SHOULD NOT"、"RECOMMENDED"、"MAY" 与 "OPTIONAL" 按 RFC 2119 的定义解释。

提交必须以类型开头。类型是一个名词，如 feat、fix 等，后面跟可选的 范围、可选的 !，以及必需的结尾冒号和空格。
当提交为应用或库新增功能时，必须使用 feat 类型。
当提交表示对应用的 bug 修复时，必须使用 fix 类型。
类型后可以提供范围。范围必须是一个描述代码库某部分的名词，写在圆括号内，例如 fix(parser):
描述必须紧跟在类型/范围前缀后的冒号和空格之后。描述是代码改动的简短摘要，例如 fix: array parsing issue when multiple spaces were contained in string。
在简短描述之后可以提供更长的提交正文，补充代码改动的上下文信息。正文必须与描述之间空一行开始。
提交正文是自由格式的，可以包含任意数量的、以换行分隔的段落。
在正文之后空一行，可以提供一个或多个页脚。每个页脚必须由一个词元（token），加上 :<space> 或 <space># 分隔符，再加上一个字符串值组成（受 git trailer 约定启发）。
页脚的词元必须用 - 代替空白字符，例如 Acked-by（这有助于把页脚区与多段正文区分开）。BREAKING CHANGE 是例外，它也可以用作词元。
页脚的值可以包含空格和换行，解析必须在下一次遇到合法的页脚词元/分隔符对时结束。
破坏性变更必须标在提交的类型/范围前缀中，或写成页脚中的一条。
如果写成页脚，破坏性变更必须由大写文本 BREAKING CHANGE，加上冒号、空格和描述组成，例如 BREAKING CHANGE: environment variables now take precedence over config files。
如果标在类型/范围前缀中，破坏性变更必须用紧跟在 : 之前的 ! 表示。若使用了 !，页脚中可以省略 BREAKING CHANGE:，此时用提交描述来说明该破坏性变更。
除 feat 与 fix 外，提交信息中可以使用其它类型，例如 docs: update ref docs。
除 BREAKING CHANGE 必须大写外，实现者不得把构成 Conventional Commits 的信息单元当作大小写敏感。
作为页脚词元使用时，BREAKING-CHANGE 必须与 BREAKING CHANGE 同义。"""

CR["manifest-yaml-cursorrules-prompt-file/.cursorrules"] = """---
description: 
globs: 
alwaysApply: true
---
**面向 Manifest 专家开发者的提示词**

**你是一个应用创建助手，将要使用后端 Manifest。你生成的应用是轻量的、用于演示的：目标不是提供完整的数据结构，而是展示多种属性类型。**

**代码结构**
被要求创建后端时，执行以下操作：

1. 安装 `manifest` npm 包
2. 在 `pacakge.json` 中加入以下脚本："manifest": "node node_modules/manifest/scripts/watch/watch.js" 与 "manifest:seed": "node node_modules/manifest/dist/manifest/src/seed/scripts/seed.js"
3. 创建 `manifest/backend.yml` 文件并把 manifest 代码写进去。
4. 在 `.vscode/extensions.json` 中加入 `redhat.vscode-yaml` 作为推荐扩展
5. 在 `.vscode/settings.json` 中加入以下 `yaml.schemas`：`"https://schema.manifest.build/schema.json": "**/manifest/**.yml"`

**后端文件**
在 `manifest/backend.yml` 上遵循以下规则：
- 严格遵循 Manifest JSON Schema：https://schema.manifest.build/schema.json
- 先给应用起一个简短的名字
- 最多 2 到 3 个实体
- 每个实体最多 4 个属性
- 尽量展示不同的属性类型
- 校验类属性只用一两次
- 不要有实体叫 admin
- 不要使用可认证实体
- 每个实体名后加一个 emoji，但关系引用里不要用这个 emoji
- 每个实体对象前加一个换行
- 每个实体只出现一次。关系写在属性正下方，不要重复实体名。
- 不要使用特殊字符。
- 不要使用 middlewares、endpoints 或 hooks。
- 对象使用 YAML 缩写形式，带空格。例如：{ name: issueDate, type: date }
- 不要给单个实体加关系
- 关系使用短格式。例如：' belongsTo:
      - Author'
- 加策略。多数项目只有 "read" 公开策略。当任何人都能提交时（联系表单提交、评论等），部分项目会有 "create" 公开策略
- 使用 "choice" 属性类型时，用 "options.values" 列出选项。例如：`{ name: type, type: choice, options: { values: ["Fire", "Water", "Grass"] } }`
- 不要给实体加 "seedCount" 和 "mainProp"

**文档**
参考 Manifest 文档：https://manifest.build/docs

**示例**
以下是 `backend.yml` 文件内容的示例：
name: My pet app 🐾
entities:
  Owner:
    properties:
      - name
      - { name: birthdate, type: date }

  Cat:
    properties:
      - name
      - { name: age, type: number }
      - { name: birthdate, type: date }
    belongsTo:
      - Owner

  Homepage:
    nameSingular: Home content
    single: true
    properties:
      - title
      - { name: description, type: richText }
      - { name: cover, type: image }"""

CR["medusa-cursorrules/.cursorrules"] = """你是一位资深软件工程师，专精现代 Web 开发，在 TypeScript、Medusa、React.js 与 TailwindCSS 方面有深厚功底。

## Medusa 规则

## 通用规则

- 导入文件时不要使用类型别名。
- 抛错时一律抛 `MedusaError`。
- 取数据一律使用 Query。

## 工作流规则

- 创建工作流或 step 时，一律用 Medusa 的 Workflow SDK `@medusajs/framework/workflows-sdk` 定义。
- 在 API 路由、定时任务或 subscriber 里加功能时，一律为它创建工作流。
- 创建工作流时，一律为它创建 step。
- 工作流中任何数据转换都用 `transform`。
- 工作流中用 `when` 定义条件。
- 调用 step 时不要用 `await`。
- 工作流中不要把工作流函数写成 async。
- 不要给 compensation 函数的入参加类型。
- 工作流中只使用 step。

## 数据模型规则

- 用 `@medusajs/framework/utils` 的 `model` 工具定义数据模型。
- 数据模型的变量名用 camelCase。传给 `model.define` 的数据模型名用 snake_case。
- 给数据模型加 `id` 字段时，一律用 `.primaryKey()` 设成主键。
- 一个数据模型只能有一个 `id`，其它 ID 要用 `text`。
- 数据模型字段用 snake_case。

## 服务规则

- 创建 service 时，方法一律写成 async。
- 如果模块有数据模型，让 service 继承 `MedusaService`。

## 后台定制规则

- 在后台定制中发请求时，一律使用 Medusa 的 JS SDK。
- 样式使用 TailwindCSS。

# 更多资源

- [Medusa 文档](https://docs.medusajs.com/llms-full.txt)"""

ap = argparse.ArgumentParser()
ap.add_argument("--apply", action="store_true")
args = ap.parse_args()

n = 0

# .mdc：读原 globs 后回写
FIELD = re.compile(r"^---\s*\n(.*?)\n---\s*\n?", re.S)
for pkg, files in MDC.items():
    d = P(pkg)
    for fn, (desc, body) in files.items():
        src = os.path.join(d, fn)
        if not os.path.exists(src):
            print("   [缺失]", pkg, fn)
            continue
        raw = open(src, encoding="utf-8", errors="replace").read()
        m = FIELD.match(raw)
        gm = re.search(r"^globs:\s*(.+)$", m.group(1), re.M) if m else None
        globs = gm.group(1).strip() if gm else "*"
        new = f"---\ndescription: {desc}\nglobs: {globs}\n---\n{body}\n"
        print(("[改写] " if new != raw else "[同文] ") + f"{pkg}/{fn}   globs={globs}")
        if args.apply and new != raw:
            open(src, "w", encoding="utf-8").write(new)
        n += 1

# .cursorrules：整篇改写，保留 manifest 那种自带 frontmatter 的文件结构
for rel, body in CR.items():
    # rel 形如 "包名/.cursorrules"，只有第一段是包
    _pkg, _fname = rel.split("/", 1)
    p = os.path.join(P(_pkg), _fname.replace("/", os.sep))
    if not os.path.exists(p):
        print("   [缺失]", rel)
        continue
    raw = open(p, encoding="utf-8", errors="replace").read()
    changed = raw.strip() != body.strip()
    print(("[改写] " if changed else "[同文] ") + f"{rel}   ({len(raw)}B -> {len(body)}B)")
    if args.apply and changed:
        open(p, "w", encoding="utf-8").write(body + "\n")
    n += 1

print()
print("=" * 90)
print(f"第三批计划处理 {n} 个文件")
print("模式：", "已写入" if args.apply else "预演")
