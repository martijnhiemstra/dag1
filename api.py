print('Start api read application')

import requests

paginaresults = requests.get('https://catfact.ninja/facts')
print(paginaresults)

feitjes = paginaresults.json()

eerstefeitje = feitjes["data"][0]["fact"]
print(eerstefeitje)
