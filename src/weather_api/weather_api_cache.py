from .weather_api import get_clima as get_clima_origin

cache= {}

def get_clima(latitud, longitud):
    llave= (latitud, longitud)
    if llave in cache.keys():
        return cache[llave]
    else: 
        data= get_clima_origin(latitud, longitud)
        cache[llave]=data
        return data    
