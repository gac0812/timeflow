"""智能提醒模块路由。

负责提醒规则、触发与通知相关接口。
"""

from fastapi import APIRouter

router = APIRouter(prefix="/reminders", tags=["reminders"])
