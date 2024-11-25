from pwn import *
from json import *

def send(hsh):
    return r.sendline(dumps(hsh).encode())

option = {
    'option': 'get_flag'
}
r = connect('socket.cryptohack.org', 13386)
r.recv()

enc = []
padding = []
n = 0
e = 11
send(option)
get1 = loads(r.recvuntil('}'))
enc.append(get1['encrypted_flag'])
padding.append(get1['padding'])

send(option)
get2 = loads(r.recvuntil('}'))
enc.append(get2['encrypted_flag'])
padding2 = get2['padding']
padding.append(get2['padding'])
assert get1['modulus'] == get2['modulus']
n = get1['modulus']

print(f'{enc = }')
print(f'{padding = }')
print(f'{n = }')
print(f'{e = }')