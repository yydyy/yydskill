# Python FastAPI 最佳实践 .cursorrules 提示文件（Python FastAPI Best Practices .cursorrules prompt file）

作者：Caio Barbieri

## 可以构建什么（What You Can Build）
可扩展 API 开发平台：构建一个云平台，简化用 Python 和 FastAPI 开发可扩展 API 的过程。它应包含用于搭建 API 路由、用 Pydantic 做输入校验、用中间件做错误处理以及性能监控的模板和模块。异步数据处理库：创建一个专注于异步数据处理任务的 Python 库，利用 FastAPI 的异步能力。该库包含处理异步数据库操作的工具、与 asyncpg 等异步库的集成，以及缓存机制。API 性能分析器：开发一个分析 FastAPI 应用性能瓶颈的工具。它应聚焦响应时间、延迟和吞吐量指标，给出优化异步流程、减少阻塞操作的建议。Pydantic 校验工具包：提供一个增强 Pydantic 校验功能的工具包，具备先进的错误处理和日志能力。该工具包可包含自定义错误类型的插件和面向复杂数据结构的校验 schema。FastAPI 中间件扩展：创建一组 FastAPI 中间件扩展，聚焦日志记录、错误监控和性能优化。它们包含管理启动/关闭事件、HTTP 错误响应和性能指标的工具。API 错误处理框架：设计一个标准化 FastAPI 应用错误处理的框架。该框架应提供一致的错误信息、日志策略和错误监控，运用自定义错误类型和工厂。懒加载数据服务：构建一个便于在 FastAPI 应用中对大型数据集进行懒加载的服务。它可包含管理分页响应和按需取数策略的 API 与工具。数据库交互 ORM：开发一个轻量 ORM，基于 SQLAlchemy 2.0 针对 FastAPI 中的异步数据库交互进行优化，重点减少阻塞操作并缓存频繁访问的数据。声明式路由构建器：提供一个用声明式语法构建 FastAPI 路由的工具，强调类型安全、清晰的返回类型标注和模块化组件。它可以简化路由定义、增强可维护性。API 缓存系统：为 FastAPI API 实现一套量身定制的缓存系统，使用 Redis 或内存存储等工具高效管理可缓存的响应和静态内容，提升性能、降低延迟。

## 优势（Benefits）


## 简介（Synopsis）
使用 FastAPI 创建可扩展 API 的开发者将从本提示词中受益，用 Python 和现代异步技术设计高性能、模块化、可维护的服务。

## .cursorrules 提示文件概述（Overview of .cursorrules prompt）
.cursorrules 文件概述了 Python 和 FastAPI 开发的最佳实践与准则，强调可扩展的 API 解决方案。它涵盖函数式与声明式编程、错误处理和性能优化等原则。它推荐简洁准确的 Python 示例、类型标注、用于校验的 Pydantic 模型以及异步操作。鼓励开发者使用 FastAPI 的依赖注入和中间件来提升性能与可维护性，重点高效管理启动与关闭过程并采用缓存策略。该文件把可读性、模块化和错误日志放在优先位置，同时利用 Pydantic 模型等 FastAPI 特有功能保证一致性。
