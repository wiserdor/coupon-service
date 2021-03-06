from datetime import datetime

from fastapi import APIRouter, Request, Depends, Response, HTTPException
import typing as t

from starlette.responses import RedirectResponse

from app.db.schemas.coupons import Coupon, CouponCreate, CouponEdit, CouponValidate, CouponOut
from core.auth import get_current_active_superuser
from db.crud.coupons import (
    get_coupons,
    create_coupon,
    edit_coupon,
    delete_coupon,
    get_coupon,
    get_coupon_by_coupon_id
)
from db.crud.vendors import get_vendor_by_email
from db.models import CouponConfig
from db.session import get_db

coupons_router = r = APIRouter()
public_coupon_router = rp = APIRouter()


@r.get(
    "/coupons",
    response_model=t.List[Coupon],
    response_model_exclude_none=True,
)
async def coupons_list(
        response: Response,
        db=Depends(get_db),
        current_user=Depends(get_current_active_superuser),
):
    """
    Get all Coupons
    """
    coupons = get_coupons(db)
    # This is necessary for react-admin to work
    response.headers["Content-Range"] = f"0-9/{len(coupons)}"
    return coupons


@r.get(
    "/coupons/{coupon_id}",
    response_model=Coupon,
    response_model_exclude_none=True,
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
    coupon = get_coupon(db, coupon_id)
    return coupon


@rp.post("/coupons", response_model=Coupon, response_model_exclude_none=True)
async def coupon_create(
        request: Request,
        coupon: CouponCreate,
        db=Depends(get_db),
):
    """
    Create a new Coupon
    """
    coupon_config = db.query(CouponConfig).first()

    user_coupons_count = db.query(Coupon).filter(Coupon.email == coupon.email and Coupon.phone == coupon.phone).count()
    if user_coupons_count == coupon_config:
        return HTTPException(400, 'User reached coupon limit')
    coupon.email = coupon.email.lower()
    return create_coupon(db, coupon)


@r.put(
    "/coupons/{coupon_id}", response_model=Coupon, response_model_exclude_none=True
)
async def coupon_edit(
        request: Request,
        coupon_id: int,
        coupon: CouponEdit,
        db=Depends(get_db),
        current_user=Depends(get_current_active_superuser),
):
    """
    Update existing coupon
    """
    return edit_coupon(db, coupon_id, coupon)


@r.delete(
    "/coupons/{coupon_id}", response_model=Coupon, response_model_exclude_none=True
)
async def coupon_delete(
        request: Request,
        coupon_id: int,
        db=Depends(get_db),
        current_user=Depends(get_current_active_superuser),
):
    """
    Delete existing coupon
    """
    return delete_coupon(db, coupon_id)


@rp.post(
    "/validate", response_model_exclude_none=True
)
async def validate_coupon(
        request: Request,
        coupon_validation: CouponValidate,
        db=Depends(get_db),
):
    """
    Validate coupon
    """
    coupon = get_coupon_by_coupon_id(db, coupon_validation.coupon_id)
    vendor = get_vendor_by_email(db, coupon_validation.email)
    coupon_config = db.query(CouponConfig).first()

    if coupon_validation.password == coupon_config.hair_password:
        if coupon.hair_used:
            raise HTTPException(409, "Coupon already used")
        else:
            coupon.hair_used = True
            coupon.hair_scanned_date = datetime.utcnow()
            coupon.hair_scanned_location = coupon_validation.geo_location
            db.commit()
    elif coupon_validation.password == coupon_config.dress_password:
        if coupon.dress_used:
            raise HTTPException(409, "Coupon already used")
        else:
            coupon.dress_used = True
            coupon.dress_scanned_date = datetime.utcnow()
            coupon.dress_scanned_location = coupon_validation.geo_location
            db.commit()
    elif coupon_validation.password == coupon_config.makeup_password:
        if coupon.makeup_used:
            raise HTTPException(409, "Coupon already used")
        else:
            coupon.makeup_used = True
            coupon.makeup_scanned_date = datetime.utcnow()
            coupon.makeup_scanned_location = coupon_validation.geo_location
            db.commit()
    else:
        raise HTTPException(401, "Incorrect Values")


@rp.get(
    "/coupons/validate/{coupon_id}",
    response_model=Coupon,
    response_model_exclude_none=True,
)
async def coupon_exists(
        request: Request,
        coupon_id: str,
        db=Depends(get_db),
        current_user=Depends(get_current_active_superuser),
):
    """
    Get any coupon details
    """
    coupon = get_coupon_by_coupon_id(db, coupon_id)
