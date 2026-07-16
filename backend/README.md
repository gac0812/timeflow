# TimeApp API

一个小而清晰的 FastAPI 项目，使用 `src` 布局与按功能领域分层的模块结构。

## 环境要求

- Python 3.11+
- [uv](https://docs.astral.sh/uv/)

## 启动

```bash
cd backend
cp .env.example .env  # 可选
uv sync
uv run uvicorn timeapp.main:app --reload
```

服务启动后可访问：

- 健康检查：http://127.0.0.1:8000/api/v1/health
- OpenAPI 文档：http://127.0.0.1:8000/docs

## 测试

```bash
uv run pytest
```

## 目录结构

```text
src/timeapp/
├── main.py                          # 创建 FastAPI，注册总路由
├── api/
│   ├── router.py                    # 聚合各领域模块的 router
│   ├── health.py                    # 运维探活（非业务域）
│   └── dependencies.py              # 登录用户、数据库会话等公共依赖
├── core/
│   └── config.py                    # 环境变量、系统配置
└── modules/
    ├── identity/                    # 个人信息
    ├── scheduling/                  # 调度：日程、待办
    ├── reminders/                   # 智能提醒
    ├── multimodal/                  # 多模态：文字、语音、图片解析
    ├── goal_planning/               # 任务拆分：长期目标、计划对话、草稿、子任务
    ├── feedback/                    # 执行反馈
    ├── replanning/                  # 智能时间重排
    ├── unified_items/               # 统一确认分发与事项展示
    ├── reviews/                     # 目标复盘、周期复盘
    └── usage_management/            # 应用使用管理
tests/
└── test_health.py
```
