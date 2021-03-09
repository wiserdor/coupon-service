from pydantic import BaseModel
from typing import Optional, Any, Union


class CouponConfigBase(BaseModel):
    max_coupons_per_user: int
    hair_password: str
    dress_password: str
    makeup_password: str
    email_template: Union[None, str]


class CouponConfigOut(CouponConfigBase):
    id: Optional[int]
    pass

    class Config:
        orm_mode = True


class CouponConfigEdit(CouponConfigBase):
    id: int

    class Config:
        orm_mode = True


class CouponConfigCreate(CouponConfigBase):
    class Config:
        orm_mode = True
