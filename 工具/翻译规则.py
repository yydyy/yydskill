# -*- coding: utf-8 -*-
"""
把 03-技术栈参考/原规则/rules 下相关包的 .mdc 规则中文化。

原则：
  * 只替换 frontmatter 的 description 和正文；
  * globs 从原文件读取后原样写回，绝不手改（保证 Cursor 文件匹配不变）；
  * 代码标识符、路径、库名、配置项保持英文原样（改写会让规则失效）。

用法：python 工具/翻译规则.py            # 预演
      python 工具/翻译规则.py --apply    # 写入
"""
import os, re, io, sys, json, argparse

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
ROOT = r"D:\Documents\AI技能库"
RULES = os.path.join(ROOT, "03-技术栈参考", "原规则", "规则包")
sys.path.insert(0, os.path.join(ROOT, "工具"))
from 包路径 import MAP as _PKGMAP, pkg_dir as _pkg_dir


def P(pkg):
    """英文包名 -> 改名后的绝对路径"""
    return _pkg_dir(pkg)

T = {
"python-fastapi-cursorrules-prompt-file": {
 "fastapi-best-practices.mdc": (
  "对 app 目录下的应用代码强制执行 FastAPI 最佳实践，包括数据校验、依赖注入与异步操作。",
  """- 用 Pydantic 模型定义请求与响应的 schema
- 对共享资源使用依赖注入
- 用 async/await 处理非阻塞操作
- 用路径操作装饰器定义接口（@app.get、@app.post 等）
- 用 HTTPException 做规范的错误处理
- 使用 FastAPI 内置的 OpenAPI 与 JSON Schema 支持"""),
 "fastapi-folder-structure.mdc": (
  "规定 FastAPI 项目的推荐目录结构，在 app 目录内保持组织清晰与关注点分离。",
  """- 遵循以下目录结构：

app/
  main.py         # 应用入口
  models/         # 数据模型
  schemas/        # 请求/响应 schema
  routers/        # 路由
  dependencies/   # 依赖
  services/       # 业务逻辑
  tests/          # 测试"""),
 "fastapi-main-application-file.mdc": (
  "规定 FastAPI 项目主应用文件的写法，重点是应用初始化与配置。",
  """- 用 FastAPI() 正确完成应用初始化
- 配置中间件与异常处理器
- 用路径操作装饰器定义 API 路由"""),
 "pydantic-models.mdc": (
  "规定 FastAPI 项目 models 目录下 Pydantic 模型的定义方式，确保数据校验与序列化。",
  """- 用 Pydantic 模型定义请求与响应的 schema
- 用 Pydantic 字段声明数据类型
- 用 Pydantic 校验器实现校验逻辑"""),
 "python-general-coding-standards.mdc": (
  "适用于通用 Python 编码规范：类型标注、用 Pydantic 做输入校验、后台任务、CORS 处理、安全工具、PEP 8 合规与完整测试。",
  """- 所有函数参数与返回值都加类型标注
- 用 Pydantic 做规范的输入校验
- 耗时操作使用 FastAPI 的后台任务
- 正确配置 CORS
- 认证使用 FastAPI 的安全工具
- 遵循 PEP 8 代码风格
- 编写完整的单元测试与集成测试"""),
},
"python-cursorrules-prompt-file-best-practices": {
 "ai-friendly-coding-practices.mdc": (
  "优化代码片段与讲解，使其清晰且适合 AI 辅助开发。",
  """- 代码片段与讲解都应围绕这些原则展开，以清晰度和 AI 辅助开发为优化目标。"""),
 "ci-cd-implementation-rule.mdc": (
  "用 GitHub Actions 或 GitLab CI 实现 CI/CD。",
  """- 用 GitHub Actions 或 GitLab CI 实现 CI/CD。"""),
 "configuration-management-rule.mdc": (
  "用环境变量管理配置。",
  """- 用环境变量管理配置。"""),
 "error-handling-and-logging-rule.mdc": (
  "实现健壮的错误处理与日志，包含上下文捕获。",
  """- 健壮的错误处理与日志记录，并捕获上下文信息。"""),
 "modular-design-rule.mdc": (
  "推行模块化设计：models、services、controllers、utilities 各自独立成文件。",
  """- 模块化设计：models、services、controllers、utilities 分别放在各自独立的文件中。"""),
 "project-structure-rule.mdc": (
  "要求清晰的项目结构，源码、测试、文档、配置各自独立目录。",
  """- 强调清晰的项目结构：源码、测试、文档、配置分别放在独立目录中。"""),
 "python-general-rules.mdc": (
  "通用 Python 开发规范：类型标注、docstring、依赖管理、用 pytest 测试，以及用 Ruff 统一代码风格。",
  """- 任何 Python 文件，都必须为每个函数或类加上类型标注，必要时补上返回类型。
- 同时为所有 Python 函数和类添加说明性 docstring，遵循 pep257 约定；已有 docstring 需要时一并更新。
- 文件中现有的注释必须保留。
- 写测试时只用 pytest 或 pytest 插件，不要用 unittest 模块。
- 所有测试同样要加类型标注。
- 所有测试都放在 ./tests 下，所需文件与目录要建全。在 ./tests 或 ./src/goob_ai 里新建文件时，若不存在 __init__.py 要先创建。
- 所有测试都要有完整标注并包含 docstring。
- 在 TYPE_CHECKING 分支下需要导入以下内容：
  from _pytest.capture import CaptureFixture
  from _pytest.fixtures import FixtureRequest
  from _pytest.logging import LogCaptureFixture
  from _pytest.monkeypatch import MonkeyPatch
  from pytest_mock.plugin import MockerFixture
- 依赖管理使用 https://github.com/astral-sh/uv 配合虚拟环境。
- 用 Ruff 保持代码风格一致。"""),
},
"python-developer-cursorrules-prompt-file": {
 "dependencies-management-rules.mdc": (
  "强制安装依赖时使用 UV，以保证各环境的一致性与效率。",
  """- 安装依赖一律使用 UV"""),
 "general-python-development.mdc": (
  "设定 Python 开发者的角色定位，专长于 Python、命令行工具与文件系统操作。",
  """你是一位资深软件开发者，精通 Python、命令行工具与文件系统操作。你在调试复杂问题和优化代码性能方面功底深厚，是本项目不可或缺的力量。"""),
 "project-technology-stack-context.mdc": (
  "概述项目所用技术，便于理解运行环境。",
  """本项目使用以下技术：

（原文此处未填写具体技术清单，请按项目实际补充。）"""),
 "python-code-style.mdc": (
  "要求所有 Python 代码用类而不是函数来写。",
  """- 一律使用类，而不是函数"""),
 "python-version.mdc": (
  "规定项目所有 Python 代码一律使用 Python 3.12。",
  """- 一律使用 Python 3.12"""),
},
"python-projects-guide-cursorrules-prompt-file": {
 "python-ai-friendly-coding-practices-rule.mdc": (
  "在 Python 文件中推行 AI 友好的编码习惯：命名有描述性、加类型标注、关键逻辑写详细注释、错误带丰富上下文。",
  """- 变量与函数命名要有描述性
- 使用类型标注
- 复杂逻辑写详细注释
- 错误信息提供丰富的上下文，便于调试"""),
 "python-ci-cd-implementation-rule.mdc": (
  "用 GitHub Actions 或 GitLab CI 实现 CI/CD 流水线，完成自动构建、测试与部署。",
  """- 用 GitHub Actions 或 GitLab CI 实现 CI/CD。"""),
 "python-code-style-consistency-rule.mdc": (
  "用 Ruff 保证 Python 文件的代码风格一致，维持整洁统一的代码库。",
  """- 用 Ruff 强制保证代码风格一致。"""),
 "python-configuration-management-rule.mdc": (
  "在 config 目录内用环境变量管理配置，使应用设置灵活易维护。",
  """- 用环境变量管理配置。"""),
 "python-dependency-management-rule.mdc": (
  "指定用 uv（首选）管理依赖与虚拟环境，保证依赖一致且相互隔离。",
  """- 依赖管理使用 https://github.com/astral-sh/uv 配合虚拟环境。"""),
 "python-documentation-rule.mdc": (
  "在 Python 文件中用 docstring 与 README 提供详细文档，提升代码可理解性与可维护性。",
  """- 用 docstring 与 README 文件提供详细文档。"""),
 "python-error-handling-and-logging-rule.mdc": (
  "强调 Python 文件中健壮的错误处理与日志实践，包含上下文捕获以便调试。",
  """- 实现健壮的错误处理与日志记录，并捕获上下文信息。"""),
 "python-modular-design-rule.mdc": (
  "在 src 目录内推行模块化设计：models、services、controllers、utilities 各自独立成文件。",
  """- 模块化设计：models、services、controllers、utilities 分别放在各自独立的文件中。"""),
 "python-project-structure-rule.mdc": (
  "要求所有 Python 项目结构清晰：源码、测试、文档、配置各自独立目录。",
  """- 保持清晰的项目结构：源码（src）、测试（tests）、文档（docs）、配置（config）分别独立成目录。"""),
 "python-testing-with-pytest-rule.mdc": (
  "规定在 tests 目录内用 pytest 做完整测试，保证代码可靠与质量。",
  """- 用 pytest 做完整测试。"""),
},
"python-llm-ml-workflow-cursorrules-prompt-file": {
 "asynchronous-programming-preference.mdc": (
  "异步编程优先使用 async 与 await。",
  """- **异步编程：** 优先使用 `async` 与 `await`"""),
 "code-formatting-with-ruff.mdc": (
  "用 Ruff 统一代码格式，取代 Black、isort、flake8。",
  """- **代码格式化：** Ruff（取代 `black`、`isort`、`flake8`）"""),
 "comprehensive-type-annotations.mdc": (
  "要求所有 Python 函数、方法与类成员都有完整类型标注。",
  """- **完整类型标注：** 所有函数、方法与类成员都必须有类型标注，并尽量使用最具体的类型。"""),
 "comprehensive-unit-testing-with-pytest.mdc": (
  "用 pytest 追求高测试覆盖率，常见场景与边界场景都要覆盖。",
  """- **充分单元测试：** 用 `pytest` 追求高覆盖率（90% 以上），常见场景和边界场景都要测。"""),
 "data-pipeline-management-with-dvc.mdc": (
  "用脚本或 dvc 之类的工具管理数据预处理，保证可复现。",
  """- **数据流水线管理：** 用脚本或 `dvc` 之类的工具管理数据预处理，保证可复现。"""),
 "data-validation-with-pydantic.mdc": (
  "FastAPI 应用用 Pydantic 模型对请求与响应数据做严格校验。",
  """- **数据校验：** 用 Pydantic 模型对请求与响应数据做严格校验。"""),
 "detailed-docstrings.mdc": (
  "要求所有函数、方法与类都有详细的 Google 风格 docstring。",
  """- **详细 docstring：** 所有函数、方法与类都必须有 Google 风格 docstring，完整说明用途、参数、返回值以及可能抛出的异常；有必要时附用法示例。"""),
 "experiment-configuration-with-hydra-yaml.mdc": (
  "建议用 Hydra 或 YAML 管理实验配置，保证清晰可复现。",
  """- **实验配置：** 用 `hydra` 或 `yaml` 管理实验配置，保证清晰可复现。"""),
 "fastapi-web-framework.mdc": (
  "指定 FastAPI 作为 API 开发的 Web 框架。",
  """- **Web 框架：** `fastapi`"""),
 "google-style-docstrings.mdc": (
  "要求所有 Python 函数、方法与类使用 Google 风格 docstring。",
  """- **文档：** Google 风格 docstring"""),
 "llm-prompt-engineering.mdc": (
  "为 LLM 应用单独划出模块或文件管理 Prompt 模板，并纳入版本控制。",
  """- **LLM Prompt 工程：** 单独划出模块或文件管理 Prompt 模板，并纳入版本控制。"""),
 "logging-module-usage.mdc": (
  "恰当使用 logging 模块记录重要事件、警告与错误。",
  """- **日志：** 恰当使用 `logging` 模块记录重要事件、警告与错误。"""),
 "prioritize-python-3-10-features.mdc": (
  "优先使用 Python 3.10 及之后版本的新特性。",
  """- **优先使用 Python 3.10+ 的新特性**。"""),
 "python-general-role-definition.mdc": (
  "把 AI 的角色定义为 Python 大师、导师、机器学习工程师与数据科学家，强调代码质量与讲解清晰。",
  """- 你是 **Python 大师**、经验丰富的 **导师**、**世界级机器学习工程师**，同时也是 **出色的数据科学家**。
- 你具备极强的编码能力，深刻理解 Python 的最佳实践、设计模式与惯用法。
- 你擅长识别并预防潜在错误，把写出高效、可维护的代码放在首位。
- 你善于用清晰简洁的方式讲解复杂概念，是有效率的导师与教育者。
- 你在机器学习领域有公认的贡献，有成体系地开发并上线成功 ML 模型的记录。
- 作为出色的数据科学家，你擅长数据分析、可视化，并能从复杂数据集中提炼可落地的结论。"""),
 "testing-framework-pytest.mdc": (
  "指定 pytest 作为 Python 项目的测试框架。",
  """- **测试框架：** `pytest`"""),
 "type-hinting-rule.mdc": (
  "强制所有 Python 函数、方法与类成员用 typing 模块做严格类型标注。",
  """- **类型标注：** 严格使用 `typing` 模块；所有函数、方法与类成员都必须有类型标注。"""),
 "uv-dependency-management.mdc": (
  "指定用 uv（首选）或 Poetry 管理 Python 项目的依赖。",
  """- **依赖管理：** uv（首选）/ Poetry"""),
},
"typescript-code-convention-cursorrules-prompt-file": {
 "expo-mobile-app-rule.mdc": (
  "规定基于 Expo 的移动应用开发的最佳实践与约定。",
  """- 你是 Expo 专家。
- 遵循 Expo 官方文档的最佳实践。"""),
 "general-project-rule.mdc": (
  "适用于所有文件类型的通用项目规则，最为宽泛。",
  """- 命名约定：遵循清晰一致的命名约定。
- 性能优化：针对性能优化代码。
- 关键约定：遵守项目自身的特定约定。
- 错误处理与校验：实现完整的错误处理与校验。"""),
 "general-typescript-rule.mdc": (
  "把通用 TypeScript 最佳实践与风格指南应用到项目所有 TypeScript 文件。",
  """- 你是 TypeScript 专家。
- TypeScript 用法：遵循 TypeScript 最佳实践，保证类型安全与代码可维护性。
- 语法与格式：遵循统一的 TypeScript 代码风格与格式规范。"""),
 "next-js-app-router-rule.mdc": (
  "把 Next.js App Router 相关规范应用到 app 目录下的组件与页面。",
  """- 你是 Next.js App Router 专家。
- 数据获取、渲染与路由方面遵循 Next.js 官方文档的最佳实践。"""),
 "node-js-backend-rule.mdc": (
  "在后端 server 目录内强制 Node.js 相关约定与实践。",
  """- 你是 Node.js 专家。
- 代码风格与结构：遵循 Node.js 约定组织后端代码。
- 错误处理与校验：在 Node.js 中实现健壮的错误处理与校验。"""),
 "radix-ui-rule.mdc": (
  "Radix UI 组件专用的样式与约定。",
  """- 你是 Radix UI 专家。"""),
 "react-component-rule.mdc": (
  "定义项目内 React 组件的代码风格与最佳实践。",
  """- 你是 React 专家。
- 代码风格与结构：保持 React 组件结构一致。
- 语法与格式：遵循统一的 React 代码风格与格式规范。"""),
 "shadcn-ui-rule.mdc": (
  "应用 Shadcn UI 组件相关的样式与约定。",
  """- 你是 Shadcn UI 专家。"""),
 "tailwind-css-styling-rule.mdc": (
  "在所有相关文件中应用 Tailwind CSS 样式约定。",
  """- 你是 Tailwind 专家。
- UI 与样式：用 Tailwind CSS 保持 UI 样式一致。"""),
 "trpc-api-rule.mdc": (
  "对 tRPC 的 API 端点与 procedure 强制相关约定与实践。",
  """- 你是 tRPC 专家。"""),
},
"typescript-llm-tech-stack-cursorrules-prompt-file": {
 "code-style.mdc": (
  "规定 TypeScript 文件的代码风格，重点是变量声明、函数用法与类型系统运用。",
  """- 变量不会被重新赋值时优先用 `const` 而不是 `let`
- 用箭头函数获得更好的词法作用域与更简洁的语法
- 充分利用 TypeScript 类型系统：恰当使用 interface、type 别名与泛型
- 用自定义错误类型实现错误处理
- 尽量写纯函数，提升可测试性并减少副作用"""),
 "documentation.mdc": (
  "要求使用 JSDoc 注释并保持 README 最新，确保项目文档完整。",
  """- 函数、类与复杂类型使用 JSDoc 注释
- 文档中适当加入示例
- README 保持最新，包含安装说明、用法示例与贡献指南"""),
 "file-organization.mdc": (
  "定义 TypeScript 项目的文件组织方式，强调模块化与关注点分离。",
  """- 相关功能归到同一模块
- 用 index 文件简化导入
- 分离关注点：业务逻辑、UI 组件与工具函数放在不同目录"""),
 "general-typescript-project-rules.mdc": (
  "把通用编码标准与最佳实践应用到项目所有 TypeScript 文件，重点是命名约定、文件组织与代码风格。",
  """- 你是资深软件工程师兼产品经理。
- 精通函数式编程，尤其是 TypeScript。
- 深刻理解 TypeScript 及其生态。
- 擅长打造让开发者用得舒服的代码库 API。
- 提倡可组合、不可变与务实的简单方案。
- 能不用类就不用类，优先用函数。
- 能不用 interface 就不用 interface，优先用 type。
- 遵循单一职责原则
- 用依赖注入提升可测试性与灵活性
- 实现规范的错误处理与日志
- 为所有业务逻辑写完整的单元测试
- 异步操作使用 async/await，不要用回调或裸 Promise
- 启用 TypeScript strict 模式以获得更强的类型检查"""),
 "library-usage.mdc": (
  "给出项目中特定库的有效使用指南，包括 axios、js-yaml、mime-types、node-gyp、uuid 与 zod。",
  """- 有效使用以下库：
  - axios (^1.7.5)：用于 HTTP 请求，用拦截器统一处理全局错误与认证
  - js-yaml (^4.1.0)：用于解析与序列化 YAML，使用类型安全的 schema
  - mime-types (^2.1.35)：用于 MIME 类型识别与文件扩展名映射
  - node-gyp (^10.2.0)：原生插件构建工具，确保构建流水线中配置正确
  - uuid (^10.0.0)：用于生成唯一标识，随机 UUID 优先用 v4
  - zod (^3.23.8)：用于运行时类型检查与数据校验，把 schema 写成可复用的"""),
 "naming-conventions.mdc": (
  "在所有 TypeScript 文件中强制统一的命名约定，保持一致性与可读性。",
  """- 文件名用 kebab-case（如 `my-component.ts`）
- 变量与函数名用 camelCase（如 `myVariable`、`myFunction()`）
- 类、类型与接口用 UpperCamelCase（PascalCase）（如 `MyClass`、`MyInterface`）
- 常量与枚举值用全大写加下划线（如 `MAX_COUNT`、`Color.RED`）"""),
},
"typescript-nestjs-best-practices-cursorrules-promp": {
 "nestjs-core-module-guidelines.mdc": (
  "NestJS 核心模块的专门规范，重点是全局过滤器、中间件、守卫与拦截器。",
  """- 全局过滤器负责异常处理。
- 全局中间件负责请求管理。
- 守卫负责权限管理。
- 拦截器负责请求处理。"""),
 "nestjs-general-guidelines.mdc": (
  "规定 NestJS 的架构原则、模块化设计与测试实践，作用于 src 目录。",
  """- 使用模块化架构
- 把 API 封装进模块。
  - 每个主要领域/路由一个模块。
  - 该路由一个 controller。
  - 次级路由用另外的 controller。
  - 一个 models 目录存放数据类型。
  - 输入用 class-validator 校验的 DTO。
  - 输出声明简单类型。
  - 一个 services 模块承载业务逻辑与持久化。
  - 每个实体一个 service。
- 一个 core 模块放 Nest 相关构件
  - 全局过滤器负责异常处理。
  - 全局中间件负责请求管理。
  - 守卫负责权限管理。
  - 拦截器负责请求处理。
- 一个 shared 模块放模块间共享的服务。
  - 工具函数
  - 共享业务逻辑
- 测试使用标准的 Jest 框架。
- 为每个 controller 与 service 写测试。
- 为每个 api 模块写端到端测试。
- 为每个 controller 加一个 admin/test 方法作为冒烟测试。"""),
 "nestjs-module-structure-guidelines.mdc": (
  "规定 NestJS 模块内部的结构与组成，包括 controller、models、DTO 与 service，确保 API 封装一致。",
  """- 每个主要领域/路由一个模块。
- 该路由一个 controller。
- 次级路由用另外的 controller。
- 一个 models 目录存放数据类型。
- 输入用 class-validator 校验的 DTO。
- 输出声明简单类型。
- 一个 services 模块承载业务逻辑与持久化。
- 每个实体一个 service。"""),
 "nestjs-shared-module-guidelines.mdc": (
  "定义 NestJS shared 模块的标准，强调跨模块可访问的工具函数与共享业务逻辑。",
  """- 工具函数
- 共享业务逻辑"""),
 "nestjs-testing-guidelines.mdc": (
  "规定 NestJS 应用的测试标准，包括单元测试、集成测试与端到端测试，以及 Jest 的使用。",
  """- 测试使用标准的 Jest 框架。
- 为每个 controller 与 service 写测试。
- 为每个 api 模块写端到端测试。
- 为每个 controller 加一个 admin/test 方法作为冒烟测试。"""),
 "typescript-general-guidelines.mdc": (
  "把通用 TypeScript 编码标准应用到整个项目，包括命名约定、函数结构、数据处理与异常处理。",
  """- 所有代码与文档使用英文。
- 每个变量和函数（参数与返回值）都声明类型。
- 避免使用 any。
- 按需创建类型。
- 用 JSDoc 记录公开的类与方法。
- 函数内部不留空行。
- 一个文件一个导出。
- 类名用 PascalCase。
- 变量、函数与方法名用 camelCase。
- 文件与目录名用 kebab-case。
- 环境变量用全大写。
- 避免魔法数字，改为定义常量。
- 每个函数以动词开头。
- 布尔变量用动词，例如 isLoading、hasError、canDelete 等。
- 用完整单词而不是缩写，并注意拼写正确。
  - 标准缩写除外，如 API、URL 等。
  - 公认的简写除外：
    - 循环用 i、j
    - 错误用 err
    - 上下文用 ctx
    - 中间件函数参数用 req、res、next
- 函数写短，单一职责，指令数少于 20 条。
- 函数名用动词加宾语。
- 返回布尔值的用 isX 或 hasX、canX 等。
- 没有返回值的用 executeX 或 saveX 等。
- 通过以下方式避免嵌套代码块：
  - 提前检查并返回。
  - 抽取成工具函数。
- 用高阶函数（map、filter、reduce 等）避免函数嵌套。
- 简单函数（少于 3 条指令）用箭头函数。
- 非简单函数用具名函数。
- 用默认参数值，而不是判断 null 或 undefined。
- 用 RO-RO 模式减少函数参数
  - 用对象传多个参数。
  - 用对象返回结果。
  - 为入参与出参声明必要的类型。
- 保持单一抽象层级。
- 不要滥用原始类型，把数据封装进复合类型。
- 避免在函数里做数据校验，改用带内部校验的类。
- 数据优先保持不可变。
- 不会变的数据用 readonly。
- 不会变的字面量用 as const。
- 遵循 SOLID 原则。
- 优先组合而不是继承。
- 用 interface 声明契约。
- 类写小、单一职责。
  - 指令数少于 200 条。
  - 公开方法少于 10 个。
  - 属性少于 10 个。
- 用异常处理预期之外的错误。
- 捕获异常应当是为了：
  - 修掉一个可预期的问题。
  - 补充上下文。
  - 否则交给全局处理器。
- 测试遵循 Arrange-Act-Assert 约定。
- 测试变量命名清晰。
- 遵循命名约定：inputX、mockX、actualX、expectedX 等。
- 为每个公开函数写单元测试。
- 用测试替身模拟依赖。
  - 执行成本不高的第三方依赖除外。
- 为每个模块写验收测试。
- 遵循 Given-When-Then 约定。"""),
},
"typescript-nodejs-nextjs-react-ui-css-cursorrules-": {
 "general-typescript-node-js-next-js-app-router-react-rule.mdc": (
  "把通用 TypeScript、Node.js、Next.js 与 React 最佳实践应用到整个项目，重点是代码风格、结构、TypeScript 用法、语法、UI 与性能优化。",
  """- 你是 TypeScript、Node.js、Next.js App Router、React、Shadcn UI、Radix UI 与 Tailwind 专家。

代码风格与结构
- 写简洁、技术化的 TypeScript 代码，示例要准确。
- 使用函数式与声明式编程范式；避免使用类。
- 优先迭代与模块化，而不是复制代码。
- 变量命名要有描述性并带助动词（如 isLoading、hasError）。
- 文件结构：导出组件、子组件、辅助函数、静态内容、类型。

命名约定
- 目录用小写加连字符（如 components/auth-wizard）。
- 组件优先使用具名导出。

TypeScript 用法
- 所有代码使用 TypeScript；优先用 interface 而不是 type。
- 避免 enum，改用 map。
- 函数式组件配合 TypeScript interface。

语法与格式
- 纯函数使用 "function" 关键字。
- 条件语句中省略不必要的花括号；简单语句用简洁写法。
- 使用声明式 JSX。

UI 与样式
- 组件与样式使用 Shadcn UI、Radix 与 Tailwind。
- 用 Tailwind CSS 实现响应式设计，采用移动优先。

性能优化
- 尽量少用 'use client'、'useEffect' 与 'setState'；优先 React Server Components（RSC）。
- 客户端组件用 Suspense 包裹并提供 fallback。
- 非关键组件使用动态加载。
- 图片优化：使用 WebP 格式、带上尺寸信息、实现懒加载。

关键约定
- 用 'nuqs' 管理 URL 查询参数状态。
- 优化 Web Vitals（LCP、CLS、FID）。
- 限制 'use client'：
  - 优先服务端组件与 Next.js SSR。
  - 仅在小体量组件访问 Web API 时使用。
  - 数据获取或状态管理不要用它。

数据获取、渲染与路由遵循 Next.js 官方文档。"""),
 "next-js-app-router-optimization-rule.mdc": (
  "专门作用于 Next.js App Router 目录，重点是性能优化、减少客户端渲染，并遵循 Next.js 文档处理数据获取、渲染与路由。",
  """- 尽量少用 'use client'、'useEffect' 与 'setState'；优先 React Server Components（RSC）。
- 客户端组件用 Suspense 包裹并提供 fallback。
- 非关键组件使用动态加载。
- 图片优化：使用 WebP 格式、带上尺寸信息、实现懒加载。
- 用 'nuqs' 管理 URL 查询参数状态。
- 优化 Web Vitals（LCP、CLS、FID）。
- 限制 'use client'：
  - 优先服务端组件与 Next.js SSR。
  - 仅在小体量组件访问 Web API 时使用。
  - 数据获取或状态管理不要用它。
- 数据获取、渲染与路由遵循 Next.js 官方文档。"""),
 "typescript-usage-rule.mdc": (
  "强制具体的 TypeScript 编码实践，包括优先 interface 而非 type、用 map 取代 enum，作用于项目所有 TypeScript 文件。",
  """- 所有代码使用 TypeScript；优先用 interface 而不是 type。
- 避免 enum，改用 map。
- 函数式组件配合 TypeScript interface。"""),
 "ui-component-styling-rule.mdc": (
  "聚焦用 Shadcn UI、Radix UI 与 Tailwind CSS 做样式与 UI 组件结构，强调响应式设计与移动优先。",
  """- 你是 Shadcn UI、Radix UI 与 Tailwind 专家。
- 组件与样式使用 Shadcn UI、Radix 与 Tailwind。
- 用 Tailwind CSS 实现响应式设计，采用移动优先。"""),
},
"python-fastapi-scalable-api-cursorrules-prompt-fil": {
 "backend-performance-optimization.mdc": (
  "聚焦 Python 后端的性能优化手法。",
  """- 用 async 函数减少阻塞式 I/O 操作。
- 对频繁访问的数据使用 Redis 或内存存储实现缓存策略。
- 大数据集与 API 响应用懒加载。"""),
 "docker-configuration.mdc": (
  "关于项目中 Docker 使用的规则。",
  """- 用 Docker 容器化，保证部署简单。
- 开发与生产环境都用 Docker 与 docker compose 做编排；不要再用已废弃的 `docker-compose` 命令。"""),
 "fastapi-backend-conventions.mdc": (
  "定义后端使用 FastAPI 的专门约定。",
  """- 遵循 RESTful API 设计原则。
- 用 FastAPI 的依赖注入系统管理状态与共享资源。
- 如适用，用 SQLAlchemy 2.0 提供 ORM 能力。
- 本地开发环境要正确配置 CORS。
- 用户访问平台不需要认证或授权。"""),
 "frontend-performance-optimization.mdc": (
  "聚焦 TypeScript 前端的性能优化手法。",
  """- 优先服务端渲染，尽量避免沉重的客户端渲染。
- 非关键组件使用动态加载；图片加载优化使用 WebP 格式并配合懒加载。"""),
 "general-python-backend-rules.mdc": (
  "适用于后端 Python 代码的通用编码风格与结构规则。",
  """- 精通 Python、FastAPI 与可扩展 API 开发。
- 用 Python 写简洁、技术化的回答，示例要准确。
- 使用函数式与声明式编程范式；除非绝对必要，避免使用类。
- 优先迭代与模块化，而不是复制代码。
- 变量命名要有描述性并带助动词（如 `is_active`、`has_permission`）。
- 遵循命名约定：小写加下划线（如 `routers/user_routes.py`）。
- 纯函数用 `def`，异步操作使用 `async def`。
- 所有函数签名都加 Python 类型标注；输入校验优先用 Pydantic 模型。
- 目录清晰分离：routes、utilities、静态内容、models/schemas。
- 使用「接收对象、返回对象」模式。
- 在函数开头用提前返回处理错误。
- 使用守卫子句，避免深层嵌套的 if 语句。
- 实现规范的日志与自定义错误类型。"""),
 "general-typescript-frontend-rules.mdc": (
  "适用于前端 TypeScript 代码的通用编码风格与结构规则。",
  """- 精通 TypeScript、React、Tailwind 与 Shadcn UI。
- 用 TypeScript 写简洁、技术化的回答，示例要准确。
- 使用函数式与声明式编程范式；除非绝对必要，避免使用类。
- 优先迭代与模块化，而不是复制代码。
- 变量命名要有描述性并带助动词（如 `isLoading`、`hasError`）。
- 遵循命名约定：目录用小写加连字符（如 `components/auth-wizard`）。
- 所有代码使用 TypeScript。优先用 interface 而不是 type。避免 enum，改用 map。
- 所有组件都写成带完整 TypeScript interface 的函数式组件。
- 用 Tailwind CSS 配合 Shadcn UI 实现响应式设计，采用移动优先。"""),
 "react-frontend-conventions.mdc": (
  "定义 React 前端开发的约定与优化要点。",
  """- 优化 Web Vitals（LCP、CLS、FID）。
- `use client` 只在访问 Web API 的小体量组件里使用。"""),
},
}

