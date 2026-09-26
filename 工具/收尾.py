# -*- coding: utf-8 -*-
"""
收尾三件事：

1. 处理 rules/ 下那个孤立的裸文件 flutter-development-guidelines-cursorrules-prompt-file
   —— 它是全库唯一没进文件夹的包。建 中文文件夹 + 补 frontmatter + 翻译正文。
2. rules-new/ 改名 精简规则/（16 个文件内容唯一，不是重复，保留）。
3. 翻译脚本改走 工具/包路径.py 的共享映射，修掉改名导致的失效。

用法：python 工具/收尾.py [--apply]
"""
import os, io, sys, re, shutil, argparse

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
ROOT = r"D:\Documents\AI技能库"
REF = os.path.join(ROOT, "03-技术栈参考")
RULES = os.path.join(REF, "原规则", "规则包")
NEWDIR = os.path.join(REF, "原规则", "rules-new")
TOOLS = os.path.join(ROOT, "工具")

# ---------------------------------------------------------------- 1. Flutter 孤儿文件
FLUTTER_SRC = os.path.join(RULES, "flutter-development-guidelines-cursorrules-prompt-file")
FLUTTER_DIR = os.path.join(RULES, "Flutter 开发规范")
FLUTTER_DST = os.path.join(FLUTTER_DIR, "flutter-development-guidelines.mdc")
FLUTTER_DESC = "Flutter 开发规范：代码风格与结构、/lib 目录组织、命名约定、导入顺序、UI 与主题、性能优化、Riverpod 状态管理与 MVVM 架构。"
FLUTTER_BODY = """### 代码风格与结构
- 写简洁高效的源码。
- 追求易读易维护的源码，示例要准确。
- 避免重复代码：把 widget 与函数模块化成可复用组件。
- 变量命名要有描述性：使用带助动词的命名，如 isLoading、hasError。

### /lib 下的目录结构
- /lib/models/：数据模型与类型定义（Model）
- /lib/viewmodels/：状态管理与业务逻辑（ViewModel）
- /lib/views/widgets/：可复用 widget（View）
- /lib/views/screens/：按屏幕划分的 widget（View）
- /lib/services/：API 调用与数据访问的 service 类
- /lib/utils/：辅助函数与常量

### 命名约定
- 目录与文件：用 snake_case（如 auth_wizard.dart）。
- UpperCamelCase：用于类名/枚举/typedef/类型参数等。
- lowerCamelCase：用于变量/函数/类成员（属性、方法）等。
- lowercase_with_underscores（snake_case）：用于文件/目录/包/库等。

### 导入
- 以 dart: 开头的导入放最前（导入前缀用小写加下划线）。
- 其次是第三方包（package:）。
- 最后才是项目内的相对路径与文件。

### 使用 Dart
- 用好类型安全：所有代码都用静态类型，并尽量利用类型推断。

### UI 与样式
- 使用 Material widget。
- 统一主题：用 ThemeData 应用一致的样式。

### 性能优化
- 不需要状态时优先用 StatelessWidget。
- 善用 const 构造函数：widget 不可变时用 const 优化构建。

### 状态管理
- 用 riverpod 实现高效的状态管理。
- 在 ViewModel 中管理状态，并与 View 关联。

### 软件架构
使用 MVVM（Model-View-ViewModel）。

### 关键规则
- 为提升可读性，每行不超过 80 个字符。
- 所有流程控制结构（if、for、while 等）都加花括号 {}。
- 主动写注释，帮助理解和维护代码。
- 用单引号，避免双引号，字符串字面量风格保持一致以提升可读性。"""

ap = argparse.ArgumentParser()
ap.add_argument("--apply", action="store_true")
args = ap.parse_args()


