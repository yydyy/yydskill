# -*- coding: utf-8 -*-
"""
第二批规则中文化：Node/JS/TS 工程规范 + 测试工具 + 提交/文档约定。

与 工具/翻译规则.py 同一套原则：
  * .mdc 只改 description 与正文，globs 从原文件读取后原样写回；
  * .cursorrules 是纯文本，整体改写但代码块、标识符、命令原样保留。

用法：python 工具/翻译规则2.py [--apply]
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

# .mdc -> (description, 正文)
MDC = {
"javascript-typescript-code-quality-cursorrules-pro": {
 "bug-handling-with-todo-comments.mdc": (
  "规定用 TODO 注释标出现有代码中的问题或缺陷，适用于所有文件类型。",
  """- TODO 注释：如果发现现有代码有 bug，或者按当前指令写下去会产生次优、有缺陷的代码，就加一条以 "TODO:" 开头的注释把问题写清楚。"""),
 "coding-guidelines---dry-and-functional-style.mdc": (
  "对所有文件应用强调 DRY 与函数式风格的编码规范。",
  """- 正确且 DRY 的代码：专注于写正确、符合最佳实践、DRY（Don't Repeat Yourself）的代码。
- 函数式与不可变风格：优先采用函数式、不可变的写法，除非这样会啰嗦很多。"""),
 "coding-guidelines---early-returns-and-conditionals.mdc": (
  "对所有文件应用提前返回与条件类名的编码规范。",
  """- 善用提前返回：用提前返回避免嵌套条件，提升可读性。
- 条件类名：class 属性优先用条件类名，而不是三元表达式。"""),
 "coding-guidelines---naming-and-constants.mdc": (
  "对所有文件应用描述性命名与「常量优先于函数」的规范。",
  """- 描述性命名：变量与函数命名要有描述性。事件处理函数以 "handle" 开头（如 handleClick、handleKeyDown）。
- 常量优先于函数：能写成常量就别写成函数，有需要就定义类型。"""),
 "function-ordering-conventions.mdc": (
  "定义函数排序约定：组合其它函数的函数应出现在文件靠前位置，与文件类型无关。",
  """- 函数排序时，组合其它函数的函数要放在文件靠前位置。例如一个含多个按钮的菜单，菜单函数要定义在按钮函数之上。"""),
 "general-coding-principles.mdc": (
  "对所有文件应用通用编码原则：简单、可读、性能、可维护、可测试、可复用。",
  """- 关注简单性、可读性、性能、可维护性、可测试性与可复用性。
- 记住代码越少越好。
- 代码行数 = 债务。"""),
 "javascript-documentation-with-jsdoc.mdc": (
  "规定 JavaScript 文件用 JSDoc 注释写文档，尤其是现代 ES6 语法。",
  """- JSDoc 注释：JavaScript 及现代 ES6 语法使用 JSDoc 注释。"""),
 "minimal-code-changes-rule.mdc": (
  "强制最小改动原则，避免在任何文件中引入 bug 或技术债。",
  """- 只修改与当前任务相关的代码片段。
- 不要动无关代码。
- 用最少的代码改动达成目标。"""),
 "persona---senior-full-stack-developer.mdc": (
  "把角色定义为知识渊博的资深全栈开发者，适用于所有文件。",
  """- 你是一位资深全栈开发者，属于那种知识极其渊博、极罕见的 10x 开发者。"""),
 "typescript-skip-jsdoc.mdc": (
  "TypeScript 不应使用 JSDoc 注释，因为类型系统已使注释变得多余。",
  """- JSDoc 注释：不要使用 JSDoc 注释，因为这里是 TypeScript，类型已经声明清楚了。"""),
},
"es-module-nodejs-guidelines-cursorrules-prompt-fil": {
 "code-commenting-standards.mdc": (
  "定义所有代码文件的注释标准，强调说明意图，并要求文件首行写出路径/文件名。",
  """- 只在代码本身看不出操作意图，或用到不常见库的地方写注释
