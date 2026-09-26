# Next.js 15、React 19、Vercel AI SDK、Tailwind CSS .cursorrules 提示文件（Next.js 15, React 19, Vercel AI SDK, Tailwind CSS .cursorrules prompt file）

作者：Adam Sardo

# 可以构建什么（What You Can Build）

借助这份 `.cursorrules` 配置，你可以使用 Next.js 15、React 19 和 Vercel AI SDK 创建现代、高性能的 Web 应用。该配置专为增强 Cursor IDE 的开发过程而设计，提供稳健的指导、精简的工作流和 AI 增强的最佳实践，用于构建可扩展、可维护且前沿的 Web 解决方案。

# 优势（Benefits）

- **定制化 AI 辅助**：这份 `.cursorrules` 文件针对高级现代 Web 开发微调 Cursor AI 的建议，确保代码补全和指导与项目相关、与项目对齐。
- **一致性与最佳实践**：在整个项目中强制执行 TypeScript、React 和 Next.js 标准，保持一致的编码风格和实践，减少团队成员之间的代码偏移。
- **精简的工作流**：利用预先配置好的错误处理、无障碍、性能优化和测试策略，提升开发速度和生产力。

# 简介（Synopsis）

这份 `.cursorrules` 的灵感来自 Lan（Cursor 创始人）自己的配置（[原始推文](https://x.com/kayladotdev/status/1853272891023872450)）、v0 的系统提示词（[GitHub 链接](https://github.com/sharkqwy/v0prompt)）、[Cursor Directory](https://cursor.directory) 上评分最高的几份配置，以及 Vercel 官方的 Next.js 15 和 AI SDK 文档。

该配置保持最新，纳入了 React 19 和 Next.js 15 的能力，帮助开发者掌握最新的特性和最佳实践，包括服务端渲染、异步组件以及用于聊天和流式能力的 AI 集成方面的最新创新。

# `.cursorrules` 提示文件概述（Overview of `.cursorrules` Prompt）

`.cursorrules` 文件旨在引导 AI 扮演一名专家级资深软件工程师，专长于：

- **现代 Web 开发**：强调 React 19、Next.js 15（App Router）和 TypeScript 等技术。
- **Vercel AI SDK**：用于构建 AI 驱动的流式文本和聊天界面。
- **UI 库**：使用 Shadcn UI、Radix UI 和 Tailwind CSS 构建模块化且无障碍的用户界面。

`.cursorrules` 包含分析、规划和实现需求的详细流程：

1. **分析流程**：识别任务类型、涉及的技术和具体需求，确保 AI 能生成最具上下文感知的方案。
2. **方案规划**：强调模块化、性能和恰当的技术选型，以设计出高质量的方案。
3. **实现策略**：包括无障碍方面的规划、性能影响考量，以及采用最新的 React 和 Next.js 最佳实践。

该文件还提供了丰富的**最佳实践**和**代码规范**：

- **TypeScript 用法**：确保恰当的类型安全、描述性命名，并与 TypeScript 的最新特性保持一致。
- **React 与 Next.js 15**：鼓励使用 React Server Components、Suspense 和服务端渲染来优化性能。
- **异步处理与状态管理**：详解如何有效使用 `useActionState`、`useFormStatus` 和新的异步组件 API。
- **Vercel AI SDK 集成**：讲解如何在服务端和 UI 组件中使用 AI SDK 包来构建 AI 驱动的应用。
