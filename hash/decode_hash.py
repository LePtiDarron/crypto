import itertools
import hashlib
import string

hashed_password = "37f62f1363b04df4370753037853fe88"
possible_chars = string.ascii_lowercase

def bruteforce(min_length=5, max_length=10):
    for length in range(min_length, max_length + 1):
        for guess in itertools.product(possible_chars, repeat=length):
            password = ''.join(guess)
            if hashlib.md5(password.encode()).hexdigest() == hashed_password:
                print(f"Mot de passe trouvé : {password}")
                return
    print("Mot de passe non trouvé.")

bruteforce()
