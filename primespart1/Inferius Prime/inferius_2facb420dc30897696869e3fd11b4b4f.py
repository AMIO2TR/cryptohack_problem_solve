#!/usr/bin/env python3

from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes, GCD

e = 65537
ct = 77578995801157823671636298847186723593814843845525223303932
n = 882564595536224140639625987659416029426239230804614613279163

# n will be 8 * (100 + 100) = 1600 bits strong (I think?) which is pretty good
p = 857504083339712752489993810777
q = 1029224947942998075080348647219
phi = (p - 1) * (q - 1)
d = inverse(e, phi)


ct = pow(ct, d, n)

print(ct)
print (hex(ct))

# print(f"n = {n}")
# print(f"e = {e}")
# print(f"ct = {ct}")

# pt = pow(ct, d, n)
# decrypted = long_to_bytes(pt)
# assert decrypted == FLAG
# print(pt)
