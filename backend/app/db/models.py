import uuid

from sqlalchemy import Boolean, Column, Integer, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
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
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    phone = Column(String, nullable=False)
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
    created_date = Column(DateTime, default=datetime.utcnow())
    hair_scanned_date = Column(DateTime, default=None)
    makeup_scanned_date = Column(DateTime, default=None)
    dress_scanned_date = Column(DateTime, default=None)
    hair_scanned_location = Column(String, default=None)
    dress_scanned_location = Column(String, default=None)
    makeup_scanned_location = Column(String, default=None)


class Vendor(Base):
    __tablename__ = "vendor"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    phone = Column(String)


class CouponConfig(Base):
    __tablename__ = "coupon_config"

    id = Column(Integer, primary_key=True, index=True)
    max_coupons_per_user = Column(Integer, default='500')
    hair_password = Column(String, default='hair')
    dress_password = Column(String, default='dress')
    makeup_password = Column(String, default='makeup')
    email_template = Column(String, default='<img src="cid:id1"><div><a href="$$LINK$$">link</a></div>')
