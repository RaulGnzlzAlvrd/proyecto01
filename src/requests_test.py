from open_weather_api import get_weather

# Codigo iata válido
data = get_weather("MXN")
assert "weather" in data.keys() and "main" in data.keys(), "No se encontró la llave weather o main"

data = get_weather("TLC")
assert "weather" in data.keys() and "main" in data.keys(), "No se encontró la llave weather o main"

# Codigo iata inválido
data = get_weather("holamundo")
assert "weather" not in data.keys() and "main" not in data.keys(), "Campos weather o main presentes y no deberían estar"
