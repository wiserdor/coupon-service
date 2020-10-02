import uuid

from fastapi import HTTPException, status
from sqlalchemy.orm import Session
import typing as t

from . import models, schemas
from app.core.security import get_password_hash
from app.mailjet import send_email


def get_vendors(db: Session, skip: int = 0, limit: int = 100) -> t.List[schemas.VendorOut]:
    return db.query(models.Vendor).offset(skip).limit(limit).all()


def get_vendor(db: Session, vendor_id: int):
    vendor = db.query(models.Vendor).filter(models.Vendor.id == vendor_id).first()
    if not vendor:
        raise HTTPException(status_code=404, detail="Vendor not found")
    return vendor


def get_vendor_by_email(db: Session, email: str) -> schemas.Vendor:
    vendor = db.query(models.Vendor).filter(models.Vendor.email == email).first()
    if not vendor:
        raise HTTPException(status_code=404, detail="Vendor not found")
    return vendor


def create_vendor(db: Session, vendor: schemas.VendorCreate):
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
        db: Session, vendor_id: int, vendor: schemas.VendorEdit
) -> schemas.CouponEdit:
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


################
####    Coupons#
################
def get_coupon(db: Session, coupon_id: int):
    coupon = db.query(models.Coupon).filter(models.Coupon.id == coupon_id).first()
    if not coupon:
        raise HTTPException(status_code=404, detail="Coupon not found")
    return coupon


def get_coupons(
        db: Session, skip: int = 0, limit: int = 100
) -> t.List[schemas.CouponOut]:
    return db.query(models.Coupon).offset(skip).limit(limit).all()


def get_coupons_by_email(db: Session, email: str) -> schemas.CouponBase:
    return db.query(models.Coupon).filter(models.Coupon.email == email).all()


def get_coupon_by_coupon_id(db: Session, coupon_id: str) -> schemas.Coupon:
    coupon = db.query(models.Coupon).filter(models.Coupon.coupon_id == coupon_id).first()
    if not coupon:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Coupon not found")
    return coupon

def create_coupon(db: Session, coupon: schemas.CouponCreate):
    db_coupon = models.Coupon(
        name=coupon.name,
        email=coupon.email,
    )
    db.add(db_coupon)
    db.commit()
    db.refresh(db_coupon)
    print("sending")
    send_email(coupon.email, 'Shafir and omri', 'girl', 'הקופון שלך מוכן', 'קיבלת קופון', db_coupon.coupon_id)
    return db_coupon


def delete_coupon(db: Session, coupon_id: int):
    coupon = get_coupon(db, coupon_id)
    if not coupon:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Coupon not found")
    db.delete(coupon)
    db.commit()
    return coupon


def edit_coupon(
        db: Session, coupon_id: int, coupon: schemas.CouponEdit
) -> schemas.CouponEdit:
    db_coupon = get_coupon(db, coupon_id)
    if not db_coupon:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Coupon not found")
    update_data = coupon.dict(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_coupon, key, value)

    db.add(db_coupon)
    db.commit()
    db.refresh(db_coupon)
    return db_coupon


#####################
######### Users     #
#####################
def get_user(db: Session, user_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


def get_user_by_email(db: Session, email: str) -> schemas.UserBase:
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(
        db: Session, skip: int = 0, limit: int = 100
) -> t.List[schemas.UserOut]:
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        is_active=user.is_active,
        is_superuser=user.is_superuser,
        hashed_password=hashed_password,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int):
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="User not found")
    db.delete(user)
    db.commit()
    return user


def edit_user(
        db: Session, user_id: int, user: schemas.UserEdit
) -> schemas.User:
    db_user = get_user(db, user_id)
    if not db_user:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="User not found")
    update_data = user.dict(exclude_unset=True)

    if "password" in update_data:
        update_data["hashed_password"] = get_password_hash(user.password)
        del update_data["password"]

    for key, value in update_data.items():
        setattr(db_user, key, value)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
