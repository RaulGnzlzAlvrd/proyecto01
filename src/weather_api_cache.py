import .weather_api

cache= {}

def get_clima(latitud, longitud):
    llave= (latitud, longitud)
    if llave in cache.keys():
        return cache[llave]
    else: 
        data=weather_api.get_clima(latitud, longitud)
        cache[llave]=data
        return data    