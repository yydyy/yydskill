# Next.js Vercel TypeScript .cursorrules 提示文件（Next.js Vercel TypeScript .cursorrules prompt file）

作者：Oleksii Bondarenko

## 你可以构建什么
AI 驱动的客户支持聊天机器人：使用 ai-sdk-rsc 为网站开发客户支持聊天机器人，集成 Vercel 中间件进行会话管理，并用 KV 数据库持久化对话状态。
实时翻译工具：创建一款实时语言翻译应用，利用 AI SDK RSC 做语言处理，用 KV 数据库保存用户会话状态，并用 Vercel 中间件高效处理请求。
交互式故事平台：构建一个平台，用 AI SDK 生成个性化故事线，把用户选择和故事进度存入 KV 数据库，并用 React Server Components 动态渲染内容。
个性化新闻聚合器：设计一个个性化新闻订阅源，通过 AI SDK RSC 学习用户偏好，用 KV 数据库存储用户数据，并基于存储的偏好通过服务端数据获取推送内容。
AI 增强的代码协作工具：开发一款代码协作工具，利用 AI 提供代码建议，使用 Vercel 的 KV 数据库进行会话管理，并通过 ai-sdk-rsc 实现实时协作。
动态商品推荐引擎：创建一个电商推荐系统，基于用户浏览历史提供 AI 驱动的推荐，利用 KV 数据库存储用户交互，并用 Vercel 中间件高效处理。
交互式虚拟导师：构建一个虚拟辅导平台，用 AI SDK 生成实时教学内容，在 KV 数据库中跟踪学生进度，并通过 Vercel 中间件处理交互。
面向博主的 AI 内容生成器：实现一款博客写作助手，用 AI SDK RSC 提供内容建议和草稿，把用户偏好保存在 KV 数据库中，并通过 React Server Components 处理 UI 更新。
带 AI 辅助的语言学习应用：开发一款语言学习应用，用 AI 进行实时对话练习，用 KV 数据库管理会话状态，并由 Vercel 中间件简化用户会话处理。
音乐创作助手：为音乐人创建一款 AI 驱动的工具，生成创作灵感，把会话数据和用户模式存入 KV 数据库，并通过 React 组件和 AI SDK 集成提供交互式反馈。

## 优势


## 简介
精通 Next.js 和 TypeScript 的开发者，可以使用 React Server Components、Vercel 中间件和 KV 数据库构建可扩展、高效的 AI 驱动界面。

## .cursorrules 提示文件概述
`.cursorrules` 文件提供了一套全面的指南，用于在 Next.js 应用中集成 `ai-sdk-rsc` 库、Vercel 中间件和 KV 数据库。它概述了利用 TypeScript、React Server Components 和 Shadcn/Radix UI 的最佳实践，强调模块化、性能优化和样式处理。文件包含在 `middleware.ts` 中设置中间件、使用 Vercel 的 KV 数据库管理用户会话，以及使用 AI SDK hooks 实现生成式内容流式输出的说明。它还涵盖数据获取策略、状态管理和部署考量，确保应用可扩展且高效。
