from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import random

# encryption:


def directionFile():
    direction = r'O:/IT/2021-2022 IT Projects/E-Open/2FA/2FA-ENABLE-USER/user_info.txt'
    return direction


with open(directionFile(), 'r', encoding='UTF-8') as file:
    read_ = file.readlines()
    for i in range(0, len(read_)):
        file_col = read_[i].split('|')
        telNo = file_col[1]

        # Random IV
        randomIV = random.randint(int(str('1')*16), int(str('9')*16))
        IV = str(randomIV)

        # ข้อมูลที่ใช้ในการ encrypt แบบ CBC ต้องทำข้อมูลให้อยู่ในรูปเป็นข้อมูลชนิด bytes แล้ว encoding แบบ UTF-8
        data = bytes(telNo, encoding='UTF-8')
        key = bytes('wI0cxJgQyW5th1HOQN5ZgHvXiXCaX20N', encoding='UTF-8')
        iv = bytes(IV, encoding='UTF-8')

        # สร้างกุญแจโดยการนำข้อมูล key และ iv มาเข้ารหัสด้วย Mode CBC
        cipher = AES.new(key, AES.MODE_CBC, iv)

        # ทำการ encrypt ช้อมูลแบบ 16 bytes ( block_size )
        ciphertext = cipher.encrypt(pad(data, AES.block_size))
        ciphertext = b64encode(ciphertext).decode('UTF-8')

        print(IV + '|' + ciphertext)
    file.close()
