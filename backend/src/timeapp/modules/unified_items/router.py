"""统一事项模块路由。

负责确认分发与统一事项展示相关接口。
"""

from fastapi import APIRouter

router = APIRouter(prefix="/unified-items", tags=["unified-items"])
