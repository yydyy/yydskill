# -*- coding: utf-8 -*-
"""
修复 收尾.py 打补丁时过贪的正则。

收尾.py 用 os\.path\.join\(RULES,\s*([^)]+?)\) 匹配，对
    os.path.join(RULES, "pkg", ".cursorrules")
这种两参数写法，[^)] 一直吃到文件名的右括号，生成
    P('pkg\\.cursorrules')          # 错
应当生成
    os.path.join(P("pkg"), ".cursorrules")

本脚本把错误的 P('a\\b') 形式还原成正确的两参数写法。

用法：python 工具/修复脚本补丁.py [--apply]
"""
import os, re, io, sys, argparse

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
TOOLS = r"D:\Documents\AI技能库\工具"
FILES = ["翻译规则.py", "翻译规则2.py", "翻译规则3.py",
         "翻译cursorrules.py", "翻译补漏.py", "清理P0P1.py"]

# P('pkg\\.cursorrules')  —— 单引号里有一个反斜杠
BAD = re.compile(r"P\('([A-Za-z0-9_.\-]+)\\\\([^']+)'\)")


def fix(m):
    pkg, fname = m.group(1), m.group(2)
    return f"os.path.join(P('{pkg}'), '{fname}')"


ap = argparse.ArgumentParser()
ap.add_argument("--apply", action="store_true")
args = ap.parse_args()

total = 0
for fn in FILES:
    p = os.path.join(TOOLS, fn)
    if not os.path.exists(p):
        print(f"  [跳过] {fn} 不存在")
        continue
    txt = open(p, encoding="utf-8").read()
    hits = BAD.findall(txt)
    if not hits:
        print(f"  [不变] {fn}")
        continue
    new = BAD.sub(fix, txt)
    for pkg, fname in hits:
        print(f"  [修] {fn}:  P('{pkg}\\\\{fname}')  ->  os.path.join(P('{pkg}'), '{fname}')")
    total += len(hits)
    if args.apply:
        open(p, "w", encoding="utf-8").write(new)

print()
print(f"共修复 {total} 处")
print("模式：", "已执行" if args.apply else "预演（加 --apply 才执行）")
