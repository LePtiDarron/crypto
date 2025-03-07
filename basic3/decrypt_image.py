import itertools
import string
from PIL import Image
import io

def xor_decrypt(encrypted_data, key):
    return bytearray([byte ^ key[i % len(key)] for i, byte in enumerate(encrypted_data)])


def bruteforce_xor(prefix, encrypted_data):
    possible_chars = string.ascii_lowercase 
    for key_length in range(0, 10):
        for key_tuple in itertools.product(possible_chars, repeat=key_length):
            key = prefix + ''.join(key_tuple)
            key_bytes = key.encode('utf-8')
            decrypted_data = xor_decrypt(encrypted_data, key_bytes)
            
            if decrypted_data[:2] != bytearray([66, 77]):
                continue
                
            try:
                with Image.open(io.BytesIO(decrypted_data)) as img:
                    img.load()
                    img.save(f"{key}.bmp")
                    print(f"Clé trouvée : {key}")
                    return 0
            except (IOError, SyntaxError):
                continue
    return 1


with open('ch2.bmp', 'rb') as f:
    encrypted_data = f.read()

prefix = 'gi'

bruteforce_xor(prefix, encrypted_data)