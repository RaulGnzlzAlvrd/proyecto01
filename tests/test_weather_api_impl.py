from unittest import TestCase

from src.weather_api import WeatherApiImpl

class TestWeatherApiImpl(TestCase):
    def setUp(self):
        """
        Inicializa lo necesario para ejecutar los tests
        """
        self.api = WeatherApiImpl()

    def test_valid_coords(self):
        """
        Testea coordenadas válidas, se espera que las llaves se
        encuentren dentro del diccionario devuelto
        """
        lat, lon = '25.7785', '-100.107'
        data = self.api.get_clima(lat, lon)
        llaves = ["temperatura", "minima", "maxima", "descripcion",
                  "sensacion_termica", "nubes"]
        for key in llaves:
            self.assertIn(key, data.keys(), f"No se encontró la llave {key}")

    def test_invalid_coords(self):
        """
        Testea coordenadas NO válidas, se espera que lance una
        excepción.
        """
        lat, lon = '2222222222', '1111111111'
        with self.assertRaises(Exception):
            self.api.get_clima(lat, lon)
