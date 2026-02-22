from fastapi import FastAPI
from app.routes.assets import router as asset_router

app = FastAPI(title="Design Asset Management API")

app.include_router(asset_router, prefix="/assets", tags=["Assets"])
