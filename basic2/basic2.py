'''
L'énoncé de cet exercice est en hexadécimal, il suffit juste de le convertir en ASCII
'''

hex_string = "57656c6c20646f6e6520212054686520666c616720666f722074686973206368616c6c656e67652069732074686973206d6573736167652e"
decrypted_message = bytes.fromhex(hex_string).decode("ASCII")

print(decrypted_message)
