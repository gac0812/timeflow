"""调度模块路由。

负责日程（Schedule）与待办（Todo）相关接口。
"""

from fastapi import APIRouter

router = APIRouter(prefix="/scheduling", tags=["scheduling"])
