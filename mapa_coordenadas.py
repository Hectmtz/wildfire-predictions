import numpy as np

#Limites del cuadrante de San Luis Potosi
lat_min, lat_max = 21.0, 24.5
lon_min, lon_max = -102.5, -98.0

#Realizar registro cada 0.5 grados.
paso = 0.5

#Crea matrices con las coordenadas
latitudes = np.arange(lat_min, lat_max + paso, paso)
longitudes = np.arange(lon_min, lon_max + paso, paso)

diccionario_coordenadas = {}

#Llena el diccionario con las latitudes y longitudes
for lat in latitudes:
    diccionario_coordenadas[lat] = list(longitudes)

print(diccionario_coordenadas)