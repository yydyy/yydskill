# Playwright API 测试提示（Playwright API Testing Prompt）

一份专用的 .cursorrules 提示，用于使用 Playwright 配合 TypeScript 和 pw-api-plugin 包创建健壮的 API 测试。

## 你可以构建什么（What You Can Build）

- **API 测试套件**：面向 RESTful API、GraphQL 端点和微服务的综合测试套件
- **Schema 校验测试**：通过 Zod 集成确保 API 响应符合预期的 schema 与契约
- **性能验证**：针对响应时间和吞吐量的基础 API 性能测试
- **身份验证测试流程**：使用各种认证机制测试受保护的 API 端点
- **错误场景测试**：验证 API 错误响应和边界情况

## 优势（Benefits）

- **pw-api-plugin 集成**：利用强大的 pw-api-plugin 包简化 API 测试
- **简化的 API 测试**：无需浏览器开销的精简 API 测试方式
- **全面的验证**：提供验证状态码、响应体和 schema 的工具
- **TypeScript 集成**：完整支持 TypeScript，保证 API 测试代码的类型安全
- **请求组织**：按端点组织 API 测试的结构化方法
- **错误场景覆盖**：内置确保错误场景得到充分测试的实践

## 简要说明（Synopsis）

本提示帮助开发者使用 Playwright 配合 pw-api-plugin 包创建全面的 API 测试。它聚焦于创建可维护、确定性的 API 测试，验证正常路径与错误路径，同时确保状态码正确、响应数据正确并符合 schema。

## .cursorrules 提示内容概述（Overview of .cursorrules Prompt）

.cursorrules 提示通过以下关键要素指导 QA 工程师使用 Playwright 创建有效的 API 测试：

- **pw-api-plugin 用法**：与 pw-api-plugin 包的详细集成，简化 API 测试
- **TypeScript 检测**：自动检测并适配项目中的 TypeScript 使用情况
- **最佳实践**：涵盖 API 测试的九项基本最佳实践，包括命名约定、响应验证和测试独立性
- **示例测试模式**：提供用户端点 API 测试的完整示例，演示状态码验证、schema 验证和错误测试
- **Schema 验证**：使用 Zod 对 API 响应做 schema 验证的高级示例
- **测试组织**：在 test.describe 块中按资源或端点合理组织 API 测试的指南
- **资源专项聚焦**：建议每个 API 资源的测试文件限制在 3-5 个聚焦的测试
