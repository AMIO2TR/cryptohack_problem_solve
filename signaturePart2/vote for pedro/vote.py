from Crypto.Util.number import bytes_to_long
msg = b'VOTE FOR PEDRO'
msg = bytes_to_long(msg)
vote = int(mod(msg, 256**15).nth_root(3))
assert (vote**3) % (256**15) == msg
print(vote)