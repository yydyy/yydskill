# SvelteKit TypeScript 指南 .cursorrules 提示文件

作者：Brandon Edley

## 可以构建什么
SvelteKit 项目起步模板：一个模板生成器，用于快速启动基于 SvelteKit、Supabase 和 Drizzle 的项目。该工具会配置 SSR、SSG 以及基于 Supabase 的实时数据，开发者只需添加自定义内容。实时聊天应用：一个使用 SvelteKit 的实时聊天应用，用 Supabase 进行身份验证、用 Drizzle 进行状态管理。它会利用 SvelteKit 的 SSR 能力确保快速加载和无缝的身份验证切换。电商平台：用 SvelteKit 构建可扩展的电商平台，使用 Supabase 管理商品库存和用户账户。该方案侧重用 SSR 高效服务端渲染商品页面，并用 SSG 将高流量页面转化为静态内容。个人博客网站：一个使用 SvelteKit 和 Tailwind CSS 的轻量级博客平台。网站支持静态站点生成与动态内容区块，作者可通过 Supabase 后端动态编辑和发布文章。多语言内容管理系统（CMS）：用 SvelteKit 和 Paraglide.js 实现一个 CMS，通过 Supabase 支持国际化和动态内容加载。该 CMS 提供简便的机制来创建和管理跨多种语言的内容。任务管理应用：一个基于 SvelteKit 的任务管理应用，使用 Supabase 实现实时协作、Drizzle 管理前端状态。应用具备动态更新和 SSR，缩短加载时间。用户身份验证模板：一组 SvelteKit 组件和模板，让开发者能借助 Supabase 的认证功能实现复杂的身份验证流程，如 OAuth 和 PKCE。在线作品集创建工具：一个让用户使用 SvelteKit、可定制的 Shadcn 组件和 Tailwind CSS 样式创建在线作品集的工具。平台使用 Supabase 存储内容并动态渲染站点。交互式数据仪表板：使用 SvelteKit 和 Supabase 创建一个仪表板应用，在合适时针对 SSR 和静态内容优化，展示来自 Supabase 数据库的实时分析和报表，为团队提供协作界面。活动管理系统：用 SvelteKit 开发活动管理系统，具备日程安排、参会者注册以及通过 Supabase 实时更新等功能。系统利用 SSR 高效渲染页面，并用 load 函数获取数据。SEO 优化博客生成器：一个让博主创建 SEO 优化博文的应用，通过 SvelteKit 的 Svelte:head 组件管理 meta 标签，并用 SSR 快速交付内容。SvelteKit 组件库：一个用 Svelte 5、Shadcn 组件和 Tailwind CSS 设计的可复用组件库，开发者可快速集成到任何 SvelteKit 项目中。Supabase 起步套件：一个提供 Supabase 与 SvelteKit 配合使用的最佳实践配置的工具包，包含身份验证流程、实时功能和数据库优化。该套件帮助开发者以最少的设置快速搭建应用。响应式 Web 应用框架：创建一个使用 SvelteKit 和 Tailwind CSS 的响应式 Web 应用框架，注重性能优化，面向构建跨平台移动和桌面应用的开发者。动态表单构建器：一个基于 GUI 的动态表单构建器，使用 SvelteKit，内置校验、服务端表单处理，并集成 Supabase 存储提交的数据。该工具让没有编程经验的人也能创建和管理复杂的表单工作流。

## 优势


## 简介
正在构建带 Supabase 集成的实时应用的 SvelteKit 项目开发者，可以使用本提示获得关于最佳实践、代码组织和 TypeScript 类型安全方面的指导。

## .cursorrules 提示概览
该 .cursorrules 文件概述了使用 Svelte 5、SvelteKit、TypeScript、Supabase、Drizzle 以及现代最佳实践进行 Web 开发的全面指南。它强调编写简洁、技术性强的代码并给出示例，利用 SvelteKit 的服务端渲染和静态站点生成，并以最少的 JavaScript 优化性能。它提供了命名、文件组织和代码结构方面的约定，侧重函数式与声明式编程以及 TypeScript 的使用。文件包含使用 Tailwind CSS 和 Shadcn 组件进行 UI 样式设计、颜色约定、状态管理、路由、API 开发、SEO、表单以及使用 Paraglide.js 的国际化等指南。它还强调无障碍性、性能优化和 Supabase 集成的最佳实践，包括安全措施和错误处理。此外，还提供了相关文档链接，以便深入理解和参考。
