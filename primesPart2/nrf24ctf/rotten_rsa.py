from flag import flag, e, n
from Crypto.Util.number import bytes_to_long as btl, getPrime, isPrime

def rotten(x):
    bit = x.bit_length()
    return (1 << bit) - 1 ^ x 

def encrypt(n):
    while 1:
        p = getPrime(n)  
        q = rotten(p) + 65537 
        if isPrime(q): 
            return p, q 
assert e % 2 == 1

p, q = encrypt(n)  
n = p * q 
c = pow(btl(flag), e, n)

print('n =', n)
print('c =', c)
