# -*- coding: utf-8 -*-
"""
修复 目录.md 中 51 条指向不存在文件夹的路径。

成因：重命名时文件夹名走了 sanitize()（/ → ·），但回写 目录.md 用的是未 sanitize
的 MAP 原始值，于是路径里留下了 /，与实际文件夹名对不上。

做法：用同一张 MAP 表，把每个引用后缀映射成 sanitize 后的真实文件夹名；
映射不上的直接报错，不静默跳过。

用法：python 工具/修复目录路径.py [--apply]
"""
import os, re, io, sys, ast, argparse

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
ROOT = r"D:\Documents\AI技能库"
REF = os.path.join(ROOT, "03-技术栈参考")
RULES = os.path.join(REF, "原规则", "规则包")
INDEX = os.path.join(REF, "目录.md")
RENAME = os.path.join(ROOT, "工具", "重命名规则包.py")

# 从重命名脚本里取出 MAP（AST 解析，不执行脚本）
tree = ast.parse(open(RENAME, encoding="utf-8").read())
MAP = None
for node in tree.body:
    if isinstance(node, ast.Assign) and getattr(node.targets[0], "id", "") == "MAP":
        MAP = ast.literal_eval(node.value)
assert MAP, "没能从 重命名规则包.py 里解析出 MAP"

ILLEGAL = set('<>:"/\\|?*')


def sanitize(name):
    out = name.replace("/", "·")
    out = "".join(c for c in out if c not in ILLEGAL)
    out = re.sub(r"\s+", " ", out).strip().rstrip(".")
    if not any("\u4e00" <= c <= "\u9fff" for c in out):
        out = out + " 规范"
    return out


OLD2NEW = {old: sanitize(new) for old, new in MAP.items()}
real = set(os.listdir(RULES))

ap = argparse.ArgumentParser()
ap.add_argument("--apply", action="store_true")
args = ap.parse_args()

raw = open(INDEX, encoding="utf-8").read()
lines = raw.split("\n")

fixed, trouble = [], []
for i, line in enumerate(lines, 1):
    if "原规则/规则包/" not in line:
        continue
    def repl(m):
        span = m.group(1)
        suf = span[len("原规则/规则包/"):]
        if suf in real:
            return m.group(0)              # 已经是有效路径，不动
        # 先用映射表还原
        if suf in OLD2NEW:
            new = OLD2NEW[suf]
            if new in real:
                fixed.append((i, suf, new))
                return f"`原规则/规则包/{new}`"
        # 再试：文件名本身已是新名，只有 / 与 · 的差异
        cand = sanitize(suf)
        if cand in real:
            fixed.append((i, suf, cand))
            return f"`原规则/规则包/{cand}`"
        trouble.append((i, suf))
        return m.group(0)
    lines[i - 1] = re.sub(r"`([^`]*原规则/规则包/[^`]*)`", repl, line)

print(f"修复 {len(fixed)} 条：")
for i, old, new in fixed:
    print(f"  L{i}: {old!r}\n        -> {new}")
if trouble:
    print(f"\n[错误] {len(trouble)} 条无法映射，请人工处理：")
    for i, s in trouble:
        print(f"  L{i}: {s!r}")

new_raw = "\n".join(lines)
if args.apply and not trouble:
    open(INDEX, "w", encoding="utf-8").write(new_raw)
    print(f"\n目录.md 已写入。")
elif args.apply:
    print("\n有无法映射的条目，未写入。")
else:
    print("\n模式：预演（加 --apply 才写入）")
