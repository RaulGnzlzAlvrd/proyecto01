from unittest import TestCase

from src.pkg.weather_api import get_clima

class TestWeatherApiImpl(TestCase):
    def test_valid_coords(self):
        """
        Testea coordenadas válidas, se espera que las llaves se
        encuentren dentro del diccionario devuelto
        """
        lat, lon = '25.7785', '-100.107'
        data = get_clima(lat, lon)
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
            get_clima(lat, lon)
