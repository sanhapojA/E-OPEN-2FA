import requests
import json

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec

import base64
import time

timestamp = int(round(time.time() * 1000))

def func_signature():

    api_key = "eY2SWPVfliurT6Hi"
    params = ''
    payload = bytes(api_key + '.' + params + '.' + str(timestamp), encoding='utf-8')

    api_secret = base64.b64decode(b'AMUYuLFBhZ+vexhXt6BdPSSmt5MLDTkKk3COzrYC73ah').hex()  # private key

    sign_key = ec.derive_private_key(int(api_secret, 16), ec.SECP256R1(), default_backend())
    signature = sign_key.sign(payload, ec.ECDSA(hashes.SHA256()))

    return signature.hex()

def issue_access_token_api():
    url = "https://open-api-test.settrade.com/api/oam/v1/505/broker-apps/ADMIN/login"
    body = {
        "apiKey": "eY2SWPVfliurT6Hi",
        "params": "",
        "signature": func_signature(),
        "timestamp": timestamp
    }
    headers = {"Content-Type": "application/json"}

    response = requests.request("POST", url, headers=headers, json=body )
    return json.loads( response.text )

access_token = issue_access_token_api()
token = access_token['access_token']
refresh_token = access_token['refresh_token']

def refresh_token():
    url = "https://open-api-test.settrade.com/api/oam/v1/505/broker-apps/ADMIN/refresh-token"

    body = {
        "apiKey": "eY2SWPVfliurT6Hi",
        "refreshToken": refresh_token
    }

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request( "POST", url, headers=headers, json=body )
    return json.loads( response.text )

def user_info():
    url = "https://open-api-test.settrade.com/api/um/v1/{brokerId}/admin/2fa/user-info/{username}".format(
        username='Sanhapoj',
        brokerId='505'
    )

    body = {
        "username": "Sanhapoj",
        "telNo": "66800000505",
        "telNoStatus": "A"
    }

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + token
    }

    response = requests.request("PUT", url, headers=headers, json=body)
    if response.status_code == 200:
        return 'Update Success'
    else:
        return response.status_code

def get_user_information():
    url = "https://open-api-test.settrade.com/api/um/v1/{brokerId}/admin/2fa/user-info/{username}".format\
        (
            brokerId = 505,
            username = 'Sanhapoj'
        )

    body = {
        "apiKey": "eY2SWPVfliurT6Hi",
        "refreshToken": refresh_token
    }

    headers = {
        'Authorization': 'Bearer ' + token
    }

    response = requests.request( "GET", url, headers=headers, json=body )
    return json.loads( response.text )

print(func_signature())

