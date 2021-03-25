from pydantic import BaseModel


class VendorBase(BaseModel):
    email: str
    first_name: str
    last_name: str
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
