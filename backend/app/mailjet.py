# import the mailjet wrapper
import qrcode
import os
from mailjet_rest import Client
import base64
from io import BytesIO
from sqlalchemy.orm import Session
from db import models

# Get your environment Mailjet keys

API_KEY = os.getenv('MAILJET_API')
API_SECRET = os.getenv('MAILJET_SECRET')
SITE_URL = os.getenv('SITE_URL')

mailjet = Client(auth=(API_KEY, API_SECRET), version='v3.1')


def send_email(db: Session, to_mail, from_name, to_name, subject, text_part, coupon_id):
    qr_link = f"{SITE_URL}coupon/" + str(coupon_id)
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)
    qr.add_data(qr_link)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    file_name = 'qrcode-' + str(coupon_id) + '.png'

    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    img_b = base64.b64encode(buffered.getvalue())
    img_str = img_b.decode('ascii')

    coupon_config = db.query(models.CouponConfig).first()
    html_string = coupon_config.email_template
    html_string = html_string.replace('$$LINK$$', qr_link)

    data = {
        'Messages': [
            {
                "From": {
                    "Email": "info@neshef.co.il",
                    "Name": from_name
                },
                "To": [
                    {
                        "Email": to_mail,
                        "Name": to_name
                    }
                ],
                "Subject": subject,
                "TextPart": text_part,
                "HTMLPart": html_string,
                "InlinedAttachments": [
                    {
                        "ContentType": "image/png",
                        "Filename": "logo.png",
                        "ContentID": "id1",
                        "Base64Content": img_str
                    }
                ]
            }
        ]
    }
    result = mailjet.send.create(data=data)
    print(result)
