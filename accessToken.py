from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec

import base64
import time
import requests
import json

timestamp = int(round(time.time() * 1000))

"""

ทำการเรียกใช้ API ตามหลักการ ดังนี้

a. เมื่อสมาชิก ได้รับ API Key และ API Secret แล้วนั้น สมาชิกจาเป็นต้องพัฒนาระบบสาหรับการต่อเชื่อมกับ Settrade Admin API 
โดยในทุก Admin API ที่ Settrade ให้บริการนั้น จำเป็นต้องใช้ Access Token ในการเข้าใช้บริการ

b. สมาชิกสามารถขอ Access Token เพื่อเข้าใช้บริการโดยการใช้งาน Issue Access Token API เพื่อขอ Access Token 
ซึ่งตัว Access Token นั้น จะมีอายุจำกัด ในกรณีที่ต้องการยืดอายุ Access Token สามารถทำได้โดยการเรียกใช้ Refresh Token API

c. เมื่อได้รับ Access Token แล้ว สมาชิกสามารถเรียกใช้ Admin API ที่ Settrade ให้บริการ โดยการแนบ Access Token 
ไปพร้อมกับ Request Header ตาม Specification

"""

broker_id = "505"
api_key = "oZetsel78hPudXWL"

def Signature():

    api_secret = b'ALX9sYz97u94xwsSdijOzMmurSML1qFj84a2e5cKQv5L'
    params = ''

    payload = bytes(api_key + '.' + params + '.' + str(timestamp), encoding='utf-8')

    decode_secert_key = base64.b64decode(api_secret).hex()  # private key

    sign_key = ec.derive_private_key(int(decode_secert_key, 16), ec.SECP256R1(), default_backend())
    signature = sign_key.sign(payload, ec.ECDSA(hashes.SHA256()))

    return signature.hex()


def IssueAccessTokenAPI():
    url = "https://open-api.settrade.com/api/oam/v1/{broker_id}/broker-apps/ADMIN/login".format(broker_id=broker_id)
    
    body = {
        "apiKey": api_key,
        "params": "",
        "signature": Signature(),
        "timestamp": timestamp,
    }

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, json=body)
    return json.loads( response.text )


print(IssueAccessTokenAPI())


