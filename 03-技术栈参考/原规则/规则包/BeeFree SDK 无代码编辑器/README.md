# Beefree SDK 集成指南

本文件夹包含一份全面的 `.cursorrules` 文件，为将 [Beefree SDK](https://docs.beefree.io/beefree-sdk) 嵌入 Web 应用提供指导方针和最佳实践，尤其适用于营销技术（Martech）行业的应用，或拥有大规模营销业务的企业内部定制开发的应用。[Beefree SDK](https://docs.beefree.io/beefree-sdk) 的前端包含一个无代码的邮件、页面和弹窗构建器。该规则文件作为开发伴侣，确保将 Beefree SDK 无代码内容编辑器一致、安全、高效地集成到你的应用中。

## 什么是 .cursorrules 文件？

`.cursorrules` 文件是一个配置文件，为 AI 编程助手提供使用 Beefree SDK 的具体指导方针。它包含：

- **安装指南**，用于正确完成 SDK 设置
- **身份验证最佳实践**，附带安全注意事项
- **配置示例**，覆盖不同用例
- **错误处理模式**，用于构建健壮的应用
- **代码示例**，涵盖 TypeScript、JavaScript 和 React
- **最佳实践**，涉及性能与安全

## 快速开始

### 1. 前提条件

在使用 Beefree SDK 之前，你需要：
- 一个带有 API 凭据的 Beefree 账户
- Node.js
- 一款现代 Web 浏览器

### 2. 安装

安装 Beefree SDK 包：

```bash
npm install @beefree.io/sdk
# or
yarn add @beefree.io/sdk
```

### 3. 环境设置

在项目根目录创建 `.env` 文件：

```env
BEE_CLIENT_ID=your_client_id_here
BEE_CLIENT_SECRET=your_client_secret_here
```

### 4. 基本实现

#### HTML 实现

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Beefree SDK Demo</title>
    <style>
        #beefree-sdk-container {
            height: 600px;
            width: 90%;
            margin: 20px auto;
            border: 1px solid #ddd;
            border-radius: 8px;
        }
    </style>
</head>
<body>
    <div id="beefree-sdk-container"></div>
    
    <script src="https://app-rsrc.getbee.io/plugin/BeefreeSDK.js"></script>
    <script>
        const beeConfig = {
            container: 'beefree-sdk-container',
            language: 'en-US',
            onSave: function (jsonFile, htmlFile) {
                console.log("Template saved:", jsonFile);
            },
            onError: function (errorMessage) {
                console.error("Beefree SDK error:", errorMessage);
            }
        };

        // Initialize with authentication
        async function initializeBeefree() {
            const token = await fetch('http://localhost:3001/proxy/bee-auth', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ uid: 'demo-user' })
            }).then(res => res.json());

            const bee = new BeefreeSDK(token);
            bee.start(beeConfig, {});
        }

        initializeBeefree();
    </script>
</body>
</html>
```

#### React 实现

```typescript
import { useEffect, useRef } from 'react';
import BeefreeSDK from '@beefree.io/sdk';

export default function BeefreeEditor() {
  const containerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    async function initializeEditor() {
      const beeConfig = {
        container: 'beefree-react-demo',
        language: 'en-US',
        onSave: (pageJson: string, pageHtml: string) => {
          console.log('Saved!', { pageJson, pageHtml });
        },
        onError: (error: unknown) => {
          console.error('Error:', error);
        }
      };

      const token = await fetch('http://localhost:3001/proxy/bee-auth', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ uid: 'demo-user' })
      }).then(res => res.json());

      const bee = new BeefreeSDK(token);
      bee.start(beeConfig, {});
    }

    initializeEditor();
  }, []);

  return (
    <div
      id="beefree-react-demo"
      ref={containerRef}
      style={{
        height: '600px',
        width: '90%',
        margin: '20px auto',
        border: '1px solid #ddd',
        borderRadius: '8px'
      }}
    />
  );
}
```

## 身份验证设置

### 安全最佳实践：代理服务器

始终使用代理服务器来保护你的凭据。创建一个 `proxy-server.js` 文件：

```javascript
import express from 'express';
import cors from 'cors';
import axios from 'axios';
import dotenv from 'dotenv';

dotenv.config();

const app = express();
const PORT = 3001;

