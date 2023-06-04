import hashlib

Hash = hashlib.sha1('Python'.encode('utf-8')).digest()

print("This is the SHA1 encrypted data: " + str(Hash))