import typing as t

from fastapi import APIRouter, Response, Depends, Request

from app.core.auth import get_current_active_superuser
from app.db.crud.coupon_config import get_coupon_config, edit_coupon_config, create_coupon_config, \
    delete_coupon_config, get_coupon_config_by_id
from app.db.schemas.coupon_config import CouponConfigOut, CouponConfigEdit, CouponConfigCreate
from app.db.session import get_db

coupon_config_router = r = APIRouter()


@r.get(
    "/coupon_config",
    response_model=t.List[CouponConfigOut],
)
async def coupon_config_list(
        response: Response,
        db=Depends(get_db),
        current_user=Depends(get_current_active_superuser),
):
    """
    Get all Coupons
    """
    config = get_coupon_config(db)
    # This is necessary for react-admin to work
    response.headers["Content-Range"] = f"0-9/{len(config)}"
    return config


@r.get(
    "/coupon_config/{coupon_id}",
    response_model=CouponConfigOut,
)
async def coupon_details(
        request: Request,
        coupon_id: int,
        db=Depends(get_db),
        current_user=Depends(get_current_active_superuser),
):
    """
    Get any coupon details
    """
    coupon = get_coupon_config_by_id(db)
    return coupon


@r.put(
    "/coupon_config/{coupon_id}", response_model=CouponConfigEdit
)
async def coupon_config_edit(
        request: Request,
        coupon_id: int,
        coupon: CouponConfigEdit,
        db=Depends(get_db),
        current_user=Depends(get_current_active_superuser),
):
    """
    Update existing coupon
    """
    return edit_coupon_config(db, coupon)


@r.post("/coupon_config", response_model=CouponConfigOut)
async def coupon_config_create(
        request: Request,
        coupon: CouponConfigCreate,
        db=Depends(get_db),
):
    """
    Create a new Coupon
    """
    print('hi')
    return create_coupon_config(db)


@r.delete(
    "/coupon_config/{coupon_id}", response_model=CouponConfigOut
)
async def coupon_config_delete(
        request: Request,
        coupon_id: int,
        db=Depends(get_db),
        current_user=Depends(get_current_active_superuser),
):
    """
    Delete existing coupon
    """
    return delete_coupon_config(db)
