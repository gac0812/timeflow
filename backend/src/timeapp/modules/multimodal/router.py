"""多模态处理模块路由。

负责文字、语音、图片等输入的解析与结构化相关接口。
"""

from fastapi import APIRouter

router = APIRouter(prefix="/multimodal", tags=["multimodal"])
