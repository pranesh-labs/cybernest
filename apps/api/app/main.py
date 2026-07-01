from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import structlog
from shared_python import setup_logging
from app.api.v1.api import api_router
from app.core.config import settings

# Initialize structured logging before anything else
setup_logging(environment=settings.ENVIRONMENT, log_level_str=settings.LOG_LEVEL)
logger = structlog.get_logger()

app = FastAPI(
    title="CyberNest API",
    description="Backend services for CyberNest Cybersecurity SaaS Platform",
    version="1.0.0",
    docs_url="/api/docs" if settings.ENVIRONMENT != "production" else None,
    redoc_url="/api/redoc" if settings.ENVIRONMENT != "production" else None,
)

# Configure CORS for React app requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify actual frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount api routers
app.include_router(api_router, prefix="/api/v1")

@app.on_event("startup")
async def startup_event() -> None:
    await logger.ainfo(
        "Application startup",
        environment=settings.ENVIRONMENT,
        log_level=settings.LOG_LEVEL,
    )

@app.on_event("shutdown")
async def shutdown_event() -> None:
    await logger.ainfo("Application shutdown")

@app.get("/")
async def root() -> dict:
    return {
        "name": "CyberNest API",
        "status": "healthy",
        "version": "1.0.0"
    }
