# Timeflow

Timeflow 是一个单仓库项目，包含 FastAPI 后端和 Expo React Native 移动端。

## 固定版本

- Node.js `20.20.2` / npm `10.8.2`，见 `.nvmrc` 和 `package.json`。
- Python `3.11.15` / uv `0.11.28`，见 `.python-version`、`backend/pyproject.toml` 和 `backend/uv.lock`。
- PostgreSQL `16.4`，由根目录 Docker Compose 提供。

## 首次安装

```bash
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env
npm run install:frontend
npm run install:backend
```

## 启动

启动 PostgreSQL 和 API：

```bash
docker compose up --build
```

只启动移动端：

```bash
npm run dev:frontend
```

API 健康检查：<http://127.0.0.1:8000/api/v1/health>

## 质量检查

```bash
npm run check:frontend
npm run check:backend
```

后端使用 `uv` 管理依赖，前端使用 `npm` 管理依赖。两种语言使用各自原生的锁文件，根目录脚本只负责统一入口。

后端按 Agent 边界组织：`agents/` 放主 Agent 和专项 Agent，`common/` 放公共数据、确认、反问、LLM、任务级画像和统一响应契约，`basic/` 放手动业务与 OCR/ASR。只有主 Agent 暴露 Agent HTTP 入口；专项 Agent 是内部能力包，不直接读写数据库，统一响应契约见 `backend/src/timeapp/common/contracts/agent_response.py`。
