#!/usr/bin/python3

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

P = b"This is a top secret."
C = bytes.fromhex("764aa26b55a4da654df6b19e4bce00f4ed05e09346fb0e762583cb7da2ac93a2")
IV = bytes.fromhex("aabbccddeeff00998877665544332211")

assert len(P) == 21

with open('words.txt') as file:
    keys = [line.strip().encode('utf-8') for line in file]

padded_P = pad(P, 16)

for k in keys:
    if len(k) <= 16:
        key = k.ljust(16, b'#')
        cipher = AES.new(key=key, mode=AES.MODE_CBC, iv=IV)
        guess = cipher.encrypt(padded_P)
        if guess == C:
            print("Key found:", key.decode('utf-8'))
            exit(0)

print("Key not found.")
