from pwn import remote
import json

# Connect to the server
r = remote('socket.cryptohack.org', 13376)

# Receive the initial message from the server (optional)
print(r.recv())

# Send the 'get_pubkey' option to request N and E
request = {"option": "get_pubkey"}
r.sendline(json.dumps(request).encode())

# Receive the server's response
response = r.recvline()
response_json = json.loads(response.decode())

# Extract N and E from the server response
N = int(response_json["N"], 16)  # Convert from hex to int
E = int(response_json["e"], 16)  # Convert from hex to int

# Print the extracted values
print(f"N (modulus): {N}")
print(f"E (public exponent): {E}")

# Close the connection
r.close()