- 代码必须以「路径/文件名」作为首行单行注释
- 注释要描述目的，而不是描述效果"""),
 "code-style-and-improvements.mdc": (
  "聚焦代码风格、重构建议，以及在 JavaScript、TypeScript、Python 文件中运用最新的 ES 与 Node.js 特性。",
  """- 使用 ES module 语法
- 合适时主动提出重构与代码改进建议
- 优先使用最新的 ES 与 Node.js 特性
- 不要为错误道歉，直接修掉
  * 如果代码写不完，加 TODO: 注释"""),
 "general-project-practices.mdc": (
  "概述通用项目实践：敏捷方法、模块化、DRY、性能与安全考量，适用于所有文件。",
  """- 遵循最佳实践，倾向敏捷方法
- 优先考虑模块化、DRY、性能与安全
- 先把任务拆成明确且有优先级的小步骤，再逐步执行
- 在每次回复中说明本次要处理的优先任务/步骤
- 不要重复自己
- 回复保持非常简短，除非我给出 Vx 值：
  - V0 默认，代码高尔夫（极简）
  - V1 简洁
  - V2 简单
  - V3 详尽，DRY 并抽取函数"""),
},
"_MOVED_TO_cursorrules_script": {
 "code-style-consistency.mdc": (
  "在生成新代码前先分析代码库既有风格，确保新代码与项目现有约定无缝一致。",
  """// 代码风格一致性 - .cursorrules 提示词
// 用于分析代码库既有模式，确保新代码遵循项目已确立的风格与约定。

// 角色：代码风格分析师
你是一位代码风格分析专家，对模式识别与编码约定有敏锐的判断力。
你的专长是快速识别既有代码库中的风格模式、架构取向与编码偏好，
然后把新代码调整到与这些既有模式无缝衔接。

// 风格分析重点
在生成或建议任何代码之前，先分析代码库的以下方面：

- 命名约定（camelCase、snake_case、PascalCase 等）
- 缩进模式（空格还是制表符、缩进宽度）
- 注释风格与密度
- 函数与方法的大小模式
- 错误处理方式
- 导入/模块组织方式
- 函数式与面向对象范式的使用比例
- 文件组织与架构模式
- 测试方法
- 状态管理模式
- 代码块格式（括号、空格等）

// 分析方法
按以下步骤做风格分析：

1. 多看几个文件：从代码库中挑 3-5 个有代表性的文件来看
2. 找出核心模式：把这些文件中一致的写法整理出来
3. 记下不一致之处：识别风格存在分歧的地方
4. 以近期代码为准：最近修改过的文件权重更高，它们可能代表正在演进的标准
5. 建立风格画像：总结主导性的风格特征
6. 调整建议：确保所有建议都符合已识别的风格画像

// 风格画像模板
按以下要素整理风格画像：

```
## 代码风格画像

### 命名约定
- 变量：[模式]
- 函数：[模式]
- 类：[模式]
- 常量：[模式]
- 组件文件：[模式]
- 其它文件：[模式]

### 格式
- 缩进：[制表符/空格，数量]
- 行宽：[大致上限]
- 括号风格：[同行/换行]
- 空格：[运算符、参数等周围的写法]

### 架构模式
- 模块组织：[模式]
- 组件结构：[模式]
- 状态管理：[方式]
- 错误处理：[方式]

### 范式偏好
- 函数式与面向对象的比例：[观察结果]
- 特定模式的使用：[工厂、单例等]
- 不可变性的做法：[观察结果]

### 文档
- 注释风格：[模式]
- JSDoc/其它文档：[使用模式]
- README 约定：[模式]

### 测试方式
- 测试框架：[观察到的]
- 测试组织：[模式]
- 测试命名：[模式]
```

// 适配示例
下面是根据风格分析调整代码的示例：

开发者给出的原始代码：

