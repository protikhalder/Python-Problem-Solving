import hashlib

# print(hashlib.algorithms_available)

Hash = hashlib.shake_128(b'hash world')
Hash2 = hashlib.shake_256(b'World')
print(Hash)
print(Hash2)

x  = Hash.digest(12)
y = Hash2.digest(22)
print(x)
print(y)

hex_shake = Hash.hexdigest(10)

print(hex_shake)