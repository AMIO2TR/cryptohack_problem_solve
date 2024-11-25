#!/usr/bin/env python3

from Crypto.Util.number import bytes_to_long, long_to_bytes
from Crypto.PublicKey import RSA  # Use PyCryptodome to generate RSA keys
from utils import listener


class Challenge():
    def __init__(self):
        self.before_input = "Welcome to my signing server. You can get_pubkey, get_secret, or sign.\n"
        
        # Generate RSA key pair (N, e, d)
        key = RSA.generate(2048)  # Generates an RSA key pair of 2048 bits
        self.N = key.n  # Modulus
        self.E = key.e  # Public exponent
        self.D = key.d  # Private exponent

    def challenge(self, your_input):
        if 'option' not in your_input:
            return {"error": "You must send an option to this server"}

        elif your_input['option'] == 'get_pubkey':
            return {"N": hex(self.N), "e": hex(self.E)}

        elif your_input['option'] == 'get_secret':
            SECRET_MESSAGE = b"Your secret message here"
            secret = bytes_to_long(SECRET_MESSAGE)
            return {"secret": hex(pow(secret, self.E, self.N))}

        elif your_input['option'] == 'sign':
            msg = int(your_input['msg'], 16)
            return {"signature": hex(pow(msg, self.D, self.N))}

        else:
            return {"error": "Invalid option"}


import builtins; builtins.Challenge = Challenge  # hack to enable challenge to be run locally
listener.start_server(port=13374)
