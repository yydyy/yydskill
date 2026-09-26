# -*- coding: utf-8 -*-
"""
处理 转mdc 有意跳过的 3 个 .cursorrules：

1. Go Temporal 工作流 DSL/.cursorrules
   正文 0 字符，是个索引清单（frontmatter 里 rules: 列了 5 个 .mdc），
   真正的规则已在同包 index/guide/workflow/activities/example-usage 五个 .mdc 里。
   → 删除（转成 .mdc 只会得到一个空文件）。

2/3. Solidity+React 区块链应用、Vue 3+Nuxt 3+TypeScript 规范
   正文是 AI 的道歉语（"I'm sorry, but it seems like you haven't provided..."），
   上游抓取时文件已损坏，共 284 B。正文无任何规则内容。
   → 不转格式，删掉损坏文件；同时删掉只为它们而存在的空壳包目录。

用法：python 工具/清理残留cursorrules.py [--apply]
"""
import os, io, sys, shutil, argparse

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
ROOT = r"D:\Documents\AI技能库"
REF = os.path.join(ROOT, "03-技术栈参考")
RULES = os.path.join(REF, "原规则", "规则包")

INDEX_PKG = "Go Temporal 工作流 DSL"
CORRUPT = [
    ("Solidity+React 区块链应用", ".cursorrules"),
    ("Vue 3+Nuxt 3+TypeScript 规范", ".cursorrules"),
]

ap = argparse.ArgumentParser()
ap.add_argument("--apply", action="store_true")
args = ap.parse_args()


def show(pkg):
    d = os.path.join(RULES, pkg)
    if not os.path.isdir(d):
        print(f"   [缺失] {pkg}")
        return None
    fs = sorted(os.listdir(d))
    real = [f for f in fs if f != "README.md"]
    print(f"   {pkg}/  ——  非 README 文件 {len(real)} 个: {real}")
    return real


print("=" * 90)
print("1. Go Temporal 工作流 DSL：删除空索引 .cursorrules")
print("=" * 90)
show(INDEX_PKG)
p = os.path.join(RULES, INDEX_PKG, ".cursorrules")
if args.apply and os.path.exists(p):
    os.remove(p)
    print("   [删除] .cursorrules")

print()
print("=" * 90)
print("2/3. 两个损坏包：正文是 AI 道歉语，剩余内容是抓错的 Python 规则")
print("=" * 90)
for pkg, fn in CORRUPT:
    real = show(pkg)
    p = os.path.join(RULES, pkg, fn)
    if real is not None:
        d = os.path.join(RULES, pkg)
        left = [f for f in real if f != fn]
        print(f"   -> 删损坏文件 {fn}；剩余 {left}")
        print(f"      剩余文件正文为 'Always use UV / python 3.12 / classes instead of functions'，")
        print(f"      globs 指向 /service-1/，与包名（{pkg}）无关，且与『Python 开发者规范』重复 → 整包删除")
        if args.apply:
            shutil.rmtree(d)

print()
print("模式：", "已执行" if args.apply else "预演（加 --apply 才执行）")
