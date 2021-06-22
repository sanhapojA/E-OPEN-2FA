import requests
import json
from accessToken import Signature


def UserInfo():
    url = "https://open-api.settrade.com/api/um/v1/{brokerId}/admin/2fa/user-info/{username}".format(
        username='SanhawatA',
        brokerId='505'
    )

    body = {
        "username": "SanhawatA",
        "telNo": "66827219557",
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


print(Signature())
