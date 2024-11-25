from Crypto.PublicKey import RSA

# Open the PEM file containing the RSA key
f = open('key.pem', 'r')

# Import the key from the file
key = RSA.import_key(f.read())

# Extract n (modulus) and e (public exponent)
n = key.n
e = key.e

# Print or use n and e as needed
print(f"Modulus (n): {n}")
print(f"Public Exponent (e): {e}")
