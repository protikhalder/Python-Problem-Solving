import  hashlib

filename_write_something = input("Enter something : ")
Hash = hashlib.sha256(b'filename_write_something').hexdigest()

with open('filename', 'wb') as f:
    f.write(Hash)
