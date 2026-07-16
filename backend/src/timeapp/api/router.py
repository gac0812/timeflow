"""Aggregate routers from infrastructure and domain modules."""

from fastapi import APIRouter

from timeapp.api.health import router as health_router
from timeapp.modules.feedback.router import router as feedback_router
from timeapp.modules.goal_planning.router import router as goal_planning_router
from timeapp.modules.identity.router import router as identity_router
from timeapp.modules.multimodal.router import router as multimodal_router
from timeapp.modules.reminders.router import router as reminders_router
from timeapp.modules.replanning.router import router as replanning_router
from timeapp.modules.reviews.router import router as reviews_router
from timeapp.modules.scheduling.router import router as scheduling_router
from timeapp.modules.unified_items.router import router as unified_items_router
from timeapp.modules.usage_management.router import router as usage_management_router

api_router = APIRouter()
api_router.include_router(health_router)
api_router.include_router(identity_router)
api_router.include_router(scheduling_router)
api_router.include_router(reminders_router)
api_router.include_router(multimodal_router)
api_router.include_router(goal_planning_router)
api_router.include_router(feedback_router)
api_router.include_router(replanning_router)
api_router.include_router(unified_items_router)
api_router.include_router(reviews_router)
api_router.include_router(usage_management_router)
