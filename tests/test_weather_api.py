from unittest import TestCase

from src.weather_api import get_clima

class TestWeatherApi(TestCase):
    def test_valid_coords(self):
        # Coordenadas válidas
        lat, lon = '25.7785', '-100.107'
        data = get_clima(lat, lon)
        llaves = ["temperatura", "minima", "maxima", "descripcion",
                  "sensacion_termica", "nubes"]
        for key in llaves:
            self.assertIn(key, data.keys(), f"No se encontró la llave {key}")

    def test_invalid_coords(self):
        # Coordenadas no válidas
        lat, lon = '2222222222', '1111111111'
        with self.assertRaises(Exception):
            get_clima(lat, lon)
