from pwn import *
import json
from Crypto.Util.number import bytes_to_long, long_to_bytes
from sympy import invert

# Set the ADMIN_TOKEN
ADMIN_TOKEN = b"admin=True"

# Convert the ADMIN_TOKEN to an integer (message m0)
m0 = bytes_to_long(ADMIN_TOKEN)
print(f"m0 (ADMIN_TOKEN as integer): {m0}")

# Given RSA parameters
N = 18848009339270098781997226046087638146630394456140158027362415004283209229286050758914353992707611861402774484944507803774933480207279266922245143508147779298027852615761063954226024070610886090241090529547047948571924873219557551997139324940530747494119382360247796307935554051268122290782530541964745224828059859015577419240776934809413466641002835188211126248474972995167843141922523024860281534511733311014555726922450945413218375827206253253406535585651906353522051930550729997074617804381410382012585696912675995103410101766177971245951652123396353211245441454684237941983848766644492880811482100687908692820181
e = 65537  # Common public exponent for RSA

# Connect to the challenge server
r = remote('socket.cryptohack.org', 13376)

# Helper function to receive JSON response from the server
def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

# Helper function to send JSON data to the server
def json_send(hsh):
    request = json.dumps(hsh).encode()
    print(request)  # Debug print of the request
    r.sendline(request)

# Step 1: Get the public key (N, e)
r.recvline()
json_send({"option": "get_pubkey"})
line = json_recv()
print(f"Public Key: {line}")

# Extract N and e
N, e = line["N"], line["e"]
N, e = int(N, 16), int(e, 16)

# Step 2: Sign a dummy message to get the first signature
json_send({"option": "sign", "msg": "02"})  # Sending "02" (as a dummy message)
line = json_recv()
print(f"First signature (c0): {line}")
c0 = int(line["signature"][2:], 16)  # Convert from hex to int
print(f"c0: {c0}")

# Step 3: Perform blinding attack
# Multiply m0 (the integer form of ADMIN_TOKEN) by 2 to "blind" it
m0 = m0 * 2

# Send the blinded message for signing
json_send({"option": "sign", "msg": hex(m0)[2:]})  # Send the blinded message in hex
line = json_recv()
print(f"Blinded signature (c1): {line}")
c1 = int(line["signature"][2:], 16)  # Convert from hex to int
print(f"c1: {c1}")

# Step 4: Forge the signature for the original ADMIN_TOKEN
# Perform the modular inverse to calculate c = c0^(-1) * c1 mod N
c = (invert(c0, N) * c1) % N
# Step 4: Forge the signature for the original ADMIN_TOKEN
# Perform the modular inverse to calculate c = c0^(-1) * c1 mod N
c = (pow(c0, -1, N) * c1) % N
print(f"Forged signature (c): {c}")
print(f"Forged signature (c): {c}")

# Step 5: Verify the forged signature using the server
json_send({
    "option": "verify",
    "msg": hex(bytes_to_long(ADMIN_TOKEN))[2:],  # Send the original ADMIN_TOKEN message
    "signature": hex(c)[2:]  # Send the forged signature
})

# Step 6: Receive and print the server response (flag or error message)
line = json_recv()
print(f"Server response: {line}")

# Closing the connection
r.close()
