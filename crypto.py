from Crypto.Cipher import AES

def encrypt(data, passw, iv='This is an IV456'):
    obj = AES.new(passw, AES.MODE_CFB, iv)
    ctext = obj.encrypt(data)
    return ctext

def decrypt(data, passw, iv='This is an IV456'):
   obj2 = AES.new(passw, AES.MODE_CFB, iv)
   etext = obj2.decrypt(data)
   return etext