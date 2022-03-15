import pandas as pd 

from .weather_api_cache import WeatherApiCache

class App():
    """
    Representa en más alto nivel la lógica del programa
    """
    def __init__(self):
        self.api = WeatherApiCache()

    def get_clima(self, ticket, site):
        """
        Obtiene el clima, a los campos resultantes les pone como
        prefijo site.

        params:
        ticket: pandas.Series, ticket con las coordenadas
        site: str, El tipo de ciudad ('origin', 'destination')

        returns: pandas.Series, los datos de la ciudad, pero índices
        modificados
        """
        latitud, longitud = [f"{site}_{coord}" for coord in ["latitude", "longitude"]]
        clima = pd.Series(self.api.get_clima(*ticket[[latitud, longitud]]))
        clima.index = site + "_" + clima.index
        return clima

    def process_row(self, row):
        """
        Procesa cada ticket y devuelve la información de
        clima de la ciudad de origen seguida de la ciudad
        de destino.

        params:
        row: pandas.Series, el ticket con las coordenadas 

        return: pandas.Series, la información climática de ambas ciudades
        """
        sites = ["origin", "destination"]
        merge = pd.concat([self.get_clima(row, site) for site in sites])
        return merge

    def run(self):
        """
        Lógica principal del programa:
        - Lee el archivo con los tickets
        - Procesa cada ticket para obtener sus datos
        - Crea el nuevo dataset con la información climatológica
        - Escribe un nuevo archivo .csv con la información
        """
        print("Leyendo .csv")
        tickets = pd.read_csv("./datasets/tickets.csv")
        print("Obteniendo datos de clima")
        datos_clima = tickets.apply(self.process_row, axis=1)
        informe_completo = pd.concat([tickets, datos_clima], axis=1)
        print("Escribiendo archivo de salida")
        informe_completo.to_csv("./datasets/clima.csv")
        print("Listo!")
