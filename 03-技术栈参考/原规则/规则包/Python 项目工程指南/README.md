# Python 项目工程指南 .cursorrules 提示文件（Python Projects Guide .cursorrules prompt file）

作者：bossjones

## 可以构建什么（What You Can Build）
AI 驱动的 Python 项目样板生成器：一个 Web 工具，生成符合最佳实践的完整 Python 项目结构。用户可指定项目细节，工具输出包含源码、测试、文档和配置目录的 zip 文件，并预生成包含 models、services、controllers、utilities 和配置文件的样板代码。Python 代码质量仪表盘：一个集成 Ruff 做风格检查、pytest 做测试并包含 CI/CD 可视化的应用。它通过友好的仪表盘界面分析代码结构、风格和测试结果，让人了解 Python 项目的健康状况。自动环境配置管理器：一项管理并部署 Python 应用环境变量的服务。用户可安全地存储、更新和访问环境配置，这些配置会自动集成到开发和 CI/CD 工作流中。AI 辅助文档生成器：一个从 Python 代码自动生成详细文档的工具。它利用 docstring 和 AI 创建全面的 README 文件和内容丰富的文档，附有清晰的说明与示例，适合开发者和 AI 模型使用。Python 错误处理与日志框架：一个提供健壮错误处理工具的库，可捕获上下文并支持详细记录日志。它可以集成到任何项目中，增强错误管理和调试能力，让跨模块追踪问题更容易。虚拟环境依赖可视化器：一个 Web 应用，可视化由 uv 和虚拟环境管理的 Python 项目依赖树。它让开发者直观地理解依赖关系和潜在冲突，助力更高效的依赖管理。CI/CD 模板仓库：一个 GitHub 仓库模板，包含为 GitHub Actions 或 GitLab CI 预配置的 YAML 文件。该服务帮助开箱即用地搭建持续集成与部署流水线。AI 驱动的代码评审助手：一个集成到 GitHub 或 GitLab 的工具，用 AI 就代码质量、风格指南遵循情况、类型标注和描述性命名给出反馈。它帮助团队维持高代码标准，减少代码评审中的人工工作量。全面的日志与错误监控工具：一项类似 Sentry 或 LogRocket、但专注于 Python 应用的服务。它提供实时错误跟踪、上下文捕获和异常的详细洞察，并给出修复建议。Python 模块化设计模板库：一套现成模板的集合，涵盖 Python 中常见的模块化设计模式，包括 MVC 架构、工具类组织等，可作为希望实现健壮项目结构的开发者的快速入门库。

## 优势（Benefits）


## 简介（Synopsis）
开发者可以使用本提示词构建结构良好、可维护的 Python 应用，具备健壮的 CI/CD、测试和对 AI 友好的编码习惯。

## .cursorrules 提示文件概述（Overview of .cursorrules prompt）
.cursorrules 文件定义了一个专精 Python 开发的 AI 助手的行为。它旨在指导开发者用清晰的结构组织项目：源码、测试、文档和配置各自使用独立目录。它通过为 models、services 等不同组件设置独立文件来推动模块化设计，并强调通过环境变量进行配置管理。该助手主张强有力的错误处理、用 pytest 做全面测试以及详尽的文档。它鼓励使用 uv（首选）和虚拟环境管理依赖，同时用 Ruff 保证代码风格一致。此外，它支持使用 GitHub Actions 或 GitLab CI 实现 CI/CD。该助手旨在提供对 AI 友好的编码习惯：描述性命名、类型标注、详细注释和丰富的错误上下文。代码片段与讲解均围绕这些原则定制，以清晰为先，并利用 AI 完成开发任务。
