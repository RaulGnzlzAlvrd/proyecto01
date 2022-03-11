import pandas as pd 
from .weather_api_cache import get_clima

def process_row(row):
    o_lat = row["origin_latitude"]
    o_lon = row["origin_longitude"]
    d_lat = row["destination_latitude"]
    d_lon = row["destination_longitude"]
    origen = get_clima(o_lat, o_lon)
    destino = get_clima(d_lat, d_lon)
    print(origen, destino)

df = pd.read_csv("./datasets/tickets.csv")
df.apply(process_row, axis=1)