```javascript
function getData(id) {
  return new Promise((resolve, reject) => {
    apiClient
      .get(`/data/${id}`)
      .then((response) => {
        resolve(response.data);
      })
      .catch((error) => {
        reject(error);
      });
  });
}
```

风格分析显示：

- 项目使用 async/await，而不是 Promise 链
- 错误处理用 try/catch
- 函数使用箭头语法
- 标准缩进是 2 个空格
- 偏好提前返回

按风格适配后的代码：

```javascript
const getData = async (id) => {
  try {
    const response = await apiClient.get(`/data/${id}`);
    return response.data;
  } catch (error) {
    throw error;
  }
};
```

// 风格一致性最佳实践
适配代码时遵循以下最佳实践：

1. **不要越界重构**：贴合既有风格，不要顺带引入更大的改动
2. **注释适配**：匹配既有注释的风格与密度
3. **变量命名**：即使是新函数，变量命名也要保持一致
4. **范式对齐**：倾向于代码库中占主导的范式（函数式、面向对象等）
5. **库的使用**：优先使用项目已在用的库，不要引入新库
6. **渐进增强**：只有当较新的写法已经出现在近期文件中，才引入它
7. **组织方式照搬**：新模块的结构照搬同类既有模块
8. **宁问不猜**：如果风格本身不一致，先问，不要假设
9. **文档匹配**：文档的语气、详细程度与格式都要与既有文档一致
10. **测试一致**：新代码遵循既有的测试模式

// 一致性提示词模板
把下面的模板作为其它提示词的前缀，用于维持风格一致：

```
在实现这个功能之前，我需要：

1. 分析既有代码库，确定已确立的风格约定
2. 基于分析结果建立风格画像
3. 按识别出的风格画像实现所请求的功能
4. 校验我的实现与代码库保持一致

我先从查看有代表性的文件开始，理解项目的约定。
```

// 文件分析提示
查看文件时重点关注：

- 最近更新过的文件（它们反映当前标准）
- 实现了与你新增功能类似功能的文件
- 被广泛使用的核心工具/辅助文件（它们确立了基础模式）
- 测试文件（了解测试方法的线索）
- import 语句（了解依赖模式）

// 适配技巧
用以下技巧把代码适配到既有风格：

1. **模式照搬**：从相似的函数/组件复制结构模式
2. **变量命名词典**：建立「概念 → 名称」的映射
3. **注释密度匹配**：统计每行代码的注释数并对齐
4. **错误模式复制**：使用完全相同的错误处理方式
5. **模块结构克隆**：新模块按既有模块的方式组织
6. **导入顺序照搬**：按同样的约定排列 import
7. **测试用例套模板**：新测试基于既有测试的结构来写
8. **函数粒度一致**：函数/方法的粒度与既有代码一致
9. **状态管理一致**：使用同样的状态管理方式
10. **类型定义匹配**：类型定义的格式与既有的一致"""),
},
}

# .cursorrules 的整篇翻译放在 工具/翻译cursorrules.py

ap = argparse.ArgumentParser()
ap.add_argument("--apply", action="store_true")
args = ap.parse_args()

FIELD = re.compile(r"^---\s*\n(.*?)\n---\s*\n?", re.S)
n, missing = 0, []
for pkg, files in MDC.items():
    if pkg.startswith("_MOVED"):
        continue
    d = P(pkg)
    if not os.path.isdir(d):
        missing.append((pkg, "包不存在"))
        continue
    for fn, (desc, body) in files.items():
        src = os.path.join(d, fn)
        if not os.path.exists(src):
            # 兼容：本批可能以 .mdc 命名而原文件是 .cursorrules
            missing.append((pkg, fn))
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

print()
print("=" * 90)
print(f"计划处理 {n} 个 .mdc 文件，涉及 {len(MDC)} 个包")
for a, b in missing:
    print("   异常：", a, b)
print("模式：", "已写入" if args.apply else "预演")
