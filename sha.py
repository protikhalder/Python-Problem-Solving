import hashlib



Hash = hashlib.sha224(b'Pythojn')
encrypted_digest = Hash.digest()
encrypted_Hex = Hash.hexdigest()

print("This digest "+ str(encrypted_digest))
print("This Hex"+ str(encrypted_Hex))