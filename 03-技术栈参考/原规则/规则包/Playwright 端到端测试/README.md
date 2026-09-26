# Playwright 端到端测试（.cursorrules prompt 文件）

作者：Peter M Souza Jr

## 可以构建的内容（What You Can Build）

端到端测试套件：为 Web 应用创建全面的端到端测试套件，验证登录、注册、结账等关键用户流程和交互。测试聚焦验证导航路径、状态更新和错误处理场景，确保应用可靠。现代测试框架：使用 Playwright 开发健壮的测试框架，利用其内置自动等待、强大的选择器和网络拦截能力。该框架提升测试的可靠性和可维护性，同时减少不稳定（flaky）测试。跨浏览器测试解决方案：实现以单一代码库在多个浏览器（Chromium、Firefox、WebKit）上运行的测试，确保在不同浏览器引擎间行为一致。移动端模拟测试：利用 Playwright 的设备模拟能力创建验证应用在移动设备上行为的测试，无需单独的移动端专用代码。视觉验证工作流：构建可捕获和比对截图进行视觉回归测试的工作流，帮助发现不同浏览器和视口下意外的 UI 变化。

## 优点（Benefits）

自动等待机制：利用 Playwright 内置的自动等待，消除显式等待的需要，减少不稳定测试。TypeScript 自动检测：自动识别 TypeScript 项目并相应调整测试代码语法，无需手动配置即可获得类型安全。跨浏览器兼容性：提供单一代码库，以最少配置即可在 Chromium、Firefox 和 WebKit 浏览器上运行。现代 API 方法：使用 async/await 模式和强大的选择器，编写更具可读性和可维护性的测试代码。强大的 Mock 能力：包含健壮的网络拦截，用于测试中的 API mock 和请求操控。

## 简介（Synopsis）

本 prompt 帮助 Web 开发者使用 Playwright 为其应用创建可靠、可维护的端到端测试套件，聚焦关键用户流程和跨多浏览器的行为验证。

## .cursorrules prompt 概述（Overview of .cursorrules prompt）

.cursorrules 文件为使用 Playwright 创建端到端 UI 测试的 QA 工程师和开发者提供指导。它采用感知 TypeScript 的方法，在存在 TypeScript 项目时自动检测并适配。该 prompt 专注于端到端测试，强调关键用户流程和正确的测试结构。它推广诸如使用 test ID 或语义化选择器、利用 Playwright 的自动等待、用 page.route mock 外部依赖、创建每个包含 3-5 个测试的聚焦测试文件等最佳实践。该 prompt 包含一个登录测试的全面示例，演示正确的设置、API mock、交互模式以及对成功和错误场景的断言。用本 prompt 创建的测试验证导航路径、状态更新和错误处理，确保应用可靠。
