import requests

r = requests.get("http://www.geoplugin.net/json.gp")
print(r.status_code)

if r.status_code != 200:
    print("Não foi possível obter a localização")
else:
    print(r.text)
