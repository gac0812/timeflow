"""任务拆分模块路由。

负责长期目标、计划对话、计划草稿与子任务相关接口。
"""

from fastapi import APIRouter

router = APIRouter(prefix="/goal-planning", tags=["goal-planning"])
