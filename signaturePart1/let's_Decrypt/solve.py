from pwn import *
from json import *
from Crypto.Util.number import bytes_to_long
from pkcs1 import emsa_pkcs1_v15

def send(hsh):
    return r.sendline(dumps(hsh))

def convert(txt):
    return int(txt, 16)

r = remote('socket.cryptohack.org', 13391)
print(r.recv())

option = {
    'option': 'get_signature'
}
send(option)
get = loads(r.recv())
N, e, s = get["N"], get["e"], get["signature"]
N, e, s = convert(N), convert(e), convert(s)

msg = 'I am Mallory, I own CryptoHack.org'
left = emsa_pkcs1_v15.encode(msg.encode(), 256)
left = bytes_to_long(left)
e = 1
n = s - left
assert left%n == s%n

option = {
    'option': 'verify',
    'msg': msg,
    'N': hex(n),
    'e': hex(e),
}
send(option)
get = loads(r.recv())
flag = (get['msg'].split(':'))[1]
print(flag)