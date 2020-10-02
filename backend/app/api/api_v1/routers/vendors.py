from fastapi import APIRouter, Request, Depends, Response, encoders
import typing as t

from app.db.schemas import Vendor, VendorCreate, VendorEdit
from core.auth import get_current_active_superuser
from db.crud import get_vendors, edit_vendor, delete_vendor, get_vendor, create_vendor
from db.session import get_db

vendors_router = r = APIRouter()


@r.get(
    "/vendors",
    response_model=t.List[Vendor],
    response_model_exclude_none=True,
)
async def vendors_list(
        response: Response,
        db=Depends(get_db),
        current_user=Depends(get_current_active_superuser),
):
    """
    Get all Vendors
    """
    vendors = get_vendors(db)
    # This is necessary for react-admin to work
    response.headers["Content-Range"] = f"0-9/{len(vendors)}"
    return vendors


@r.get(
    "/vendors/{vendor_id}",
    response_model=Vendor,
    response_model_exclude_none=True,
)
async def vendor_details(
        request: Request,
        vendor_id: int,
        db=Depends(get_db),
        current_user=Depends(get_current_active_superuser),
):
    """
    Get any vendor details
    """
    vendor = get_vendor(db, vendor_id)
    return vendor


@r.post("/vendors", response_model=Vendor, response_model_exclude_none=True)
async def vendor_create(
        request: Request,
        vendor: VendorCreate,
        db=Depends(get_db),
        current_user=Depends(get_current_active_superuser),
):
    """
    Create a new Vendor
    """
    return create_vendor(db, vendor)


@r.put(
    "/vendors/{vendor_id}", response_model=Vendor, response_model_exclude_none=True
)
async def vendor_edit(
        request: Request,
        vendor_id: int,
        vendor: VendorEdit,
        db=Depends(get_db),
        current_user=Depends(get_current_active_superuser),
):
    """
    Update existing vendor
    """
    return edit_vendor(db, vendor_id, vendor)


@r.delete(
    "/vendors/{vendor_id}", response_model=Vendor, response_model_exclude_none=True
)
async def vendor_delete(
        request: Request,
        vendor_id: int,
        db=Depends(get_db),
        current_user=Depends(get_current_active_superuser),
):
    """
    Delete existing vendor
    """
    return delete_vendor(db, vendor_id)
