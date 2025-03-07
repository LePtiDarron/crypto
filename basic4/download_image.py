import requests

url = "https://crypto.lucas.zip/basic4.webp"

response = requests.get(url)

if response.status_code == 200:
    with open("basic4.webp", "wb") as file:
        file.write(response.content)
