# JavaScript Chrome API 规范 .cursorrules 提示文件（JavaScript Chrome APIs .cursorrules prompt file）

作者：Tyler H

## 可以构建什么（What You Can Build）
隐私保护扩展：开发一款 Chrome 扩展，通过拦截跟踪脚本和 Cookie、管理所访问网站的权限并提供隐私报告来增强用户隐私。使用 Chrome 开发者工具进行调试，并实现带本地化功能的友好界面。文章摘要工具：创建一款扩展，从在线文章中提取要点并在页面上直接给出简洁摘要。用 content script 分析页面内容、用 popup script 显示摘要，确保性能优化、资源占用最小。暗色模式定制器：一款允许用户在任意网站上自定义暗色模式设置的扩展。用 content script 动态操控 CSS 样式，提供响应式 popup UI 供用户配置，并支持 CSS 框架以增强样式效果。标签页管理与整理工具：构建一个通过分组、重命名和搜索打开的标签页来增强标签页管理的工具。使用 Chrome tabs API 执行操作、storage API 保存标签页分组，并开发直观的选项页面用于配置。语言学习助手：设计一款翻译选中文本并提供语言学习提示的扩展。利用 Chrome 的 i18n API 实现国际化，并用 content script 和安全的消息传递实现翻译服务功能。环保购物助手：创建一款在网购时推荐环保替代品的扩展。用 background script 处理对环保产品数据库的 API 请求，并在商品页面上呈现通知或 UI 增强效果。专注模式拦截器：开发一款效率扩展，在专注时段临时屏蔽分散注意力的网站。用 alarms API 实现定时调度、用 declarative net request 进行拦截，并在 UI 中提供可自定义的专注计时器。会议安排增强器：构建一款与日历平台集成的扩展，根据时区差异和空闲情况推荐最佳会议时间。使用 Chrome 的 storage API 保存用户设置，并用响应式 popup 与日历数据交互。食谱保存整理工具：创建一款保存并分类整理网上食谱的扩展。用 content script 提取食谱信息、storage API 管理数据，用 popup UI 查看和整理已保存的食谱。邮件模板系统：开发一款与 Web 邮件服务集成的扩展，快速访问可复用模板。用 content script 与邮件客户端交互、storage API 管理模板，并提供可配置的选项页面用于创建模板。

## 优势（Benefits）


## 简介（Synopsis）
Chromium 扩展开发者可以借助本提示词，用现代 JavaScript 开发高效、安全的广告拦截器或效率工具，并遵循 Chrome 扩展的最佳实践。

## .cursorrules 提示文件概述（Overview of .cursorrules prompt）
.cursorrules 文件概述了开发 Chrome 扩展的最佳实践与准则。它涵盖多个方面，例如代码风格（强调简洁的 ES6+ JavaScript 和模块化架构）、命名约定（camelCase、PascalCase，常量用大写）以及现代 JavaScript 特性的使用。它还详述了如何组织扩展结构，包括 manifest 文件和 Chrome API 的实现，同时确保安全与性能。此外，它提供了开发流程的步骤、测试与调试技巧，以及在 Chrome Web Store 发布前的准备工作。该文件还鼓励使用国际化功能，并推荐参考示例扩展进行学习。
