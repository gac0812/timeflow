"""重排模块路由。

负责智能时间重排相关接口。
"""

from fastapi import APIRouter

router = APIRouter(prefix="/replanning", tags=["replanning"])
