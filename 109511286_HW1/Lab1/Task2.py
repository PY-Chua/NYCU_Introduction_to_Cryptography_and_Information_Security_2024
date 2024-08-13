from Crypto.Cipher import AES

plaintext = bytes.fromhex("255044462d312e350a25d0d4c5d80a34")
ciphertext = bytes.fromhex("d06bf9d0dab8e8ef880660d2af65aa82")
IV = bytes.fromhex("09080706050403020100A2B2C2D2E2F2")

with open('key.txt', 'r') as f:
    keys = f.readlines()

for k in keys:
    key = bytes.fromhex(k.strip())
    cipher = AES.new(key, AES.MODE_CBC, IV)
    encrypted = cipher.encrypt(plaintext)
    if ciphertext == encrypted[:len(ciphertext)]:
        print("Match found")
        print("key:", k.strip())
        print("Ciphertext:", ciphertext.hex())
        print("Encrypted:", encrypted.hex())
