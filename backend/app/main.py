from fastapi import FastAPI, Depends
from starlette.requests import Request
import uvicorn

from app.api.api_v1.routers.vendors import vendors_router
from app.api.api_v1.routers.users import users_router
from app.api.api_v1.routers.auth import auth_router
from app.api.api_v1.routers.coupon import coupons_router, public_coupon_router
from app.api.api_v1.routers.coupon_config import coupon_config_router
from app.core import config
from app.db.session import SessionLocal
from app.core.auth import get_current_active_user, get_current_active_superuser
from app.core.celery_app import celery_app

app = FastAPI(
    title=config.PROJECT_NAME, docs_url="/api/docs", openapi_url="/api", debug=True
)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    request.state.db = SessionLocal()
    response = await call_next(request)
    request.state.db.close()
    return response


@app.get("/api/v1")
async def root():
    return {"message": "neshef api"}


# Routers
app.include_router(
    users_router,
    prefix="/api/v1",
    tags=["users"],
    dependencies=[Depends(get_current_active_user)],
)
app.include_router(
    coupons_router,
    prefix="/api/v1",
    tags=["coupons"],
    dependencies=[Depends(get_current_active_user)],
)
app.include_router(
    coupon_config_router,
    prefix="/api/v1",
    tags=["coupon_config"],
    dependencies=[Depends(get_current_active_user)],
)
app.include_router(
    public_coupon_router,
    prefix="/api/v1",
    tags=["coupons"],
)
app.include_router(
    vendors_router,
    prefix="/api/v1",
    tags=["vendors"],
    dependencies=[Depends(get_current_active_user)],
)
app.include_router(auth_router, prefix="/api", tags=["auth"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8888)
