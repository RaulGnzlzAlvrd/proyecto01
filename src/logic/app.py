import pandas as pd 
from weather_api.weather_api_cache import get_clima

def process_row(row):
    o_lat = row["origin_latitude"]
    o_lon = row["origin_longitude"]
    d_lat = row["destination_latitude"]
    d_lon = row["destination_longitude"]
    origen = get_clima(o_lat, o_lon)
    destino = get_clima(d_lat, d_lon)
    merge = list(origen.values()) + list(destino.values())
    return merge

def run():
    print("Leyendo .csv")
    df = pd.read_csv("./datasets/tickets.csv")
    campos = ["descripcion", "temperatura", "minima", "maxima",
              "sensacion_termica", "nubes"]
    campos_origen = [f"origin_{campo}" for campo in campos]
    campos_destino = [f"destination_{campo}" for campo in campos]
    print("Obteniendo datos de clima")
    df[campos_origen + campos_destino] = df.apply(process_row, axis=1, result_type="expand")
    print("Escribiendo archivo de salida")
    df.to_csv("./datasets/clima.csv")
    print("Listo!")
