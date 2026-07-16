"""个人信息模块路由。

负责用户资料、偏好等个人信息相关接口。
"""

from fastapi import APIRouter

router = APIRouter(prefix="/identity", tags=["identity"])
