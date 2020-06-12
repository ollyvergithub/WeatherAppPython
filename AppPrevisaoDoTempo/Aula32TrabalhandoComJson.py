import requests
import json
import pprint

r = requests.get("http://www.geoplugin.net/json.gp")
print("Status Code", r.status_code)

if r.status_code != 200:
    print("Não foi possível obter a localização")
else:
    print(type(json.loads(r.text)))
    localizacao = json.loads(r.text)
    print(pprint.pprint(localizacao))
    lat = localizacao['geoplugin_latitude']
    long = localizacao['geoplugin_longitude']
    print("Latitude: ", lat)
    print("Longitude: ", long)