import requests


def download_file(name):
    url = "https://crypto.lucas.zip/" + name

    response = requests.get(url)

    if response.status_code == 200:
        with open(name, "wb") as file:
            file.write(response.content)

download_file("rsa1.pem")
download_file("rsa1Cipher.txt")