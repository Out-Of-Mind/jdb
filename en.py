import crypto, os
from Crypto.Hash import SHA256
path = '/data/data/com.termux/files/usr/var/lib/jdb'

def en(passw):
   lss = os.listdir(path)
   for i in lss:
       with open(path+'/'+i, 'rb') as f:
           data = f.read()
       os.remove(path+'/'+i)
       c = crypto.encrypt(data, passw, 'OF2;9lEvs0r1QY43')
       with open(path+'/'+i+'.aes', 'wb') as f:
           f.write(c)
def de(passw):
    ls = os.listdir(path)
    with open('/data/data/com.termux/files/usr/etc/JDB/.t.txt', 'rb') as f:
        dat = f.read()
    sha = SHA256.new()
    sha.update(passw)
    if dat == sha.digest():
        pass
    else: 
        return 0
    for i in ls:
        if i[-4:] == '.aes':
            with open(path+'/'+i, 'rb') as f:
                data = f.read()
            c = crypto.decrypt(data, passw, 'OF2;9lEvs0r1QY43')
            with open(path+'/'+i[:-4], 'wb') as f:
                f.write(c)
            os.remove(path+'/'+i)
    return 1