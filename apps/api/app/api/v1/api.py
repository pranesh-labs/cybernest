from fastapi import APIRouter
from app.api.v1.endpoints import agent, auth, devices

api_router = APIRouter()

# Register sub-routes
api_router.include_router(auth.router, prefix="/auth", tags=["authentication"])
api_router.include_router(devices.router, prefix="/devices", tags=["devices"])
api_router.include_router(agent.router, prefix="/agent", tags=["agent-communication"])
