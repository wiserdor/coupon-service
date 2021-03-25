from datetime import datetime
from pydantic import BaseModel, UUID4
from typing import Optional


class CouponBase(BaseModel):
    email: str
    phone: str
    first_name: Optional[str]
    last_name: Optional[str]


class CouponOut(CouponBase):
    coupon_id: str
    dress_used: bool
    makeup_used: bool
    hair_used: bool


class CouponCreate(CouponBase):

    class Config:
        orm_mode = True


class CouponEdit(CouponBase):
    coupon_id: str

    class Config:
        orm_mode = True


class Coupon(CouponBase):
    id: int
    coupon_id: UUID4
    dress_used: bool
    makeup_used: bool
    hair_used: bool
    created_date: datetime
    hair_scanned_date: Optional[datetime]
    makeup_scanned_date: Optional[datetime]
    dress_scanned_date: Optional[datetime]
    dress_vendor: Optional[str]
    makeup_vendor: Optional[str]
    hair_vendor: Optional[str]
    hair_scanned_location: Optional[str]
    dress_scanned_location: Optional[str]
    makeup_scanned_location: Optional[str]

    class Config:
        orm_mode = True


class CouponValidate(BaseModel):
    email: str
    phone: Optional[str]
    coupon_id: str
    password: str
    geo_location: Optional[str]

    class Config:
        orm_mode = True
