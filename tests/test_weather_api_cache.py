from unittest import TestCase

from src.pkg.weather_api import WeatherApiCache

class TestWeatherApiCache(TestCase):
    def setUp(self):
        """
        Inicializa lo necesario para realizar los tests
        """
        self.api = WeatherApiCache()
        self.coords = [
                {"latitud": "25.7785", "longitud": "-100.107"},
                {"latitud": "19.4363", "longitud": "-99.0721"},
        ]

    def test_calls(self):
        """
        Revisa que solo se haga una llamada a la api aunque
        se haya obtenido el clima del mismo lugar muchas veces
        """
        for i in range(10):
            for coord in self.coords:
                self.api.get_clima(coord["latitud"], coord["longitud"])
        condition = self.api._calls == len(self.coords)
        self.assertTrue(condition, f"Se realizó más de {len(self.coords)} llamada")

    def test_size(self):
        """
        Revisa que el tamaño del cache no crezca aunque
        se haya obtenido el clima del mismo lugar muchas veces
        """
        for i in range(10):
            for coord in self.coords:
                self.api.get_clima(coord["latitud"], coord["longitud"])
        condition = len(self.api.cache) == len(self.coords)
        self.assertTrue(condition, f"Hay más de {len(self.coords)} entradas en cache")