def do_flutter():
    if os.path.isdir(FLUTTER_DIR):
        print("  [跳过] Flutter 开发规范/ 已存在")
        return
    if not os.path.isfile(FLUTTER_SRC):
        print("  [跳过] 孤儿文件不存在")
        return
    print(f"  [建目录 + 移入 + 补 frontmatter + 翻译]")
    print(f"      {os.path.basename(FLUTTER_SRC)}")
    print(f"      -> Flutter 开发规范/flutter-development-guidelines.mdc")
    if args.apply:
        os.makedirs(FLUTTER_DIR, exist_ok=True)
        os.remove(FLUTTER_SRC)
        with open(FLUTTER_DST, "w", encoding="utf-8") as f:
            f.write(f"---\ndescription: {FLUTTER_DESC}\nglobs: lib/**/*.dart\n---\n{FLUTTER_BODY}\n")


def do_rules_new():
    target = os.path.join(REF, "原规则", "精简规则")
    if os.path.isdir(target):
        print("  [跳过] 精简规则/ 已存在")
        return
    if not os.path.isdir(NEWDIR):
        print("  [跳过] rules-new/ 不存在")
        return
    n = len(os.listdir(NEWDIR))
    print(f"  [改名] rules-new/ -> 精简规则/   ({n} 个文件)")
    if args.apply:
        os.rename(NEWDIR, target)


# 把翻译脚本里 RULES 常量的定义换成走共享映射
PATCH = {
    "翻译规则.py": None, "翻译规则2.py": None, "翻译规则3.py": None,
    "翻译cursorrules.py": None, "翻译补漏.py": None, "清理P0P1.py": None,
}
OLD_RE = re.compile(r'^RULES = os\.path\.join\(.*\)$', re.M)
NEW_LINE = (
    'RULES = os.path.join(ROOT, "03-技术栈参考", "原规则", "规则包")\n'
    'sys.path.insert(0, os.path.join(ROOT, "工具"))\n'
    'from 包路径 import MAP as _PKGMAP, pkg_dir as _pkg_dir\n'
    '\n'
    '\n'
    'def P(pkg):\n'
    '    """英文包名 -> 改名后的绝对路径"""\n'
    '    return _pkg_dir(pkg)\n'
)

# 脚本内部仍按英文包名拼路径，改成走 P()
JOIN_RE = re.compile(r'os\.path\.join\(RULES,\s*([^)]+?)\)')


def do_patch_scripts():
    for fn in PATCH:
        p = os.path.join(TOOLS, fn)
        if not os.path.exists(p):
            print(f"  [跳过] {fn} 不存在")
            continue
        txt = open(p, encoding="utf-8").read()
        orig = txt
        notes = []
        if "from 包路径 import" not in txt:
            if not OLD_RE.search(txt):
                print(f"  [跳过] {fn} 没找到 RULES 定义，需人工看")
                continue
            txt = OLD_RE.sub(NEW_LINE.rstrip("\n"), txt, count=1)
            notes.append("RULES 走共享映射")
        # 把 os.path.join(RULES, <包名>) 换成 P(<包名>)
        n_join = len(JOIN_RE.findall(txt))
        if n_join:
            def rep(m):
                inner = m.group(1).strip()
                # 只替换“英文包名”这种用法，保留 RULES 自身定义行
                return f"P({inner})"
            txt = JOIN_RE.sub(rep, txt)
            notes.append(f"{n_join} 处包路径改走 P()")
        if txt == orig:
            print(f"  [跳过] {fn} 无需改动")
            continue
        print(f"  [打补丁] {fn}：" + "、".join(notes))
        if args.apply:
            open(p, "w", encoding="utf-8").write(txt)


print("=" * 86)
print("1. 处理孤立的 Flutter 裸文件")
print("=" * 86)
do_flutter()

print()
print("=" * 86)
print("2. rules-new/ 改中文名")
print("=" * 86)
do_rules_new()

print()
print("=" * 86)
print("3. 修因改名而失效的脚本")
print("=" * 86)
do_patch_scripts()

print()
print("模式：", "已执行" if args.apply else "预演（加 --apply 才执行）")
