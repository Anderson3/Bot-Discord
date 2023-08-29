
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

    req = requests.get('https://api.open-meteo.com/v1/dwd-icon?latitude='+str(lat)+'&longitude='+str(long)+'&hourly=temperature_2m,relativehumidity_2m,windspeed_10m')
    #pprint(req.json())

    humidade_relativa = req.json()['hourly']['relativehumidity_2m'][0]
    temperatura = req.json()['hourly']['temperature_2m'][0]
    horario = req.json()['hourly']['time'][0]
    vento_velocidade = req.json()['hourly']['windspeed_10m'][0]

    #humidade_relativa = req.json()
    #pprint(humidade_relativa)
    #pprint(temperatura)
    #pprint(horario)
    #pprint(vento_velocidade)

    print(f'{city.upper()}, está atualmente com Temperatura de {temperatura}°C, Humidade relativa de {humidade_relativa}% e ventos a {vento_velocidade} km/h.')
    if float(temperatura) > 15:
        print('Essa temperatura é fria pra flamingos.')
    else:
        print('Essa temperatura é quente pra flamingos.')


tempo('são paulo')


def local(city):

    req = requests.get('https://api.api-ninjas.com/v1/geocoding?city='+city, headers={'X-Api-Key': '8zF4dEsOBx4cfzqQ4Pc8Xw==7VukABeFVan7N5R9'})
    cidade = req.json()[0]
    lat, long = cidade['latitude'], cidade['longitude']
    #print(cidade)
    print(lat,long)
    #pprint(req.json())

#local('london')