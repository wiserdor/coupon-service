#!/usr/bin/env python3

from app.db.session import get_db
from app.db.crud.users import create_user
from app.db.crud.coupon_config import create_coupon_config
from app.db.schemas.users import UserCreate
from app.db.session import SessionLocal


def init() -> None:
    db = SessionLocal()

    create_user(
        db,
        UserCreate(
            email="shafir@fashion.com",
            password="password",
            is_active=True,
            is_superuser=True,
        ),
    )

    create_coupon_config(db)


if __name__ == "__main__":
    print("Creating superuser shafir@fashion.com")
    init()
    print("Superuser created")
