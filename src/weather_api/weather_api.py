import requests
import os
from dotenv import load_dotenv
load_dotenv()

def get_clima(latitud, longitud):
    """
    Funcion que hace la peticion get a openweather, obtiene el 
    clima de la ubicacion con la latitud y longitud pasada como 
    parametro
    params: latitud y longitud para hacer la peticion 
    return: Los datos de la peticion a openweather
    """
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
    """
    Funcion que da un formato en español a los datos devueltos en la peticion get aponeweather
    params: Datos en un diccionario
    return: Diccionario con la informacion modificada 
    """
    clean_data = {}
    clean_data['descripcion'] = data['weather'][0]['description']
    clean_data['temperatura'] = data['main']['temp']
    clean_data['minima'] = data['main']['temp_min']
    clean_data['maxima'] =  data['main']['temp_max']
    clean_data['sensacion_termica'] = data['main']['feels_like']
    clean_data['nubes']= data['clouds']['all']
    return clean_data 
