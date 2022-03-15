from .weather_api import get_clima as get_clima_origin

class weatherApiCache:
    """
    Consulta la api usando el cache, eliminando consultas duplicadas.
    """
    def __init__ (self):
        self.cache = {}

  
    def get_clima(self, latitud, longitud):
        """
        Función para obtener datos del clima a partir de la latitud y longitud.
        """
        llave= (latitud, longitud)
        if llave in self.cache.keys():
            return self.cache[llave]
        else: 
            data= get_clima_origin(latitud, longitud)
            self.cache[llave]=data
            return data    