app.use(cors());
app.use(express.json());

const BEE_CLIENT_ID = process.env.BEE_CLIENT_ID;
const BEE_CLIENT_SECRET = process.env.BEE_CLIENT_SECRET;

app.post('/proxy/bee-auth', async (req, res) => {
  try {
    const { uid } = req.body;
    
    const response = await axios.post(
      'https://auth.getbee.io/loginV2',
      {
        client_id: BEE_CLIENT_ID,
        client_secret: BEE_CLIENT_SECRET,
        uid: uid || 'demo-user'
      },
      { headers: { 'Content-Type': 'application/json' } }
    );
    
    res.json(response.data);
  } catch (error) {
    console.error('Auth error:', error.message);
    res.status(500).json({ error: 'Failed to authenticate' });
  }
});

app.listen(PORT, () => {
  console.log(`Proxy server running on http://localhost:${PORT}`);
});
```

启动代理服务器：

```bash
node proxy-server.js
```

## .cursorrules 涵盖的关键功能

### 1. 容器设置
- 正确的 HTML 容器配置
- CSS 样式指南
- React 集成模式

### 2. 配置选项
- 必填参数（container）
- 可选参数（language、merge tags、special links）
- 回调函数（onSave、onError、onAutoSave、onSend）

### 3. 模板管理
- 加载现有模板
- 将模板保存到 localStorage
- 自动保存功能
- HTML 导入能力

### 4. 错误处理
- 全面的错误处理模式
- 用户友好的错误提示
- 身份验证错误恢复

### 5. 自定义
- UI 主题
- 语言国际化
- 合并标签（merge tags）和特殊链接（special links）
- 自定义 CSS 集成

## 高级功能

### 模板加载

```typescript
// Load template from localStorage
const selectedTemplate = JSON.parse(localStorage.getItem('currentEmailData'));

if (selectedTemplate) {
  beefreeSDKInstance.start(selectedTemplate);
  console.log('Loaded template from localStorage');
} else {
  beefreeSDKInstance.start();
  console.log('Started with empty template');
}
```

### HTML 导入

```javascript
// Convert HTML to Beefree format
const response = await fetch('https://api.getbee.io/v1/conversion/html-to-json', {
  method: 'POST',
  headers: {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "text/html"
  },
  body: "<!DOCTYPE html><html><body><h1>Hello World</h1></body></html>"
}); 
const data = await response.json();
```

### 变更跟踪

```typescript
const beeConfig = {
  container: 'beefree-sdk-container',
  onChange: function (jsonFile, response) {
    console.log('Template changed:', jsonFile);
    console.log('Response:', response);
  }
};
```

## 最佳实践

### 性能
- 仅在需要时初始化 SDK
- 正确清理资源
- 实现恰当的错误处理

### 安全
- 切勿在前端代码中暴露凭据
- 使用代理服务器进行身份验证
- 验证用户输入

### 用户体验
- 显示加载指示器
- 显示有帮助的错误提示
- 实现自动保存功能

## 故障排查

### 常见问题

1. **身份验证错误**
   - 核实 `.env` 中的凭据
   - 确保代理服务器正在运行
   - 检查网络连接

2. **找不到容器**
   - 核实容器 ID 与配置一致
   - 确保在 SDK 初始化之前容器已存在

3. **SDK 未加载**
   - 检查浏览器控制台是否有错误
   - 确认 Beefree SDK 脚本已加载
   - 确保初始化顺序正确

### 调试模式

启用调试日志：

```typescript
const beeConfig = {
  container: 'beefree-sdk-container',
  debug: {
    all: true,                 // Enables all debug features
    inspectJson: true,        // Shows an eye icon to inspect JSON data for rows/modules
    showTranslationKeys: true // Displays translation keys instead of localized strings
  },
  onError: function (errorMessage) {
    console.error("Beefree SDK error:", errorMessage);
  }
};
```

## 资源

- [Beefree SDK 文档](https://docs.beefree.io/beefree-sdk)
- [HTML Importer API](https://docs.beefree.io/beefree-sdk/apis/html-importer-api/import-html)
- [React 示例仓库](https://github.com/BeefreeSDK/beefree-react-demo)
- [多版本概念](https://github.com/BeefreeSDK/beefree-sdk-simple-schema/tree/main/multiple-versions-concept)
