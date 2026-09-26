# -*- coding: utf-8 -*-
"""
P0+P1 清理执行器（已执行，保留作审计记录）

P0 纯噪音：
  1. 03-技术栈参考/上游英文目录.md        上游 README 抄件（含赞助广告）
  2. 03-技术栈参考/原规则/.cursorrules    上游仓库自己的规则
  3. rails 包的 0 字节 .cursorrules
  4. swift 包的 .cursorrules-mvvm-rxswift_2 冲突副本
  5. salesforce 包的 .cursorrules.txt 扩展名错误
  6. code-pair-interviews/README.md       混入源码目录的说明文档
  7. 工具/一次性迁移.ps1                  已执行完毕的一次性脚本

P1 去重：
  8. 01-工程原则/*/精简版.md    （15 份，与 SKILL.md 正文同文）
  9. 02-个人习惯/*/原文.md      （5 份，段落 100% 被 SKILL.md 包含）
 10. .cursorrules 内容已被 .mdc 完整覆盖的包 → 删 .cursorrules（56 个）
 11. 残留 37 段孤立内容的 17 个包 → 把那几段抽到 补充原文.md 后删 .cursorrules

用法：python 工具/清理P0P1.py --apply     不加 --apply 只打印计划
"""
import os, re, sys, json, shutil, argparse

ROOT = r"D:\Documents\AI技能库"
REF = os.path.join(ROOT, "03-技术栈参考")
RULES = os.path.join(ROOT, "03-技术栈参考", "原规则", "rules")
sys.path.insert(0, os.path.join(ROOT, "工具"))
from 包路径 import MAP as _PKGMAP, pkg_dir as _pkg_dir


def P(pkg):
    """英文包名 -> 改名后的绝对路径"""
    return _pkg_dir(pkg)

# ---------- P0 清单 ----------
P0_FILES = [
    os.path.join(REF, "上游英文目录.md"),
    os.path.join(REF, "原规则", ".cursorrules"),
    P("rails-cursorrules-prompt-file", ".cursorrules"),
    P("swift-uikit-cursorrules-prompt-file", ".cursorrules-mvvm-rxswift_2"),
    P("salesforce-apex-cursorrules-prompt-file", ".cursorrules.txt"),
    P("code-pair-interviews", "README.md"),
    os.path.join(ROOT, "工具", "一次性迁移.ps1"),
]

# ---------- P1 固定清单 ----------
SIMPLIFIED = [
    "DDD精要", "代码大全", "企业应用架构模式", "务实程序员", "发布上线", "处理遗留代码",
    "实现DDD", "数据密集型应用", "整洁代码", "整洁架构", "毛泽东思想视角",
    "软件设计哲学", "重构", "重构大师", "领域驱动设计",
]
ORIGINAL = ["Cocos引擎开发", "框架开发指南", "编码四原则", "规则优先级", "质量保障角色"]


def read(p):
    return open(p, encoding="utf-8", errors="replace").read()


def norm(t):
    t = t.lower()
    t = re.sub(r"[\s`*_#>|]+", " ", t)
    t = re.sub(r"[^a-z0-9\u4e00-\u9fff ]", "", t)
    return re.sub(r"\s+", " ", t).strip()


def norm_lines(t):
    """整行归一化，用于把 .cursorrules 的原始行抽出来。"""
    out = []
    for raw in t.splitlines():
        s = raw.strip()
        if not s or s.startswith(("//", "#", "```", "---")):
            continue
        s2 = re.sub(r"^[-*+\u2022]\s*", "", s)
        s2 = re.sub(r"^\d+[.)]\s*", "", s2)
        s2 = s2.strip('"\',;` ')
        if norm(s2) in PARAGRAPH_SET:
            out.append(s)
    return out


plan = json.load(open(os.path.join(ROOT, "_p1plan.json"), encoding="utf-8"))
orphans = json.load(open(os.path.join(ROOT, "_orphans.json"), encoding="utf-8"))
ORPHAN_BY_PKG = {}
for pkg, text in orphans:
    ORPHAN_BY_PKG.setdefault(pkg, []).append(text)

# A 组：正文段落 100% 被 .mdc 覆盖（0 字节 rails 的 .cursorrules 已在 P0 处理，排除）
delete_cr = [(p, n, cov, size, 0) for p, n, npar, nmiss, cov, size in plan["ready"]
             if n == ".cursorrules" and size > 0]
# B 组零孤立：高覆盖且缺失段落别处已有
for p, n, npar, nmiss, cov, size in plan["keep"]:
    if cov >= 0.85 and p not in ORPHAN_BY_PKG:
        delete_cr.append((p, n, cov, size, 0))
