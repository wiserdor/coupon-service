"""Coupon tests"""
import json
from uuid import uuid4

from app.db import models
from app import mailjet


def test_get_coupon(client, test_db, superuser_token_headers):
    coupon = models.Coupon(first_name='test', last_name='test', phone='0544444444', email='fake@email.com')
    test_db.add(coupon)
    test_db.commit()
    response = client.get("/api/v1/coupons", headers=superuser_token_headers)
    assert response.status_code == 200
    assert len(response.json()) == 1
    res_coupon = response.json()[0]
    assert res_coupon['first_name'] == coupon.first_name
    assert res_coupon['last_name'] == coupon.last_name
    assert res_coupon['phone'] == coupon.phone
    assert res_coupon['email'] == coupon.email


def test_post_coupon(client, test_db, test_coupon_config, monkeypatch):
    monkeypatch.setattr(mailjet, "send_email", lambda: 'ok')

    coupon = {'first_name': 'test', 'last_name': 'test', 'phone': '0544444444', 'email': 'fake@email.com'}

    response = client.post("/api/v1/coupons", data=json.dumps(coupon))

    assert response.status_code == 200

    res_coupon = test_db.query(models.Coupon).all()
    assert len(res_coupon) == 1
    res_coupon = res_coupon[0]
    assert coupon['first_name'] == res_coupon.first_name
    assert coupon['last_name'] == res_coupon.last_name
    assert coupon['phone'] == res_coupon.phone
    assert coupon['email'] == res_coupon.email


def test_validate_coupon(client, test_db, test_coupon_config):
    coupon_data = {'first_name': 'test', 'last_name': 'test', 'phone': '0544444444', 'email': 'fake@email.com'}
    coupon = models.Coupon(**coupon_data)
    test_db.add(coupon)
    test_db.commit()

    vendor_data = {'email': 'vendor@test.com', 'first_name': 'test', 'last_name': 'test', 'phone': '123456789'}
    vendor = models.Vendor(**vendor_data)
    test_db.add(vendor)
    test_db.commit()

    payload = {"email": vendor.email,
               "phone": vendor.phone,
               "coupon_id": str(coupon.coupon_id),
               "password": test_coupon_config.hair_password,
               }

    response = client.post("/api/v1/validate", data=json.dumps(payload))

    assert response.status_code == 200

    first_coupon = test_db.query(models.Coupon).first()

    assert first_coupon.hair_used
    assert first_coupon.hair_vendor == vendor.email


def test_validate_coupon_not_valid(client, test_db, test_coupon_config):
    coupon_data = {'first_name': 'test', 'last_name': 'test', 'phone': '0544444444', 'email': 'fake@email.com'}
    coupon = models.Coupon(**coupon_data)
    test_db.add(coupon)
    test_db.commit()

    vendor_data = {'email': 'vendor@test.com', 'first_name': 'test', 'last_name': 'test', 'phone': '123456789'}
    vendor = models.Vendor(**vendor_data)
    test_db.add(vendor)
    test_db.commit()

    # Wrong mail

    payload = {"email": "wrong@test.com",
               "phone": "123456789",
               "coupon_id": str(coupon.coupon_id),
               "password": test_coupon_config.hair_password,
               }

    response = client.post("/api/v1/validate", data=json.dumps(payload))

    assert response.status_code == 404

    # Wrong password

    payload = {"email": vendor.email,
               "phone": "123456789",
               "coupon_id": str(coupon.coupon_id),
               "password": 'wrong password for test',
               }

    response = client.post("/api/v1/validate", data=json.dumps(payload))

    assert response.status_code == 401

    # Coupon already used

    coupon.hair_used = True
    test_db.commit()

    payload = {"email": vendor.email,
               "phone": "123456789",
               "coupon_id": str(coupon.coupon_id),
               "password": test_coupon_config.hair_password,
               }

    response = client.post("/api/v1/validate", data=json.dumps(payload))

    assert response.status_code == 409


def test_coupon_exists(client, test_db, test_coupon_config):
    """Test coupon exists"""
    coupon_data = {'first_name': 'test', 'last_name': 'test', 'phone': '0544444444', 'email': 'fake@email.com'}
    coupon = models.Coupon(**coupon_data)
    test_db.add(coupon)
    test_db.commit()

    response = client.get("/api/v1/coupons/validate/" + str(coupon.coupon_id))
    assert response.status_code == 200


def test_coupon_not_exists(client, test_db, test_coupon_config):
    """Test coupon not exists"""
    coupon_data = {'first_name': 'test', 'last_name': 'test', 'phone': '0544444444', 'email': 'fake@email.com'}
    coupon = models.Coupon(**coupon_data)
    test_db.add(coupon)
    test_db.commit()

    response = client.get('/api/v1/coupons/validate/' + str(uuid4()))
    assert response.status_code == 400
