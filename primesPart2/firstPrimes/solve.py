from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Util.number import inverse
# Read the public key from the PEM file
with open('key.pem', 'rb') as f:
    key = RSA.import_key(f.read())

# Given values of p and q
p = 51894141255108267693828471848483688186015845988173648228318286999011443419469
q = 77342270837753916396402614215980760127245056504361515489809293852222206596161

# Calculate n and the totient
n = p * q
totient = (p - 1) * (q - 1)

# Ciphertext in hexadecimal format
c_hex = "249d72cd1d287b1a15a3881f2bff5788bc4bf62c789f2df44d88aae805b54c9a94b8944c0ba798f70062b66160fee312b98879f1dd5d17b33095feb3c5830d28"
c = bytes.fromhex(c_hex)

# Calculate the private exponent d
d = inverse(key.e, totient)

# Construct the private key
private_key = RSA.construct((n, key.e, d))

# Create the cipher object for decryption
cipher = PKCS1_OAEP.new(private_key)

# Decrypt the ciphertext
plaintext = cipher.decrypt(c)

# Print the plaintext
print(plaintext.decode())
