from sqlalchemy.orm import Session
from fastapi import HTTPException, status
import typing as t
from app.db import models

from db.schemas.coupon_config import CouponConfigOut, CouponConfigEdit


def get_coupon_config(
        db: Session
) -> t.List[CouponConfigOut]:
    return db.query(models.CouponConfig).all()


def get_coupon_config_by_id(db: Session):
    coupon = db.query(models.CouponConfig).first()
    if not coupon:
        raise HTTPException(status_code=404, detail="Coupon not found")
    return coupon


def edit_coupon_config(
        db: Session, coupon: CouponConfigEdit
) -> CouponConfigEdit:
    db_coupon = get_coupon_config_by_id(db)
    if not db_coupon:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Coupon config not found")
    update_data = coupon.dict(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_coupon, key, value)

    db.add(db_coupon)
    db.commit()
    db.refresh(db_coupon)
    return db_coupon


def create_coupon_config(db: Session):
    coupon_config = db.query(models.CouponConfig).first()
    if not coupon_config:
        coupon_config = models.CouponConfig()
        db.add(coupon_config)
        db.commit()
        db.refresh(coupon_config)
    return coupon_config


def delete_coupon_config(db: Session):
    coupon_config = get_coupon_config_by_id(db)
    if not coupon_config:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Coupon config not found")
    db.delete(coupon_config)
    db.commit()
    return coupon_config
