import itertools
import string
from PIL import Image
import os

def xor_decrypt(encrypted_data, key):
    return bytearray([byte ^ key[i % len(key)] for i, byte in enumerate(encrypted_data)])


def bruteforce_xor(prefix, encrypted_data):
    possible_chars = string.printable
    for key_length in range(0, 10):
        for key_tuple in itertools.product(possible_chars, repeat=key_length):
            key = prefix + ''.join(key_tuple)
            key_bytes = key.encode('utf-8')
            decrypted_data = xor_decrypt(encrypted_data, key_bytes)
            
            if not (decrypted_data[:4] == b'RIFF' and decrypted_data[8:12] == b'WEBP'):
                continue

            with open(f'image.webp', 'wb') as f:
                f.write(decrypted_data)
            try:
                with Image.open(f'image.webp') as img:
                    img.show()
                print(f"Clé trouvée : {key}")
                return 0
            except Exception as e:
                os.remove(f'image.webp')
    return 1


with open('basic4.webp', 'rb') as f:
    encrypted_data = f.read()

prefix = 'w?v=MsQaPR2N'

bruteforce_xor(prefix, encrypted_data)