# Salesforce Apex .cursorrules 提示词文件

**作者：**James Simone

本 `.cursorrules` 文件将 Cursor AI 配置为一名资深全栈 Salesforce 开发者，精通 Apex、设计模式（GoF、Null Object、Repository）和面向对象编程。

规则强调：

- **可测试性：**优先编写易于测试的代码，充分利用既有模式。
- **简洁与可读性：**编写清晰、简洁、易维护的代码。
- **性能：**在性能与可读性之间取得平衡。
- **可复用性：**创建可复用的类和方法。

关键技术指南包括：

- 使用 `System.Queueable` 配合 `System.Finalizer` 进行异步操作（替代 `@future`）。
- 优先使用 Null Object 模式和多态，而非嵌套条件判断。
- 遵循特定的变量命名约定（如 Map 使用 `keyToValue`）。
- 使用 `Enums` 而非字符串常量。
- 除非已在使用 Selector 模式，否则对 DML/SOQL 采用 Repository 模式。
- 遵循特定的类结构（"newspaper" 规则）与注释规范。
- 使用 `TODO:` 注释标记缺陷或欠佳的代码。
