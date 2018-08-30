# convert cookies from EditThisCookie export format to required format

import json
cookies = {}
with open('cookies_full.json') as cookies_full_file:  
    cookies_full = json.load(cookies_full_file)
    for cookie in cookies_full:
        cookies[cookie['name']] = cookie['value']

with open('cookies.json', 'w') as cookies_file:  
    json.dump(cookies, cookies_file, indent=2)
