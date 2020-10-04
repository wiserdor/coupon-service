from pydantic import BaseModel


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
