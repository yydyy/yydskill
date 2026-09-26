# Cypress API 测试 .cursorrules 提示文件（Cypress API Testing .cursorrules prompt file）

作者：Peter M Souza Jr

## 你可以构建什么

API 测试套件：创建全面的 API 测试套件，验证关键端点、响应结构和错误处理模式。测试使用 cypress-ajv-schema-validator 确保 API 响应符合预期的 JSON schema，提供超越简单属性检查的稳健校验。
Schema 校验框架：开发结构化的 API 测试方法，为不同资源编写文档完善的 schema 定义，创建可随 API 一起演进的可维护校验体系。
错误处理验证：实现系统化验证 API 如何响应无效请求、缺失认证及其他错误条件的测试，确保应用中错误处理的一致性。
认证测试策略：为需认证的端点构建测试策略，验证应用 API 层的访问控制、令牌校验和权限检查是否正确。
自动化 API 契约测试：创建验证 API 符合其文档规范的测试体系，作为活的文档，验证前端与后端组件之间的契约。

## 优势

基于 Schema 的校验：使用 cypress-ajv-schema-validator 执行全面的 JSON schema 校验，而非逐项属性检查。
TypeScript 自动检测：自动识别 TypeScript 项目并相应调整测试代码语法，无需手动配置即可获得类型安全。
全面覆盖：同时测试正常路径和错误场景，完整验证 API 功能。
测试独立性：倡导创建隔离的、确定性的测试，不依赖现有服务器状态或其他测试的执行。

## 简介

这一提示词赋能开发者使用 Cypress 与 cypress-ajv-schema-validator 包创建稳健的 API 测试，验证端点行为、响应 schema 和错误处理。

## .cursorrules 提示文件概述

`.cursorrules` 文件为使用 Cypress 创建 API 测试的 QA 工程师和开发者提供指导。它强调使用 cypress-ajv-schema-validator 包进行响应 schema 的全面校验，以及正确的状态码和错误消息验证。该提示词采用 TypeScript 感知的方式，在存在 TypeScript 项目时自动检测并适配。它推广描述性测试命名、测试独立性，以及按端点或资源对 API 测试进行恰当分组等最佳实践。用这一提示词创建的测试聚焦验证成功操作和错误处理场景，确保 API 在各种条件下行为正确。该提示词包含一个详细示例，演示了针对用户 API 端点的 schema 定义、请求实现和校验模式。
