import requests
import json
## import pprint

accuweatherAPIKey = 'TVcI7dWJq2YRDWXarVUqo5YUoRuUEh5P'

def pegarCoordenadas():
    r = requests.get("http://www.geoplugin.net/json.gp")
    if r.status_code != 200:
        print("Não foi possível obter a localização")
        return None
    else:
        try:
            localizacao = json.loads(r.text)
            coordenadas = {}
            coordenadas['lat'] = localizacao['geoplugin_latitude']
            coordenadas['long'] = localizacao['geoplugin_longitude']
            print("Latitude: ", coordenadas['lat'])
            print("Longitude: ", coordenadas['long'])
            return coordenadas
        except:
            return None

def pegarCodigoLocal(lat, long):
    location_api_url = "http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey="+accuweatherAPIKey+"&q="+lat+"%2C%20"+long+"&language=pt-br"
    r = requests.get(location_api_url)
    if r.status_code != 200:
        print("Não foi possível obter o código local")
        return None
    else:
        try:
            locationResponse = json.loads(r.text)
            infoLocal = {}
            infoLocal['nomeLocal'] = locationResponse['LocalizedName'] + ", " + locationResponse['AdministrativeArea']['LocalizedName'] + ". " + locationResponse['Country']['LocalizedName']
            infoLocal['codigoLocal'] = locationResponse["Key"]
            return infoLocal
        except:
            return None


def pegarTempoAgora(codigoLocal, nomeLocal):
    CurrentConditionAPIUrl = "http://dataservice.accuweather.com/currentconditions/v1/"+codigoLocal+"?apikey="+accuweatherAPIKey+"&language=pt-br"
    r = requests.get(CurrentConditionAPIUrl)
    if r.status_code != 200:
        print("Não foi possível obter as condições climáticas")
        return None
    else:
        try:
            current_conditions_response = json.loads(r.text)
            infoClima = {}
            infoClima['textoClima'] = current_conditions_response[0]["WeatherText"]
            infoClima['temperatura'] = current_conditions_response[0]["Temperature"]["Metric"]["Value"]
            infoClima['nomeLocal'] = nomeLocal
            return infoClima
        except:
            return None

## Inicio do Programa
if(__name__ == "__main__"):
    coordenadas = pegarCoordenadas()

    try:
        local = pegarCodigoLocal(coordenadas["lat"], coordenadas["long"])
        climaAtual = pegarTempoAgora(local["codigoLocal"], local["nomeLocal"])
        print("Clima atual em: ", climaAtual['nomeLocal'])
        print(climaAtual['textoClima'])
        print("Temperatura: " + str(climaAtual["temperatura"]) + "\xb0" + "C")
    except:
        print("Não foi possível obter as condições climáticas")



