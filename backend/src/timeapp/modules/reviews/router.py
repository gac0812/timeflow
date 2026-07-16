"""复盘模块路由。

负责目标复盘与周期复盘相关接口。
"""

from fastapi import APIRouter

router = APIRouter(prefix="/reviews", tags=["reviews"])
