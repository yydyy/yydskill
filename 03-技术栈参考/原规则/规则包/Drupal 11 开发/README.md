# Drupal 11 Awesome CursorRules

本仓库提供了一份专为 Drupal 11 项目定制的 **CursorRules** 文件。`.cursorrules` 文件中定义的规则确保 AI 生成的代码符合 Drupal 11 的编码标准、最佳实践与现代架构，充分利用 PHP 8.x、Symfony 6 与 Drupal 的 API。

## 目的

本项目的目标是通过以 Drupal 专属指令引导 AI 工具（如 Cursor AI 编辑器或 VS Code 扩展），实现一致、安全且高效的开发体验。这有助于确保所有代码建议都：

- 与 Drupal 11 完全兼容。
- 符合 Drupal 的编码与性能标准。
- 在模块、主题与 API 开发中采用最佳实践设计。

## 内容

- **`.cursorrules`**：包含 AI 行为的详细指令，涵盖代码结构、命名约定、Drupal API 使用、主题化与安全等指南。
- **`README.md`**：提供项目概述、安装说明与贡献指南。

## 安装

1. **复制规则文件：**  
   将 `.cursorrules` 文件放到 Drupal 11 项目的根目录（即与 `composer.json` 同级的目录）。

2. **在编辑器中启用：**  
   - 如果你使用 Cursor AI 编辑器，请确保已启用项目规则（通常通过设置开关）。
   - VS Code 用户请安装 [Cursor VS Code 扩展](https://marketplace.visualstudio.com/)，并使用其命令面板确保 `.cursorrules` 文件被识别。

3. **提交变更：**  
   添加后将该文件提交到你的仓库，让整个开发团队共享这些规则。

## 参考

- [Awesome CursorRules on GitHub](https://github.com/awesome-cursorrules/awesome-cursorrules)
- [Drupal 11 文档](https://www.drupal.org/docs/understanding-drupal)
- [Drupal 编码标准（PSR-12）](https://www.drupal.org/docs/develop/standards)

## 贡献

欢迎贡献与改进。如果你有建议或增强想法，请提交 issue 或发起 pull request。

## 许可证

本项目采用 MIT 许可证。详情见 [LICENSE](LICENSE) 文件。
