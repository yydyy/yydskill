# Vitest 单元测试 Prompt（Vitest Unit Testing Prompt）

一个专门用于使用 Vitest 创建全面单元测试（支持 TypeScript）的 .cursorrules prompt。

## 可以构建的内容（What You Can Build）

- **单元测试套件**：针对关键业务逻辑和工具函数的聚焦测试
- **基于 Mock 的测试**：使用 vi.mock 将代码与外部依赖正确隔离的测试
- **数据驱动测试**：跨多种数据场景验证功能的测试
- **TypeScript 测试**：带正确接口定义和类型断言的强类型测试
- **边缘情况覆盖**：处理 undefined 值、类型不匹配等边缘情况的测试

## 优点（Benefits）

- **现代测试框架**：利用 Vitest 的速度及其与 Vite 项目的兼容性
- **ESM 优先的方法**：支持带顶层 await 和动态导入的 ES modules
- **正确的依赖隔离**：在导入之前一致地 mock 依赖
- **完整的 TypeScript 支持**：对被测函数和 mock 的依赖提供全面的类型安全
- **全面的测试覆盖**：以各种数据场景聚焦业务逻辑
- **可维护的测试结构**：以清晰的 arrange-act-assert 模式组织测试

## 简介（Synopsis）

本 prompt 帮助开发者用 Vitest 创建高质量单元测试，聚焦关键功能，同时确保正确 mock 依赖、覆盖全面的数据场景和边缘情况。

## .cursorrules prompt 概述（Overview of .cursorrules Prompt）

.cursorrules prompt 指导开发者使用 Vitest 创建有效的单元测试，包含以下关键要素：

- **TypeScript 检测**：自动检测项目中是否使用 TypeScript 并相应适配
- **依赖 Mock**：使用 vi.mock 在导入之前正确 mock 依赖的指南
- **最佳实践**：单元测试的八项基本实践，包括聚焦关键功能、数据场景和边缘情况
- **示例测试模式**：提供 JavaScript 和 TypeScript 单元测试的详细示例，结构正确
- **可维护的方法**：每个文件专注于编写有限数量的高价值测试
- **测试组织**：使用 describe/it 块并以描述性名称组织测试
- **AAA 模式**：使用 Arrange-Act-Assert 模式的示例，结构清晰
