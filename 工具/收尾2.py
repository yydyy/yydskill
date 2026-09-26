# -*- coding: utf-8 -*-
"""
最后一步收尾：

1. rules-new/ 已在文件系统改成 精简规则/，同步 目录.md 里 18 条引用与那一节标题，
   并把第一节的机器直译中文名换成真正的中文名。
2. 把 原规则/rules 这个英文目录名也改成 原规则/规则包，并同步所有引用它的地方
   （目录.md 的 196 条路径、工具里的 RULES 常量、文档里的提及）。

用法：python 工具/收尾2.py [--apply]
"""
import os, re, io, sys, argparse

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
ROOT = r"D:\Documents\AI技能库"
REF = os.path.join(ROOT, "03-技术栈参考")
ORIG = os.path.join(REF, "原规则")
RULES = os.path.join(ORIG, "rules")
RULES_CN = os.path.join(ORIG, "规则包")
INDEX = os.path.join(REF, "目录.md")

# 精简规则/ 那 18 个文件的中文名（替换机器直译）
NEW_NAMES = {
 "beefreeSDK.mdc": "BeeFree SDK 无代码编辑器",
 "clean-code.mdc": "整洁代码",
 "codequality.mdc": "代码质量",
 "cpp.mdc": "C++",
 "database.mdc": "数据库",
 "fastapi.mdc": "FastAPI",
 "gitflow.mdc": "Git 流程",
 "medusa.mdc": "Medusa",
 "nativescript.mdc": "NativeScript",
 "nextjs.mdc": "Next.js",
 "node-express.mdc": "Node.js Express",
 "python.mdc": "Python",
 "react.mdc": "React",
 "rust.mdc": "Rust",
 "svelte.mdc": "Svelte",
 "tailwind.mdc": "Tailwind",
 "typescript.mdc": "TypeScript",
 "vue.mdc": "Vue",
}

# 会被改到路径的其它文件
PATCH_FILES = [
    os.path.join(ROOT, "工具", "重命名规则包.py"),
    os.path.join(ROOT, "工具", "包路径.py"),
    os.path.join(ROOT, "工具", "翻译规则.py"),
    os.path.join(ROOT, "工具", "修复目录路径.py"),
    os.path.join(ROOT, "文档", "翻译进度.md"),
    os.path.join(ROOT, "文档", "库体检报告.md"),
    os.path.join(ROOT, "文档", "整理记录.md"),
    os.path.join(ROOT, "工具", "收尾.py"),
    os.path.join(ROOT, "工具", "收尾2.py"),
]

ap = argparse.ArgumentParser()
ap.add_argument("--apply", action="store_true")
args = ap.parse_args()


def step1_index_rules_new():
    txt = open(INDEX, encoding="utf-8").read()
    before = txt
    # 标题
    txt = txt.replace("## 精简新规则 rules-new", "## 精简规则")
    # 路径
    txt = txt.replace("`原规则/rules-new/", "`原规则/精简规则/")
    # 机器直译的中文名换掉
    for fn, cn in NEW_NAMES.items():
        txt = re.sub(rf"^\|\s*[^|]+\|\s*`原规则/精简规则/{re.escape(fn)}`\s*\|$",
                     f"| {cn} | `原规则/精简规则/{fn}` |", txt, flags=re.M)
    print(f"  目录.md：精简规则 引用与名称已同步（{'有改动' if txt != before else '无变化'}）")
    if args.apply:
        open(INDEX, "w", encoding="utf-8").write(txt)


def step2_rename_rules_dir():
    if os.path.isdir(RULES_CN):
        print("  [跳过] 原规则/规则包 已存在")
        return
    if not os.path.isdir(RULES):
        print("  [跳过] 原规则/rules 不存在")
        return
    n = len([d for d in os.listdir(RULES) if os.path.isdir(os.path.join(RULES, d))])
    print(f"  [改名] 原规则/rules -> 原规则/规则包   ({n} 个包)")
    if args.apply:
        os.rename(RULES, RULES_CN)


def step3_patch_refs():
    for p in PATCH_FILES:
        if not os.path.exists(p):
            continue
        txt = open(p, encoding="utf-8").read()
        orig = txt
        txt = txt.replace('"原规则", "规则包"', '"原规则", "规则包"')
        txt = txt.replace("原规则/规则包/", "原规则/规则包/")
        txt = txt.replace("原规则\\rules", "原规则\\规则包")
        txt = txt.replace("`规则包`", "`规则包`")
        if txt != orig:
            print(f"  [改引用] {os.path.relpath(p, ROOT)}")
            if args.apply:
                open(p, "w", encoding="utf-8").write(txt)


print("=" * 86)
print("1. 目录.md 同步 精简规则")
print("=" * 86)
step1_index_rules_new()

print()
print("=" * 86)
print("2. 英文目录名 rules -> 规则包")
print("=" * 86)
step2_rename_rules_dir()

print()
print("=" * 86)
print("3. 同步所有引用")
print("=" * 86)
step3_patch_refs()

print()
print("模式：", "已执行" if args.apply else "预演（加 --apply 才执行）")
