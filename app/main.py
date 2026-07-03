from fastapi import FastAPI

from app.api.routes import router


app = FastAPI(
    title="Merchant AI Assistant API",
    description="AI-powered Merchant Assistant",
    version="1.0.0",
)

app.include_router(
    router,
    prefix="/v1",
)