ap = argparse.ArgumentParser()
ap.add_argument("--apply", action="store_true")
args = ap.parse_args()

FIELD = re.compile(r"^---\s*\n(.*?)\n---\s*\n?", re.S)
n_done, n_missing, skipped = 0, [], []
for pkg, files in T.items():
    d = P(pkg)
    if not os.path.isdir(d):
        n_missing.append((pkg, "包不存在"))
        continue
    for fn, (desc, body) in files.items():
        src = os.path.join(d, fn)
        if not os.path.exists(src):
            n_missing.append((pkg, fn))
            continue
        raw = open(src, encoding="utf-8", errors="replace").read()
        m = FIELD.match(raw)
        if not m:
            n_missing.append((pkg, fn + " (无 frontmatter)"))
            continue
        fm = m.group(1)
        gm = re.search(r"^globs:\s*(.+)$", fm, re.M)
        globs = gm.group(1).strip() if gm else "*"
        new = f"---\ndescription: {desc}\nglobs: {globs}\n---\n{body}\n"
        changed = new != raw
        print(("[改写] " if changed else "[同文] ") + f"{pkg}/{fn}   globs={globs}")
        if args.apply and changed:
            open(src, "w", encoding="utf-8").write(new)
        n_done += 1

print()
print("=" * 90)
print(f"计划处理 {n_done} 个 .mdc 文件，涉及 {len(T)} 个包")
if n_missing:
    print("异常：")
    for a, b in n_missing:
        print("   ", a, b)
print("模式：", "已写入" if args.apply else "预演（加 --apply 才写入）")
