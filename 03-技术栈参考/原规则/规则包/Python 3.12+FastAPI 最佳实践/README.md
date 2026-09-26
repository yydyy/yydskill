# Python 3.12 FastAPI 最佳实践 .cursorrules 提示文件

作者：Raphael Mansuy

## 你可以构建什么
任务管理 API：使用 FastAPI 开发用于创建和管理任务的 API 服务。使用 pydantic 进行数据校验和序列化，使用 fastapi-users 进行用户管理，使用 fastapi-jwt-auth 实现安全的用户身份验证。该服务应处理 CRUD 操作，使用 fastapi-cache 实现缓存，使用 fastapi-limiter 实现限流，并使用 fastapi-pagination 高效地列出任务。电子商务平台后端：使用 FastAPI 构建电子商务平台后端，利用 sqlalchemy 作为 ORM，使用 pydantic 进行数据校验，并使用 FastAPI-users 管理用户账户和身份验证。使用 fastapi-mail 发送订单确认邮件，使用 fastapi-cache 缓存商品数据，并使用 fastapi-pagination 处理批量数据检索。博客平台：使用 FastAPI 创建博客平台后端，支持用户发布的博客文章。使用 fastapi-users 进行账户管理，使用 sqlalchemy 进行数据库事务处理，使用 fastapi-jwt-auth 进行用户身份验证。使用 fastapi-mail 实现邮件通知，并使用 fastapi-cache 缓存频繁访问的文章。在线课程平台：使用 FastAPI 设计在线课程管理后端，用于处理课程内容和学生选课。利用 pydantic 进行课程数据校验，使用 fastapi-users 进行用户身份验证，使用 fastapi-jwt-auth 进行令牌管理。使用 fastapi-mail 实现邮件通知，并利用 fastapi-pagination 管理大量课程和学生选课列表。招聘板 API：使用 FastAPI 为招聘板应用开发 API，重点关注职位列表和候选人申请。使用 fastapi-users 管理求职者和招聘者账户，使用 fastapi-jwt-auth 实现安全身份验证，使用 sqlalchemy 管理职位条目。使用 fastapi-mail 发送申请跟进和职位提醒，并使用 fastapi-pagination 高效列出职位。订阅服务：使用 FastAPI 构建订阅服务后端，支持用户订阅多种套餐。利用 fastapi-users 进行用户管理，使用 fastapi-jwt-auth 实现安全登录，使用 fastapi-mail 发送订阅通知和发票。使用 fastapi-limiter 防止滥用订阅变更，使用 fastapi-cache 快速检索订阅数据。社交网站后端：使用 FastAPI 创建社交网站后端。使用 pydantic 校验用户和帖子数据，使用 fastapi-users 处理用户资料和关系，使用 fastapi-jwt-auth 进行身份验证。使用 fastapi-cache 缓存热门帖子或用户数据，并使用 fastapi-pagination 实现搜索功能。活动管理系统：使用 FastAPI 开发用于管理活动的后端。使用 fastapi-users 和 fastapi-jwt-auth 实现用户注册和活动创建。使用 fastapi-mail 发送活动邀请和更新，并使用 fastapi-pagination 管理大量参与者或活动。利用 fastapi-cache 优化活动数据检索。食谱分享平台：使用 FastAPI 创建食谱分享平台后端，使用 pydantic 进行食谱数据校验。使用 fastapi-users 管理用户账户和食谱提交。利用 fastapi-mail 发送食谱分享通知，使用 fastapi-cache 存储热门食谱以便快速访问。使用 fastapi-pagination 浏览食谱。健身追踪应用 API：使用 FastAPI 为健身追踪应用构建 API。使用 pydantic 校验训练和营养数据，使用 fastapi-users 进行用户管理，使用 fastapi-jwt-auth 实现安全身份验证。使用 fastapi-mail 发送每周进度总结和成就。使用 fastapi-pagination 管理大量活动日志，使用 fastapi-cache 处理频繁访问的数据。

## 优势


## 简介
使用 FastAPI 构建 RESTful API 的开发者可以创建健壮、可扩展的应用程序，这得益于严格遵循 Python 3.12 以及在身份验证、缓存和分页等任务中使用现代库。

## .cursorrules 提示内容概述
.cursorrules 文件概述了使用 Python 3.12 及多个框架和工具开发 Python 应用的最佳实践和指南。它指定了使用 pydantic、fastapi、sqlalchemy 以及多种 fastapi 扩展来完成用户管理、身份验证、邮件发送、缓存、限流和分页等任务。依赖管理由 poetry 处理，并推荐使用 alembic 管理数据库迁移。文件还强调编码规范，如使用有意义的命名、遵循 PEP 8、使用 docstring、编写简单代码，以及运用列表推导式和 try-except 块。此外还建议使用虚拟环境、编写单元测试、利用类型提示，并避免全局变量，以确保产出干净、高效、可维护的代码。
