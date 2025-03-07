import base64

cookie = "{'admin': 0, 'password': '1234', 'username': 'vivi'}"
token_b64 = "Q01pZXV4VW5JVlJhbmRvbbBNVUWTyb3i9ih6TPY9Ovoo5fVrPFYcVC4rtwbrNTYWpnuRukhXjtfF9/D0T+oEjyqZaakvWT/eBPcJ3gqlmKY="
token_bytes = bytearray(base64.b64decode(token_b64))

iv = token_bytes[:16]
ciphertext = token_bytes[16:]

iv[10] = iv[10] ^ ord('0') ^ ord('1')
new_token = base64.b64encode(bytes(iv) + ciphertext).decode()

print(f"New token : {new_token}")


"""
BFS{3ll3_S0n1_0u_lé_P1l_v1t3_v1t3_1_H4V_N33D5!}
"""
