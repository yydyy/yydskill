# Elixir 工程师指南（Elixir Engineer Guidelines）.cursorrules 提示词文件

作者：Zane Riley

## 你可以构建什么
Elixir 微服务平台：开发一个用 Elixir 创建和管理微服务的平台，借助 Docker 进行容器化、PostgreSQL 存储数据，利用 Phoenix LiveView 实现实时数据更新，并提供基于 Phoenix LiveDashboard 的监控面板。实时协作工具：使用 Elixir 和 Phoenix LiveView 创建 Web 应用，允许多名用户同时在项目上协作，结合 Tailwind CSS 实现现代响应式样式，使用 Ecto 管理 PostgreSQL 中的项目数据。自动化 DevOps 流水线：设计使用 Docker 自动化部署流程的 CI/CD 工具，集成 LeftHook 处理 git hooks，用 Sobelow 和 Credo 扫描安全与风格问题，利用 ExUnit 实现测试自动化、用 ExCoveralls 生成测试覆盖率报告。本地化管理系统：使用 Gettext 构建翻译管理系统，让用户轻松为项目添加和更新多语言支持；集成文件系统监视器以自动重新加载更改，并提供友好的文本管理面板。安全通信平台：用 Elixir 和 Phoenix 开发安全消息应用，使用 Swoosh 发送邮件、Finch 发起 HTTP 请求，用 Sobelow 进行持续安全扫描，用 Plug 集成自定义中间件以确保数据安全。事件监控与响应工具：使用 DNS Cluster 进行网络监控、Phoenix LiveDashboard 提供可视化洞察的告警系统，利用 Ecto 和 PostgreSQL 记录事件数据，用 Tailwind CSS 提升 UI/UX 设计。云端电商解决方案：构建可扩展的电商平台，用 Phoenix LiveView 实现动态商品列表、PostgreSQL 管理交易数据，采用 Docker 简化部署，用 Swoosh 发送订单确认邮件。交互式学习平台：利用 Phoenix LiveView 提供实时反馈、用 Ecto 存储练习内容的交互式编程教程平台，支持 Gettext 多语言翻译，并以 Tailwind CSS 保证流畅的样式体验。API 管理与网关：使用 Elixir 的 Plug 路由请求的 API 网关方案，允许开发者设置 API 使用规则并通过 Phoenix LiveDashboard 监控流量，使用 Finch 发起外部 HTTP 请求、Jason 进行数据序列化。可定制的仪表盘工具：使用 Phoenix LiveDashboard 构建自定义仪表盘的工具，允许用户通过 Ecto 集成指标并用 Tailwind CSS 可视化展示，通过 Phoenix LiveView 提供实时数据更新。Q1：如何使用 Ecto 管理分布式 Elixir 服务之间的数据一致性？Q2：使用 Phoenix LiveView 构建应用时应考虑哪些安全最佳实践？Q3：Docker 能从哪些方面提升 Elixir 应用的可扩展性？

## 优势


## 简介
使用 Elixir 和 Phoenix 的开发者可以通过规范化的可靠提交信息，配合全面的代码质量与 CI 实践，构建可扩展、易维护的应用，从而受益。

## .cursorrules 提示词概述
.cursorrules 文件为使用 Elixir、Phoenix、Docker 等多种工具与库的技术栈工作的资深 Elixir 专家工程师制定了指南。它强调在开发前充分考量代码需求，并在回答后提出有洞察力的后续问题。文件还给出了撰写提交信息的结构化方法，详述类型、可选作用域、描述以及可能的正文或页脚，用于说明软件项目中的变更。这确保了代码变更的清晰性、一致性和正确归类。
