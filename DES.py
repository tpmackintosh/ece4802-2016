from Crypto.Cipher import DES
import codecs

pt = "48656c6c6f212121"
ct = "d52bd481f21e25a1"

pt = pt.decode("hex")
ct = ct.decode("hex")

iv = "00000000".decode("hex")
key = "0000000000000000".decode("hex")

for x in range(4**8):
    cipher = DES.new(key^x, DES.MODE_ECB)
    msg = cipher.encrypt(pt)
    if msg == ct:
        break
