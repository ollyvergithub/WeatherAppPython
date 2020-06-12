# Aula 30 Requisições HTTP

import requests

r = requests.get("https://www.google.com")
print(r.status_code)
print(r.headers)
print(r.text)




