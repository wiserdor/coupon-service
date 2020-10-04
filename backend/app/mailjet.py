# import the mailjet wrapper
import qrcode

from mailjet_rest import Client
import base64
from io import BytesIO

# Get your environment Mailjet keys
API_KEY = ''
API_SECRET = ''

mailjet = Client(auth=(API_KEY, API_SECRET), version='v3.1')


def send_email(to_mail, from_name, to_name, subject, text_part, coupon_id):
    qr_link = "http://138.197.178.22/coupon/" + str(coupon_id)
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
    data = {
        'Messages': [
            {
                "From": {
                    "Email": "vgibsonsg@gmail.com",
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
                "HTMLPart": '<img src=\"cid:id1\"><div><a href=\"'+qr_link+'\">לינק</a></div>',
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
