# AI技能库

个人整理的 AI 编码规则与 skill，不绑定任何模型或工具。`SKILL.md` 遵循 [Agent Skills 开放标准](https://agentskills.io/specification)，Claude Code、Codex、Cursor、Gemini CLI 等支持该标准的工具都能直接用。

**要把 skill 装进项目，看 [部署指南.md](部署指南.md)**。可以直接让 AI 照着执行，例如："按 D:\Documents\yydskill\部署指南.md 给当前项目配上 skill"。

## 目录

| 目录 | 内容 | 语言 |
| --- | --- | --- |
| `01-工程原则` | 11 本经典书蒸馏成的 skill，每本两份：`SKILL.md`（精简）+ `完整版.md`（含完整的生成规则、禁止模式） | 标题和 `description` 中文，正文英文 |
| `02-个人习惯` | 自己的编码原则、规则优先级、质量检查、Cocos 与自研框架约束 | 中文 |
| `文档` | [外部工具登记](文档/外部工具登记.md)：装在别处但在用的 skill / MCP | 中文 |
| [目录.json](目录.json) | 全部 16 个 skill 的清单：id、源路径、部署方式、适用范围、标签 | — |

`02-个人习惯` 里有两类特殊的：

- `规则优先级`、`编码四原则` 是需要常驻的规则（`deploy: agents-md`），部署时合进项目的 `AGENTS.md`，不作为按需触发的 skill。
- `框架开发指南` 只适用于使用 `cocosFrameworkCli` 的项目。

## 命名约定

- 库内文件夹用中文，方便自己浏览。
- `SKILL.md` 的 YAML `name` 用英文 kebab-case，与 `目录.json` 的 `id` 相同。
- 标准要求文件夹名与 `name` 一致，所以**部署时文件夹要改名为 `id`**，部署指南里已写明。

## 维护

**新增 skill**：

1. 在 `01-工程原则` 或 `02-个人习惯` 下建中文文件夹，写 `SKILL.md`。frontmatter 里 `name` 用英文 kebab-case；`description` 写清"做什么 + 什么时候用"，它决定 skill 能否被正确触发。
2. `SKILL.md` 控制在 500 行以内，细节放同目录的其他文件，并在 `SKILL.md` 里用相对链接引用。
3. 在 [目录.json](目录.json) 补一条，填好 `id`、`folder`、`deploy`、`scope`、`tags`。

**改名或删除**：同步改 `目录.json`。已经部署到各项目和用户级目录的旧副本不会自动更新，需要手动清理。

## 来源与许可

- `01-工程原则` 蒸馏自 agent-rules-books（MIT）。
- 原先的 `03-技术栈参考`（awesome-cursorrules 社区规则，CC0）已删除，需要时去上游 [PatrickJS/awesome-cursorrules](https://github.com/PatrickJS/awesome-cursorrules) 取。
