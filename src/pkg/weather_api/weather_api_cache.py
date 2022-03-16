from .weather_api import get_clima as get_clima_origin

class WeatherApiCache:
    """
    Consulta la api usando el cache, eliminando consultas duplicadas.
    """
    def __init__ (self):
        self.cache = {}
        self._calls = 0
  
    def get_clima(self, latitud, longitud):
        """
        Función para obtener datos del clima a partir de la latitud y longitud.
        """
        llave= (latitud, longitud)
        if llave in self.cache.keys():
            return self.cache[llave]
        else: 
            data = get_clima_origin(latitud, longitud)
            self.cache[llave]=data
            self._calls += 1
            return data    
