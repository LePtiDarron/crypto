from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Util.number import inverse

P = 11901234461494228310064076121482038286429650089208969229876184007349956782094248940290427800597817633601014470221576037327691902428151823981665392121868907

def get_private_key():
    with open("rsa1.pem", "rb") as f:
        key = RSA.import_key(f.read())
    n = key.n
    e = key.e
    
    q = n // P
    phi = (P - 1) * (q - 1)
    d = inverse(e, phi)
    private_key = RSA.construct((n, e, d, P, q))
    return private_key

with open("rsa1Cipher.txt", "rb") as f:
    cipher_text = f.read()

private_key = get_private_key()
cipher_rsa = PKCS1_OAEP.new(private_key)
decrypted_message = cipher_rsa.decrypt(cipher_text)
print(decrypted_message.decode())
