import uuid

from sqlalchemy import Boolean, Column, Integer, String, text
from sqlalchemy.dialects.postgresql import UUID

from .session import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)


class Coupon(Base):
    __tablename__ = "coupon"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False)
    name = Column(String)
    coupon_id = Column(
        UUID(as_uuid=True),
        nullable=False,
        index=True,
        unique=True,
        default=uuid.uuid4,
    )
    dress_used = Column(Boolean, default=False)
    makeup_used = Column(Boolean, default=False)
    hair_used = Column(Boolean, default=False)


class Vendor(Base):
    __tablename__ = "vendor"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    name = Column(String)
    phone = Column(String)
