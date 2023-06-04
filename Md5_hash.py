import  hashlib

md5 = hashlib.md5()

md5.update(b'ptrsfsdfdf')


Encrypted_Data = md5.digest()
Encrypted_Hex_Data = md5.hexdigest()

#
print("This is the encrypted data:" + str(Encrypted_Data))
print("This is the hex encrypted data:" + str(Encrypted_Hex_Data))