# B 组有孤立：先抽段到 补充原文.md，再删
extract_then_delete = [(p, n, cov, size, len(ORPHAN_BY_PKG[p]))
                      for p, n, npar, nmiss, cov, size in plan["keep"]
                      if cov >= 0.85 and p in ORPHAN_BY_PKG]

keep_both = [x for x in plan["keep"] if x[4] < 0.85]
nodata = plan["nodata"]

ap = argparse.ArgumentParser()
ap.add_argument("--apply", action="store_true")
args = ap.parse_args()


def do(path, why):
    rel = os.path.relpath(path, ROOT)
    if not os.path.exists(path):
        print(f"  [跳过-不存在] {rel}")
        return 0
    size = os.path.getsize(path)
    print(f"  [删除 {size:6d}B] {rel}   <- {why}")
    if args.apply:
        # 一次性迁移.ps1 不硬删，留一份在 文档/ 作历史
        if os.path.basename(path) == "一次性迁移.ps1":
            shutil.move(path, os.path.join(ROOT, "文档", "一次性迁移.ps1.bak"))
            return size
        os.remove(path)
    return size


print("=" * 96)
print("P0 纯噪音")
print("=" * 96)
s0 = sum(do(p, "P0") for p in P0_FILES)

print()
print("=" * 96)
print(f"P1-a 删除与 SKILL.md 同文的 精简版.md（{len(SIMPLIFIED)} 份）")
print("=" * 96)
s1 = 0
for name in SIMPLIFIED:
    p = os.path.join(ROOT, "01-工程原则", name, "精简版.md")
    s1 += do(p, "SKILL.md 正文同文")

print()
print("=" * 96)
print(f"P1-b 删除 100% 被 SKILL.md 包含的 原文.md（{len(ORIGINAL)} 份）")
print("=" * 96)
s2 = 0
for name in ORIGINAL:
    p = os.path.join(ROOT, "02-个人习惯", name, "原文.md")
    s2 += do(p, "SKILL.md 已含全部段落")

print()
print("=" * 96)
print(f"P1-c 删除 .mdc 已完整覆盖的 .cursorrules（{len(delete_cr)} 个包）")
print("=" * 96)
s3 = 0
for p, n, cov, size, _ in sorted(delete_cr, key=lambda x: x[0]):
    s3 += do(P(p, n), f".mdc 覆盖 {cov*100:.1f}%")

print()
print("=" * 96)
print(f"P1-d 先把孤立段落抽到 补充原文.md，再删 .cursorrules（{len(extract_then_delete)} 个包）")
print("=" * 96)
s4 = 0
for p, n, cov, size, norph in sorted(extract_then_delete, key=lambda x: x[0]):
    d = P(p)
    src = os.path.join(d, n)
    if not os.path.exists(src):
        print(f"  [跳过-不存在] {os.path.relpath(src, ROOT)}")
        continue
    PARAGRAPH_SET = set(ORPHAN_BY_PKG[p])
    lines = norm_lines(read(src))
    dest = os.path.join(d, "补充原文.md")
    body = ("# 补充原文\n\n"
            "从原 `.cursorrules` 抽出、未被本包其它文件覆盖的条目（清理时保留）。\n\n"
            + "\n".join(f"- {l}" for l in lines) + "\n")
    print(f"  [抽 {len(lines):2d} 条 → 补充原文.md] {p}   (cov {cov*100:.0f}%)")
    if args.apply:
        open(dest, "w", encoding="utf-8").write(body)
    s4 += do(src, "孤立内容已抽出")

print()
print("=" * 96)
print(f"保留双格式：{len(keep_both)} 个包（.cursorrules 与 .mdc 内容实质不同，非重复）")
print(f"无法判定  ：{len(nodata)} 个包（缺 .mdc 或缺 .cursorrules，无对照物）")
print("=" * 96)
for p, n, npar, nmiss, cov, size in sorted(keep_both, key=lambda x: x[0]):
    print(f"    保留  {cov*100:5.1f}%  {size:6d}B  {p}")
for p, why in nodata:
    print(f"    保留  {why:34s}  {p}")

print()
print("=" * 96)
print(f"合计释放：P0 {s0/1024:.1f} KB + 精简版 {s1/1024:.1f} KB + 原文 {s2/1024:.1f} KB "
      f"+ .cursorrules {s3/1024:.1f} KB = {(s0+s1+s2+s3)/1024:.1f} KB")
print(f"删除文件数：{len(P0_FILES)+len(SIMPLIFIED)+len(ORIGINAL)+len(delete_cr)+len(extract_then_delete)}"
      f"（另新增 {len(extract_then_delete)} 个 补充原文.md）")
print("模式：", "已执行" if args.apply else "预演（加 --apply 才动手）")
