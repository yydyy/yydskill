---
name: cocos-skills
description: Cocos Creator 2.4.x / 3.x 开发规范：版本语法差异、组件与生命周期、渲染与内存性能、异步回调安全、禁止扩展引擎类型。用于编写或审查 Cocos Creator 的 TypeScript/JavaScript 代码、场景、预制体和资源加载逻辑。
---

# Cocos引擎开发

通用编码约束（先问后写、极简、自检）见 `coding-rules`，这里只写 Cocos 专属规则。

## 1. 版本意识

- 动手前先确认项目的 Cocos Creator 版本：2.4.x 与 3.x 的 API 不兼容。
- 必须区分 2.4.x（`cc.Node`、`cc.Vec2`、`cc.loader` / `cc.resources`）与 3.x（`import { Node, Vec3 } from 'cc'`、`setPosition`、`resources`）语法。
- 优先 TypeScript 严格类型，避免 `any`。

## 2. 组件使用规范

- 使用 Cocos 组件前先查阅对应版本的 API 文档，确认参数与生命周期语义（`onLoad` / `start` / `onEnable` / `onDisable` / `onDestroy`）。
- 不确定某个 API 在当前版本是否存在时，明确说出来并请求确认，禁止凭经验臆测调用。

## 3. 性能优先

- **渲染**：优先考虑静态合批、GPU Instancing、RenderTexture 管理。
- **DrawCall 守卫**：当 UI 布局或节点结构可能破坏合批（材质混用、图集混用、层级交错）时必须预警。
- **分配**：减少 `update()` 与高频循环中的对象创建，优先预分配和复用临时向量。
- **内存**：高频实例化场景使用对象池（`cc.NodePool` / `NodePool`），并明确 `addRef` / `decRef` / `release` 释放策略。
- **泄漏**：注册事件、计时器时必须同时给出 `off` / `unschedule` / 销毁时的清理逻辑。

## 4. 同步架构

- 坚持逻辑层与表现层分离。
- 帧同步 / 状态同步要保证确定性逻辑，警惕浮点误差和依赖帧率的计算。

## 5. 异步安全

- 异步回调（`resources.load`、`scheduleOnce`、`Promise`、网络回调）执行前，先检查 `this.node && this.node.isValid`（3.x 可用 `isValid(this.node)`）。

## 6. 禁止扩展引擎类型

- **严格禁止**：不要在引擎系统类型（`cc.Node`、`cc.Component` 等）的实例上新增自定义字段。
- ❌ 错误：`node.age = 10`
- ✅ 正确：在自定义组件上声明字段。

## 7. 输出要求

- 每个方案简述一个潜在代价，例如"内存增加换取 DrawCall 降低"。
