from pydantic import BaseModel, UUID4
import typing as t


class VendorBase(BaseModel):
    email: str
    name: str
    phone: str


class VendorOut(VendorBase):
    pass


class VendorCreate(VendorBase):
    class Config:
        orm_mode = True


class VendorEdit(VendorBase):
    class Config:
        orm_mode = True


class Vendor(VendorBase):
    id: int

    class Config:
        orm_mode = True


class CouponBase(BaseModel):
    email: str
    name: str


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

    class Config:
        orm_mode = True


class CouponValidate(BaseModel):
    email: str
    phone: str
    coupon_id: str
    password: str

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str
    is_active: bool = True
    is_superuser: bool = False
    first_name: str = None
    last_name: str = None


class UserOut(UserBase):
    pass


class UserCreate(UserBase):
    password: str

    class Config:
        orm_mode = True


class UserEdit(UserBase):
    password: t.Optional[str] = None

    class Config:
        orm_mode = True


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str = None
    permissions: str = "user"
