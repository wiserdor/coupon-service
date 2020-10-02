from fastapi import APIRouter, Request, Depends, Response, HTTPException, status
import typing as t

from starlette.responses import RedirectResponse

from app.db.schemas import Coupon, CouponCreate, CouponEdit, CouponValidate
from core.auth import get_current_active_superuser
from db.crud import get_coupons, create_coupon, edit_coupon, delete_coupon, get_coupon, get_coupon_by_coupon_id, \
    get_vendor_by_email
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
    response = RedirectResponse(url="http://localhost:8000/completed")
    coupon = get_coupon_by_coupon_id(db, coupon_validation.coupon_id)
    vendor = get_vendor_by_email(db, coupon_validation.email)
    if coupon_validation.password == "hair":
        if coupon.hair_used:
            raise HTTPException(409, "Coupon already used")
        else:
            coupon.hair_used = True
            db.commit()
    elif coupon_validation.password == "dress":
        if coupon.dress_used:
            raise HTTPException(409, "Coupon already used")
        else:
            coupon.dress_used = True
            db.commit()
    elif coupon_validation.password == "makeup":
        if coupon.makeup_used:
            raise HTTPException(409, "Coupon already used")
        else:
            coupon.makeup_used = True
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
