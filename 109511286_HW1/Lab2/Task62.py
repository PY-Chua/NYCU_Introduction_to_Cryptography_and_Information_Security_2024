#!/usr/bin/python3

def xor(first, second, third):
    return bytearray(x ^ y ^ z for x, y, z in zip(first, second, third))
    
P1 = "This is a known message!"
C1 = "a469b1c502c1cab966965e50425438e1bb1b5f9037a4c159"
C2 = "bf73bcd3509299d566c35b5d450337e1bb175f903fafc159"

D1 = bytes(P1, 'utf-8')
D2 = bytearray.fromhex(C1)
D3 = bytearray.fromhex(C2)

P2 = xor(D1, D2, D3)

print('P2 in hex:', P2.hex())
print('P2 in ascii', P2.decode('utf-8'))
