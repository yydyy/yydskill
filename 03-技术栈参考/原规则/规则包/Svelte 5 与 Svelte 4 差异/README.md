# Svelte 5 与 Svelte 4（Svelte 5 vs Svelte 4）.cursorrules 提示词文件

作者：Adam Shand

## 你可以构建什么
Svelte 5 交互式演练场：允许开发者在实时编码环境中试验 Svelte 5 新特性（如 runes、响应式状态、effects 和 snippets）的在线交互平台。它可以与 Svelte 4 并排对比，以展示差异与改进。Svelte 5 代码迁移工具：帮助把项目从 Svelte 4 迁移到 Svelte 5 的 Web 应用。它会自动更新已弃用的语法（如 on: 指令），并把顶层 let 声明、响应式变量等转换为新的 Svelte 5 格式。Svelte 5 进阶教程系列：全面的教程系列，提供涵盖 Svelte 5 所有新特性（包括 $state、$derived、$effect 和 snippets）的详细课程、测验与实战项目。Svelte 5 开发者工具扩展：Chrome 或 Firefox 浏览器扩展，帮助开发者调试和可视化 Svelte 5 应用，具备检查 $state 变化、跟踪依赖与渲染流程等功能。Svelte 5 代码片段库：专门面向 Svelte 5 的可复用代码片段仓库，包含新的响应式声明和 $derived 的高级用法。这些片段可集成到 VSCode 或 Sublime Text 等主流编辑器中。Svelte 5 项目脚手架生成器：基于 CLI 的工具，生成使用 Svelte 5 构建的起步项目模板，预置现代构建工具、状态管理与组件组织方案。Svelte 5 社区论坛：专注于 Svelte 5 及其新特性的讨论、问答和最佳实践分享的在线论坛，可作为开发者互相联系、彼此学习的中心。Svelte 5 性能分析器：分析 Svelte 5 应用性能的 Web 工具，指出可通过 $state.raw 提升性能的环节，并就 effects 与派生状态给出优化建议。Svelte 5 组件市场：开发者买卖、分享用 Svelte 5 构建的组件的在线市场，强调与新响应式模型和 snippet 机制的兼容性。Svelte 5 工作坊系列：面向团队或个人的 Svelte 5 培训工作坊，由经验丰富的 Svelte 开发者带领，聚焦新特性在真实项目场景中的实际应用。Svelte 5 可视化库：利用 Svelte 5 的 $effect 和 $state 特性创建动态实时数据可视化的库或工具集，适用于仪表盘与分析类应用。Svelte 5 事件修饰符建议工具：帮助开发者用包装函数替代已弃用的事件修饰符的应用，就 Svelte 5 中新的事件处理范式给出建议与最佳实践。

## 优势


## 简介
从 Svelte 4 升级到 Svelte 5 的开发者，可以通过使用 runes、$state、$effect 和更新后的事件处理语法，构建具有更强状态管理与响应式能力的应用，从而受益。

## .cursorrules 提示词概述
.cursorrules 文件详细概述了 Svelte 5 相较于 Svelte 4 引入的变化。它重点介绍了 runes 的引入——一组用于增强响应式控制能力的高级原语。文件给出了各关键特性及其用途，例如用 `$state` 声明响应式状态、用 `$derived` 表示派生状态、用 `$effect` 处理副作用，并包含演示每项特性用法的代码示例。文件还讲解了组件 props 与 `$props`、通过 `$bindable` 实现可绑定 props，并描述了 `on:` 指令等某些 Svelte 4 构造的弃用。此外还涵盖 snippets——一种用于可复用标记的新概念，取代 slots 且用法更灵活。文档解释了事件处理器如何被简化为属性，以及事件修饰符的弃用。最后，它通过常见场景的前后对比示例，帮助开发者从 Svelte 4 迁移到 Svelte 5。
