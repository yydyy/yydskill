# Solidity Foundry .cursorrules 提示词文件

作者：heyjonbray
改编自 brolag 的 [solidity-hardhat-cursorrules](/rules/solidity-hardhat-cursorrules-prompt-file/)

## 你可以构建什么

- **安全的 DeFi 协议**：创建借贷平台、去中心化交易所或收益优化工具，遵循安全最佳实践。
- **NFT 与代币系统**：开发具备高级特性的 ERC-20、ERC-721 或 ERC-1155 实现。
- **DAO 治理**：为去中心化组织构建投票系统、提案机制和资金库管理。
- **市场基础设施**：创建托管系统、拍卖平台和去中心化商业解决方案。
- **预言机实现**：为链上应用开发安全的数据馈送和 VRF 实现。
- **安全工具**：创建审计辅助工具、漏洞扫描器和合约验证工具。
- **Layer 2 解决方案**：构建侧链、rollup 或跨链桥，以安全为先。
- **身份系统**：开发链上声誉、验证和认证协议。

## 优势

借助 Foundry 强大的模糊测试、分叉测试和 cheatcode 提升测试能力
通过 forge、cast 和 anvil 等专用工具改进开发工作流
利用 Foundry 内置的 gas 报告和快照功能实现更好的 gas 优化
使用 Foundry 的追踪工具实现更高效的调试

## 概要

专注于 Solidity 安全的智能合约开发者可以借助此提示词，使用最佳实践和 Foundry 等工具创建安全、高效、文档完善的区块链应用，在优化性能的同时大幅减少漏洞。

## .cursorrules 提示词概览

该 .cursorrules 文件确立了使用 Foundry 开发框架开发和加固 Solidity 智能合约的一系列指导准则。它强调简洁准确的代码实现，鼓励拥抱新技术，并概述了 Solidity 开发的多种最佳实践。包括使用特定的编码模式和工具来提升智能合约的安全性、可读性和可维护性，如使用显式的函数可见性修饰符、为状态变更实现事件，以及遵循 Checks-Effects-Interactions 模式。文件重点介绍了 Foundry 特有的测试能力，如模糊测试、不变量测试和 cheatcode，以实现全面的测试覆盖。它涉及使用 Foundry 的 gas 快照和报告工具进行 gas 效率相关的性能优化，并提供了融合 forge、cast 和 anvil 等 Foundry 专用工具的开发工作流。文件提倡文档最佳实践，注重为智能合约和测试场景维护清晰且最新的文档。
