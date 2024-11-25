from pwn import *
import json
from Crypto.Util.number import long_to_bytes

con = remote('socket.cryptohack.org', 13374)
rec = con.recv(1024)
con.send(json.dumps({"option":"get_pubkey"}))
rec = con.recv(1024)
con.send(json.dumps({"option":"get_secret"}))
rec = con.recv(1024)
secret = json.loads(rec)['secret']
con.send(json.dumps({"option":"sign", 'msg':secret}))
rec = con.recv(1024)
signature = json.loads(rec)['signature']
flag = long_to_bytes(int(signature, 16))
print(flag)