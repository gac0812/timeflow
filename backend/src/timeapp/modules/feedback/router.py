"""反馈模块路由。

负责执行反馈的采集与处理相关接口。
"""

from fastapi import APIRouter

router = APIRouter(prefix="/feedback", tags=["feedback"])
