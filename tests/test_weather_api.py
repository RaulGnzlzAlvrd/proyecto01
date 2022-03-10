from unittest import TestCase

from src.open_weather_api import get_weather

class TestWeatherApi(TestCase):
    def test_valid_code(self):
        # Codigo iata válido
        data = get_weather("MXN")
        condition = "weather" in data.keys()
        condition = condition and "main" in data.keys()
        self.assertEqual(True, condition,
                         "No se encontó la llave weather o main")

    def test_valid_code_2(self):
        data = get_weather("TLC")
        condition = "weather" in data.keys()
        condition = condition and "main" in data.keys()
        self.assertEqual(True, condition,
                         "No se encontó la llave weather o main")

    def test_invalid_code(self):
        # Codigo iata inválido
        data = get_weather("holamundo")
        condition = "weather" not in data.keys()
        condition = condition and "main" not in data.keys()
        self.assertEqual(True, condition,
                         "Campos weather o main presentes, no deberían estar")
