from glob import glob
from math import gcd
from Crypto.PublicKey import RSA

# Gather all RSA moduli from .pem files
moduli = [RSA.import_key(open(f_name, 'r').read()).n for f_name in glob("*.pem")]

# Load the vulnerable key
vuln_key = RSA.import_key(open("21.pem", 'r').read())
n = vuln_key.n
e = vuln_key.e

# Print out the loaded moduli for debugging
print("Moduli found:")
for m in moduli:
    print(m)

# Find the greatest common divisor with the moduli
common_factors = [gcd(n, m) for m in moduli]

# Ensure that we found common factors
if common_factors:
    p = max(common_factors)  # Choose the largest common factor
    q = n // p  # Calculate q
    print(f"p: {p}")
    print(f"q: {q}")
else:
    raise ValueError("No common factors found with the given moduli.")
