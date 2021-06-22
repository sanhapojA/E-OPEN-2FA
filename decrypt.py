from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# decryption:
try:
    key = b'wI0cxJgQyW5th1HOQN5ZgHvXiXCaX20N'
    iv_self = bytes('9577301744989195', encoding='UTF-8')
    ct = b64decode('TQcdopwWGdsiKYXh8Q4KSA==')
    cipher = AES.new(key, AES.MODE_CBC, iv_self)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    print("The message was: ", pt.decode('UTF-8'))
except ValueError:
    print("Incorrect decryption")