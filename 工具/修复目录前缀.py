# -*- coding: utf-8 -*-
"""
修 目录.md 的路径前缀：原规则/rules/ -> 原规则/规则包/

rules 目录已改名 规则包，但索引里的前缀没跟着换，导致 196 条引用全部失效。
本脚本同时做三件事：
  1. 换前缀；
  2. 用 包路径.py 的反向映射校验每个后缀是不是真实文件夹名，不是就报错；
  3. 打印最终失效数。

用法：python 工具/修复目录前缀.py [--apply]
"""
import os, re, io, sys, argparse

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
ROOT = r"D:\Documents\AI技能库"
sys.path.insert(0, os.path.join(ROOT, "工具"))
from 包路径 import RULES as RULES_DIR  # noqa: E402

REF = os.path.join(ROOT, "03-技术栈参考")
INDEX = os.path.join(REF, "目录.md")

ap = argparse.ArgumentParser()
ap.add_argument("--apply", action="store_true")
args = ap.parse_args()

real = set(os.listdir(RULES_DIR))
txt = open(INDEX, encoding="utf-8").read()

# 1) 统一前缀
old_pref = "原规则/rules/"
new_pref = "原规则/规则包/"
n_pref = txt.count(old_pref)
txt = txt.replace(old_pref, new_pref)
print(f"替换前缀 {old_pref!r} -> {new_pref!r}：{n_pref} 处")

# 2) 校验
refs = re.findall(r"`(原规则/[^`]+)`", txt)
bad = [p for p in refs if not os.path.exists(os.path.join(REF, p))]
print(f"引用 {len(refs)} 条，失效 {len(bad)} 条")
for b in bad[:20]:
    print("   失效:", b)

# 3) 反向映射体检：中文名是否都能映射回英文名
from 包路径 import REVERSE  # noqa: E402
unmapped = [d for d in real if d not in REVERSE]
print(f"\n规则包/ 下 {len(real)} 个文件夹，反向映射缺失 {len(unmapped)} 个")
for u in unmapped:
    print("   ", u)

if args.apply and not bad:
    open(INDEX, "w", encoding="utf-8").write(txt)
    print("\n目录.md 已写入。")
elif args.apply:
    print("\n仍有失效引用，未写入。")
else:
    print("\n模式：预演（加 --apply 才写入）")
