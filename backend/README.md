# Timeflow API

后端使用 Python 3.11、uv、FastAPI、SQLAlchemy、Alembic 和 PostgreSQL。

## 本地启动

```bash
cp .env.example .env
uv sync --locked --all-groups
uv run uvicorn timeapp.main:app --reload
```

如果本机没有 PostgreSQL，使用仓库根目录的 Compose：

```bash
docker compose up --build
```

健康检查：<http://127.0.0.1:8000/api/v1/health>

## Agent 目录边界

```text
src/timeapp/
├── agents/                 # 主 Agent 和专项 Agent
│   ├── main_agent/         # 唯一 Agent HTTP 入口和内部调度
│   │   ├── router.py
│   │   ├── schemas.py
│   │   └── dispatcher.py
│   ├── schedule_todo_agent/    # schemas.py + service.py + prompts.py
│   ├── task_breakdown_agent/   # schemas.py + service.py + prompts.py
│   ├── replanning_agent/       # schemas.py + service.py + prompts.py
│   ├── review_agent/           # schemas.py + service.py + prompts.py
│   └── feedback_agent/         # schemas.py + service.py + prompts.py
├── basic/                  # 手动业务、事项展示和 OCR/ASR
├── common/                 # 数据、确认、反问、LLM、任务级画像、跨 Agent 契约
├── api/                    # HTTP 路由聚合和基础设施探活
└── core/                   # 配置、数据库连接和基础设施
```

专项 Agent 是进程内能力包，不暴露 HTTP Router。它们只接收主 Agent 整理好的完整参数，返回 `AgentResponse`；不直接访问数据库、不负责追问，也不直接执行 `db_action`。所有写操作必须由主 Agent 在用户确认和公共数据校验后落盘。

## 测试与检查

```bash
uv run ruff check .
uv run ruff format --check .
uv run mypy
uv run pytest
```
