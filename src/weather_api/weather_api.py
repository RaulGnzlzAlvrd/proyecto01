import requests
import os
from dotenv import load_dotenv
load_dotenv()

def get_clima(latitud, longitud):
    apiKey = os.environ['APIKEY']
    params = {
        'lat':latitud,
        'lon':longitud,
        'appid':apiKey,
        'units':'metric',
        'lang': 'sp'
    }
    response = requests.get('https://api.openweathermap.org/data/2.5/weather', params=params)
    if response.status_code == 400:
        raise Exception('Parametros no validos')
    return clean_response(response.json())


def clean_response(data):
    clean_data = {}
    clean_data['descripcion'] = data['weather'][0]['description']
    clean_data['temperatura'] = data['main']['temp']
    clean_data['minima'] = data['main']['temp_min']
    clean_data['maxima'] =  data['main']['temp_max']
    clean_data['sensacion_termica'] = data['main']['feels_like']
    clean_data['nubes']= data['clouds']['all']
    return clean_data 
