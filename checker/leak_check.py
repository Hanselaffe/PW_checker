import requests
import hashlib

def check_leak(password, use_custom_api=False, custom_api_key=''):
    if use_custom_api and custom_api_key:
        return check_leak_custom_api(password, custom_api_key)
    else:
        return check_leak_hibp(password)

def check_leak_hibp(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    
    url = f"https://api.pwnedpasswords.com/range/{first5_char}"
    response = requests.get(url)
    
    hashes = (line.split(':') for line in response.text.splitlines())
    for h, count in hashes:
        if h == tail:
            return f"This password has been seen {count} times before."
    
    return "This password has not been found in known leaks."

def check_leak_custom_api(password, api_key):
    url = f"https://leakcheck.net/api/v1?key={api_key}&check={password}&type=password"
    response = requests.get(url)
    result = response.json()

    if result['success']:
        if result['found']:
            return f"This password has been seen {result['count']} times before."
        else:
            return "This password has not been found in known leaks."
    else:
        return "Error checking password leaks with custom API."
