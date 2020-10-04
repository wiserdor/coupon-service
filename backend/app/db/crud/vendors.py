from fastapi import HTTPException, status
from sqlalchemy.orm import Session
import typing as t

from app.db import models
from app.db.schemas.vendors import VendorOut, VendorCreate, VendorEdit, Vendor
from db.crud.coupons import get_coupon


def get_vendors(db: Session, skip: int = 0, limit: int = 100) -> t.List[VendorOut]:
    return db.query(models.Vendor).offset(skip).limit(limit).all()


def get_vendor(db: Session, vendor_id: int):
    vendor = db.query(models.Vendor).filter(models.Vendor.id == vendor_id).first()
    if not vendor:
        raise HTTPException(status_code=404, detail="Vendor not found")
    return vendor


def get_vendor_by_email(db: Session, email: str) -> Vendor:
    vendor = db.query(models.Vendor).filter(models.Vendor.email == email).first()
    if not vendor:
        raise HTTPException(status_code=404, detail="Vendor not found")
    return vendor


def create_vendor(db: Session, vendor: VendorCreate):
    db_vendor = models.Vendor(
        name=vendor.name,
        email=vendor.email,
        phone=vendor.phone
    )
    db.add(db_vendor)
    db.commit()
    db.refresh(db_vendor)
    return db_vendor


def delete_vendor(db: Session, vendor_id: int):
    vendor = get_coupon(db, vendor_id)
    if not vendor:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Vendor not found")
    db.delete(vendor)
    db.commit()
    return vendor


def edit_vendor(
        db: Session, vendor_id: int, vendor: VendorEdit
) -> Vendor:
    db_vendor = get_vendor(db, vendor_id)
    if not db_vendor:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Vendor not found")
    update_data = vendor.dict(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_vendor, key, value)

    db.add(db_vendor)
    db.commit()
    db.refresh(db_vendor)
    return db_vendor
