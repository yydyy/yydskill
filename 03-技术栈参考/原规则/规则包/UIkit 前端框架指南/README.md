# UIKit 指南（.cursorrules Prompt 文件）

作者：MoonAndEye

## 可以构建的内容（What You Can Build）
iOS 应用部署 - 面向原生 iOS 应用的 App Store 分发包。按照 Apple 的提交指南提供生产就绪的 IPA 包。实现所需的 provisioning profiles、entitlements 和合规措施以进行公开发布。


## 简介（Synopsis）
使用 SnapKit 实现 Auto Layout，不用 Storyboard/XIB 而以编程方式创建 UI，使用 Factory/Builder 模式管理 UI 组件，实现标准化的 ViewModel，并使用基于闭包的事件处理机制。


## .cursorrules prompt 概述（Overview of .cursorrules prompt）
.cursorrules 文件为使用 Swift 和 UIKit 开发 iOS 应用提供全面指南。它强调遵循最新文档和特性来编写可维护、干净的代码。指南聚焦使用 SnapKit 实现响应式布局、避免 Storyboard/XIB、以编程方式创建所有 UI 组件。它提倡使用视图组合和自定义视图子类来提高可复用性。

文件中列出的原则包括：
1. Auto Layout：使用 SnapKit 实现响应式布局，支持 Dynamic Type 和 Safe Area。
2. 编程式 UI：直接在代码中实现 UI 组件，避免 Storyboard/XIB。
3. MVC/MVVM 原则：UI 组件不应直接访问模型或 DTO。使用 ViewController、Factory 或 Builder 模式。
4. 事件处理：使用闭包传递事件，并确保闭包将 'self' 作为参数传递，供外部对象识别。

遵循这些指南，开发者可以创建高效、可扩展、可维护的 iOS 应用，符合最佳实践和 Apple 的 MVC 原则。
