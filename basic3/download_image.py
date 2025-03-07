import requests

url = "https://crypto.lucas.zip/ch2.bmp"

response = requests.get(url)

if response.status_code == 200:
    with open("ch2.bmp", "wb") as file:
        file.write(response.content)
