# 项目上下文管理的 Cursor Rules（Cursor Rules for Project Context Management）

作者：[@kryptobaseddev](https://github.com/kryptobaseddev)

## 概述

本仓库包含一个全面的 `.cursorrules` 文件，旨在使用 Cursor AI Agent 时增强项目管理和开发工作流。这些规则专门设计用于维护一致的项目上下文，并把开发任务拆分为可管理、可跟踪的单元。

## 核心概念

### ProjectDocs 结构

```
ProjectDocs/
├── Build_Notes/
│   ├── active/          # Current build notes
│   ├── completed/       # Finished build notes
│   └── archived/        # Deprecated build notes
└── contexts/
    ├── projectContext.md    # Master project context
    ├── appFlow.md          # Application flow documentation
    ├── authFlow.md         # Authentication flow documentation
    └── ...                 # Additional context files
```

### 关键特性

- **构建笔记管理**：系统化地跟踪开发进度
- **上下文感知**：维护项目上下文，减少 AI 幻觉
- **任务组织**：把复杂任务拆分为可管理的单元
- **进度跟踪**：清晰的任务完成监控体系
- **文档规范**：统一的格式与组织方式

## 技术标准

### 代码质量与风格
- 单个文件最多 150 行；超出则重构为更小的模块
- 函数式、声明式编程方式（避免 OOP 和类）
- 使用带辅助动词的语义化变量命名（如 `isLoading`、`hasError`）
- 目录和文件名使用小写加连字符
- DRY（Don't Repeat Yourself）原则
- 定期进行代码审查和重构

### 技术栈与框架约定
- Next.js 15+，使用 App Router 和 React Server Components（RSC）
- 客户端组件使用 Zustand 做状态管理
- 使用 `npx shadcn@latest add` 管理 Shadcn UI
- 移动优先与响应式设计
- 侧重服务端逻辑
- 渐进式 Web 应用（PWA）结构

### 项目结构
```
├── app/
│   ├── (auth)/           # Auth-related routes/pages
│   ├── (dashboard)/      # Dashboard routes/pages
│   ├── api/              # API routes
│   └── layout.tsx        # Root layout
├── components/
│   ├── shared/           # Shared UI components
│   ├── features/         # Feature-specific components
│   └── ui/               # Shadcn UI components
├── lib/
│   ├── supabase/         # Supabase client and utilities
│   ├── constants/        # Global constants
│   ├── hooks/            # Custom React hooks
│   ├── middleware/       # Custom middleware
│   └── utils/           # Shared utility functions
└── ...
```

## 使用方法

1. **初始设置**：
   - 在项目根目录创建 `ProjectDocs` 文件夹
   - 添加 `contexts` 文件夹，至少包含一个 `projectContext.md` 文件
   - 搭建 `Build_Notes` 目录结构

2. **上下文文件**：
   - 先创建 `projectContext.md`，包含：
     - 项目目标与目的
     - 技术栈细节
     - 集成规格说明
     - 架构概览
   - 按需添加额外的上下文文件（如 `appFlow.md`、`authFlow.md`）

3. **构建笔记**：
   - 为具体任务组创建单独的构建笔记文件
   - 遵循命名约定：`build-title_phase-#_task-group-name.md`
   - 包含任务目标、当前状态、未来状态和实施计划

4. **最佳实践**：
   - 为每个构建笔记创建单独的 Cursor Agent 对话
   - 保持上下文文件更新但稳定
   - 把已完成的构建笔记移入相应目录
   - 与 Agent 协作时引用具体的上下文文件

### 构建笔记结构
每个构建笔记应包含：
1. **任务目标**：目标简述
2. **当前状态评估**：当前项目状态的描述
3. **未来状态目标**：期望结果的描述
4. **实施计划**：带检查清单任务的编号步骤
   - 任务完成后同步更新
   - 划掉不适用的任务（绝不删除）
   - 按需添加新步骤/任务

## 开发标准

### 错误处理与校验
- 在函数开头用守卫子句处理错误
- 用 if-return 模式减少嵌套
- 用 Zod 实现模式校验
- react-hook-form 配合 useActionState 使用
- 实现恰当的错误日志记录和用户友好的提示信息

### 状态管理与数据获取
- 优先使用 React Server Components 获取数据
- 使用 Supabase 处理实时数据
- 实现预加载模式
- 使用 Vercel KV 存储聊天记录和进行速率限制

### 测试与质量保证
- 为工具函数和 hooks 编写单元测试
- 为复杂组件编写集成测试
- 为关键流程编写端到端测试
- 本地 Supabase 测试
- 保持最低测试覆盖率

## 优势

- 通过一致的上下文减少 AI 幻觉
- 改善项目组织与文档
- 增强团队协作与知识共享
- 保持开发专注度与进度跟踪
- 提供清晰的项目历史与决策记录

## 自定义

`.cursorrules` 文件可按项目具体需求进行定制：
- 修改项目结构以匹配你的工作流
- 调整编码标准和约定
- 更新文档要求
- 添加项目专属的规则和指南

## 开始使用

1. 把 `.cursorrules` 文件复制到你的项目中
2. 搭建 `ProjectDocs` 目录结构
3. 创建初始的 `projectContext.md`
4. 为你的任务开始编写构建笔记

## 贡献

欢迎 fork 并按自己的项目修改这些规则。欢迎通过 pull request 提交贡献和改进。

## 许可证

MIT License - 可自由用于你的项目并修改。

---

由 [@kryptobaseddev](https://github.com/kryptobaseddev) 创建
