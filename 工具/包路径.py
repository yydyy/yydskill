# -*- coding: utf-8 -*-
"""
共享路径映射：英文包名 → 中文文件夹名。

2026-09-26 把 rules/ 下 178 个包文件夹改成了中文名，原先按英文名定位包的
翻译脚本因此失效。此模块由 工具/重命名规则包.py 的 MAP 派生，供翻译脚本复用。

用法：
    from 包路径 import pkg_dir
    d = pkg_dir("python-fastapi-cursorrules-prompt-file")
"""
import os, re, ast

ROOT = r"D:\Documents\AI技能库"
RULES = os.path.join(ROOT, "03-技术栈参考", "原规则", "规则包")
_RENAME = os.path.join(ROOT, "工具", "重命名规则包.py")

# 从重命名脚本里 AST 解析出 MAP（不执行该脚本）
_tree = ast.parse(open(_RENAME, encoding="utf-8").read())
_RAW = None
for _n in _tree.body:
    if isinstance(_n, ast.Assign) and getattr(_n.targets[0], "id", "") == "MAP":
        _RAW = ast.literal_eval(_n.value)
assert _RAW, "没能从 重命名规则包.py 解析出 MAP"

_ILLEGAL = set('<>:"/\\|?*')


def _sanitize(name):
    out = name.replace("/", "·")
    out = "".join(c for c in out if c not in _ILLEGAL)
    out = re.sub(r"\s+", " ", out).strip().rstrip(".")
    if not any("\u4e00" <= c <= "\u9fff" for c in out):
        out = out + " 规范"
    return out


# 英文名 → 中文文件夹名（含手工补充的、不在 MAP 里的包）
MAP = {old: _sanitize(new) for old, new in _RAW.items()}
EXTRA = {
    "flutter-development-guidelines-cursorrules-prompt-file": "Flutter 开发规范",
}
MAP.update(EXTRA)
# 反向：中文名 → 英文名
REVERSE = {v: k for k, v in MAP.items()}


def pkg_dir(name):
    """传英文包名或中文文件夹名，都返回绝对路径。找不到就抛错，不静默返回。"""
    cn = MAP.get(name, name)
    p = os.path.join(RULES, cn)
    if not os.path.isdir(p):
        raise FileNotFoundError(f"包不存在：{name!r} -> {cn!r}")
    return p


def all_pkg_dirs():
    return sorted(
        os.path.join(RULES, d) for d in os.listdir(RULES)
        if os.path.isdir(os.path.join(RULES, d))
    )


if __name__ == "__main__":
    import io, sys
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    real = set(os.listdir(RULES))
    print(f"RULES = {RULES}")
    print(f"实际文件夹 {len(real)} 个，映射表 {len(MAP)} 条")
    missing = [c for c in MAP.values() if c not in real]
    print(f"映射到不存在文件夹的条目：{len(missing)}")
    for m in missing:
        print("   ", m)
