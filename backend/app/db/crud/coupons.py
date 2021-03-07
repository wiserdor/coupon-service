from fastapi import HTTPException, status
from sqlalchemy.orm import Session
import typing as t

from app.db import models
from app.db.schemas.coupons import CouponOut, CouponBase, Coupon, CouponCreate, CouponEdit
from mailjet import send_email


def get_coupon(db: Session, coupon_id: int):
    coupon = db.query(models.Coupon).filter(models.Coupon.id == coupon_id).first()
    if not coupon:
        raise HTTPException(status_code=404, detail="Coupon not found")
    return coupon


def get_coupons(
        db: Session, skip: int = 0, limit: int = 100
) -> t.List[Coupon]:
    return db.query(models.Coupon).offset(skip).limit(limit).all()


def get_coupons_by_email(db: Session, email: str) -> CouponBase:
    return db.query(models.Coupon).filter(models.Coupon.email == email).all()


def get_coupon_by_coupon_id(db: Session, coupon_id: str) -> Coupon:
    coupon = db.query(models.Coupon).filter(models.Coupon.coupon_id == coupon_id).first()
    if not coupon:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Coupon not found")
    return coupon


def create_coupon(db: Session, coupon: CouponCreate) -> CouponCreate:
    db_coupon = models.Coupon(
        first_name=coupon.first_name,
        last_name=coupon.last_name,
        phone=coupon.phone,
        email=coupon.email,
    )
    db.add(db_coupon)
    db.commit()
    db.refresh(db_coupon)
    print("sending")
    send_email(coupon.email, 'Shafir and omri', 'girl', 'הקופון שלך מוכן', 'קיבלת קופון', db_coupon.coupon_id)
    pprint.pprint(db_coupon.__dict__)
    return db_coupon


def delete_coupon(db: Session, coupon_id: int):
    coupon = get_coupon(db, coupon_id)
    if not coupon:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Coupon not found")
    db.delete(coupon)
    db.commit()
    return coupon


def edit_coupon(
        db: Session, coupon_id: int, coupon: CouponEdit
) -> CouponEdit:
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
