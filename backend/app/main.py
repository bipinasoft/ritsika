from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.router import api_router
app = FastAPI(title="Ritsika API", version="0.1.0")
app.add_middleware(CORSMiddleware, allow_origins=settings.cors_origin_list, allow_credentials=True,
                   allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE"],
                   allow_headers=["Authorization", "Content-Type", "X-Request-ID"])
app.include_router(api_router, prefix="/api/v1")
@app.get("/")
def root():
    return {"name": "Ritsika API", "docs": "/docs"}
