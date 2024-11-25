from functools import reduce
from pwn import *
import json
from Crypto.Util.number import *

p = 1 << 768
PRIMES = [...] # TODO change this to a list containing the first 1000 primes

product = lambda a: reduce(lambda x, y: x * y, a)

rem = remote("socket.cryptohack.org", 13394)
rem.recvline()

rem.sendline(json.dumps({"option": "get_signature"}))
signature = int(json.loads(rem.recvline().decode().strip())['signature'], 16)

def get_order(num, n, o):
    order = 1
    for p in PRIMES:
        if pow(num, o // p, n) != 1:
            order *= p

    for m in range(mul):
        if pow(num, prod * (prod + 1) ** m, n) == 1:
            order *= (prod + 1) ** (m - 1)
            break

    return order

prod = 1
for p in PRIMES:
    prod *= p
    q = prod + 1
    if not isPrime(q) or GCD(signature, q) > 1:
        continue

    mul = 0
    n = 1
    while n <= signature:
        mul += 1
        n *= q
    assert n == q ** mul

    o = prod * q ** (mul - 1) # order of the multiplicative group mod n, i.e. totient(n)
    oo = product(p if pow(signature, o // p, n) == 1 else 1 for p in PRIMES + [q])
    print(p, mul, oo)