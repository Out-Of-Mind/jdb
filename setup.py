import os
from Crypto.Hash import SHA256
sha = SHA256.new()
passw = input('enter password to your database: ')
if not input('re-enter password: ') == passw:
    print('incorrect password, try again')
    passw = input('enter password to your database: ')
if not len(passw) == 16:
    print('password must be 16 characters long')
    exit()
os.mkdir('/data/data/com.termux/files/usr/var/lib/jdb')
os.mkdir('/data/data/com.termux/files/usr/etc/JDB')
with open('/data/data/com.termux/files/usr/etc/JDB/.t.txt', 'wb') as f:
    f.write(sha.digest())