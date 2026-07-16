"""应用使用管理模块路由。

负责应用分类、使用监控与限制等相关接口。
"""

from fastapi import APIRouter

router = APIRouter(prefix="/usage-management", tags=["usage-management"])
