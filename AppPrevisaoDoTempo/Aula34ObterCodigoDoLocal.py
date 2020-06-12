import requests
import json
import pprint

accuweatherAPIKey = 'TVcI7dWJq2YRDWXarVUqo5YUoRuUEh5P'
r = requests.get("http://www.geoplugin.net/json.gp")
print("Status Code", r.status_code)

if r.status_code != 200:
    print("Não foi possível obter a localização")
else:
    #print(type(json.loads(r.text)))
    localizacao = json.loads(r.text)
    #print(pprint.pprint(localizacao))
    lat = localizacao['geoplugin_latitude']
    long = localizacao['geoplugin_longitude']
    print("Latitude: ", lat)
    print("Longitude: ", long)



location_api_url = "http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey="+accuweatherAPIKey+"&q="+lat+"%2C%20"+long+"&language=pt-br"
r2 = requests.get(location_api_url)
if r2.status_code != 200:
    print("Não foi possível obter a localização")
else:
    locationResponse = json.loads(r2.text)
    print(pprint.pprint(locationResponse))
    nomeLocal = locationResponse['LocalizedName'] + ", " + locationResponse['AdministrativeArea']['LocalizedName'] + ". " + locationResponse['Country']['LocalizedName']
    codigoDoLocal = locationResponse["Key"]

    print("Local: ", nomeLocal)
    print("Codigo do Local: ", codigoDoLocal)

