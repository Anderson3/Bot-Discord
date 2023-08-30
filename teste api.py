
from pprint import pprint
import requests
from pexels_api import API
import random
PEXELS_API_KEY = 'CKyCRJGQrSmOYHVcCr2HqvSUOWVViZRDYBRHb4ppBPGgOcBcRYSmZZm0'



def imagem(*args):
    print(args)
    '''
    p_api = API(PEXELS_API_KEY)
    p_api.search('flamingo', page=random.randint(0,5), results_per_page=10)
    photos = p_api.get_entries()

    photo = photos[random.randint(0,9)]
    print('Photographer: ', photo.photographer)
    print('Photo original size: ', photo.original)
    '''
#imagem('carro andado')


def tempo(*args):
    city = args[0]
    req = requests.get('https://api.api-ninjas.com/v1/geocoding?city='+city, headers={'X-Api-Key': '8zF4dEsOBx4cfzqQ4Pc8Xw==7VukABeFVan7N5R9'})
    cidade = req.json()[0]
    lat, long = cidade['latitude'], cidade['longitude']

    req = requests.get('https://api.open-meteo.com/v1/dwd-icon?latitude='+str(lat)+'&longitude='+str(long)+'&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m')
    pprint(req.json())

    humidade_relativa = req.json()['hourly']['relativehumidity_2m'][0]
    temperatura = req.json()['hourly']['temperature_2m'][0]
    horario = req.json()['hourly']['time'][0]
    vento_velocidade = req.json()['hourly']['windspeed_10m'][0]

    #humidade_relativa = req.json()
    #pprint(humidade_relativa)
    #pprint(temperatura)
    #pprint(horario)
    #pprint(vento_velocidade)
    '''
    print(f'{city.upper()}, está atualmente com Temperatura de {temperatura}°C, Humidade relativa de {humidade_relativa}% e ventos a {vento_velocidade} km/h.')
    if float(temperatura) > 15:
        print('Essa temperatura é fria pra flamingos.')
    else:
        print('Essa temperatura é quente pra flamingos.')
    '''


#tempo('parnaíba')


def local(city):

    req = requests.get('https://api.api-ninjas.com/v1/geocoding?city='+city, headers={'X-Api-Key': '8zF4dEsOBx4cfzqQ4Pc8Xw==7VukABeFVan7N5R9'})
    cidade = req.json()[0]
    lat, long = cidade['latitude'], cidade['longitude']
    #print(cidade)
    print(lat,long)
    #pprint(req.json())

#local('london')



def tempo(cidade):
    API_TEMPO = 'ec5eb2abed5765d5372423e4d3a0cdfa'
    req = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+cidade+"&appid="+API_TEMPO+"&lang=pt_br")
    'https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}'
    pprint(req.json())

    try:
        cidade = req.json()['name']
        termica_sensacao = int(req.json()['main']['feels_like'] - 273.15)
        temperatura = int(req.json()['main']['temp'] - 273.15)
        max_temperatura = int(req.json()['main']['temp_max'] - 273.15)
        min_temperatura = int(req.json()['main']['temp_min'] - 273.15)

        condicao_tempo = req.json()['weather'][0]['description']
        velocidade_vento = req.json()['wind']['speed']
        angulo_vento = req.json()['wind']['deg']

        print(f'{cidade.upper()} está atualmente com temperatura de {temperatura}°C (máxim: {max_temperatura}°C, e mínima: {min_temperatura}°C). A sensação térmica é de {termica_sensacao}°C, e as condições do tempo é {condicao_tempo}, com ventos de {velocidade_vento}Km/h a {angulo_vento} graus.')
    
    except Exception as error:
        print('Erro: ', error)
        print('Infelizmente não foi possível verificar essa cidade no momento. Verifique se o nome da cidade está correto, meu nobre.')

#tempo('Londres')


import json
import requests
import pprint
import base64

url = 'https://api.gotit.ai/NLU/v1.5/Analyze'
data = {"T":"Victor comeu uma pizza deliciosa.","S":true}
data_json = json.dumps(data)
userAndPass = base64.b64encode(b"#APIKey_Identifier#:#APIKey_Secret#").decode("ascii")
headers = {'Content-type': 'application/json', "Authorization": "Basic %s" %  userAndPass}
response = requests.post(url, data=data_json, headers=headers)
pprint.pprint(response.json())