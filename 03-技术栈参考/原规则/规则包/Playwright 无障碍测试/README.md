# Playwright 无障碍测试提示（Playwright Accessibility Testing Prompt）

一份专用的 .cursorrules 提示，用于使用 Playwright 配合 TypeScript 和 axe-core 创建全面的无障碍测试。

## 你可以构建什么（What You Can Build）

- **自动化无障碍审计**：全面扫描 WCAG 合规性问题
- **键盘导航测试**：验证关键用户流程的键盘无障碍性
- **屏幕阅读器兼容性测试**：确保屏幕阅读器播报正确的测试
- **响应式无障碍测试**：检查不同视口尺寸下的无障碍表现
- **ARIA 验证**：确保 ARIA 角色和属性正确实现的测试

## 优势（Benefits）

- **WCAG 合规**：针对 Web 内容无障碍指南（WCAG）的自动化验证
- **完整的 TypeScript 支持**：完整的 TypeScript 集成，编写类型安全的无障碍测试
- **全面的测试**：提供自动化和手动无障碍验证的工具
- **可执行的报告**：清晰报告问题并给出修复建议
- **与 axe-core 集成**：利用业界标准的无障碍测试引擎

## 简要说明（Synopsis）

本提示帮助开发者使用 Playwright 和 axe-core 创建全面的无障碍测试，确保 Web 应用对残障用户无障碍并符合 WCAG 标准。

## .cursorrules 提示内容概述（Overview of .cursorrules Prompt）

.cursorrules 提示通过以下关键要素指导 QA 工程师使用 Playwright 创建有效的无障碍测试：

- **TypeScript 检测**：自动检测并适配项目中的 TypeScript 使用情况
- **最佳实践**：涵盖无障碍测试的九项基本最佳实践，包括全面覆盖、颜色对比度测试和焦点管理
- **示例测试模式**：提供登录页无障碍测试的详细示例，包含自动违规检查、键盘导航测试和 ARIA 属性验证
- **WCAG 标准**：确保测试符合 WCAG 2.1 AA 标准和无障碍最佳实践
- **报告配置**：生成详细无障碍违规报告的指南
