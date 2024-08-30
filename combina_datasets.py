import pandas as pd
import os

#Lista de fechas de de las tomas de cada 8 dias.
date = [
    '2023-01-01', '2023-01-09', '2023-01-17', '2023-01-25', '2023-02-02', '2023-02-10',
    '2023-02-18', '2023-02-26', '2023-03-06', '2023-03-14', '2023-03-22', '2023-03-30',
    '2023-04-07', '2023-04-15', '2023-04-23', '2023-05-01', '2023-05-09', '2023-05-17',
    '2023-05-25', '2023-06-02', '2023-06-10', '2023-06-18', '2023-06-26', '2023-07-04',
    '2023-07-12', '2023-07-20', '2023-07-28', '2023-08-05', '2023-08-13', '2023-08-21',
    '2023-08-29', '2023-09-06', '2023-09-14', '2023-09-22', '2023-09-30', '2023-10-08',
    '2023-10-16', '2023-10-24', '2023-11-01', '2023-11-09', '2023-11-17', '2023-11-25',
    '2023-12-03', '2023-12-11', '2023-12-19', '2023-12-27'
]

#Conversion de las fechas a dataframe
date_dataframe = pd.DataFrame(date, columns=['date'])
ruta_base = './Cuadrantes/'

for i in range(1, 64):

    carpeta = str(i)
    land_surface = pd.read_csv(os.path.join(ruta_base, carpeta, 'LAND_SURFACE', 'promedios.csv'))
    ndvi = pd.read_csv(os.path.join(ruta_base, carpeta, 'NDVI', 'promedios.csv'))
    precipitacion = pd.read_csv(os.path.join(ruta_base, carpeta, 'PRECIPITATION', 'promedios.csv'))
    water_vapor = pd.read_csv(os.path.join(ruta_base, carpeta, 'WATER_VAPOR', 'promedios.csv'))

    #Los archivos de ndvi se registran cada 16 dias, por lo que se repiten 2 veces para que coincidan la cantidad de datos.
    ndvi_procesado = ndvi.reindex(ndvi.index.repeat(2)).reset_index(drop=True)

    #Los archivos de precipitacion se registran cada mes, por lo que se repiten 3-4 veces para que coincidan la cantidad de datos.
    indices_a_repetir = [3, 9]

    # Crear un DataFrame vacío para almacenar el resultado
    precipitacion_procesado = pd.DataFrame()

    #Itera sobre cada índice de la informacion de precipitacion.
    for i in range(len(precipitacion)):
        #Repite el dato 3 veces
        if i in indices_a_repetir:
            precipitacion_procesado = pd.concat([precipitacion_procesado, precipitacion.iloc[[i]].reindex(precipitacion.iloc[[i]].index.repeat(3))])
        #Repite el dato 4 veces
        else:
            precipitacion_procesado = pd.concat([precipitacion_procesado, precipitacion.iloc[[i]].reindex(precipitacion.iloc[[i]].index.repeat(4))])

    #Cambia el nombre de las columnas y lo guarda en un archivo.
    precipitacion_procesado = precipitacion_procesado.reset_index(drop=True)
    dataset_completo = pd.concat([date_dataframe, land_surface['Promedio'], ndvi_procesado['Promedio'], precipitacion_procesado['Promedio'], water_vapor['Promedio']], axis=1)
    dataset_completo.columns=['date','land_surface','ndvi','precipitation','water_vapor']

    output_file = f'datasets_combinados/dataset_combinado_{carpeta}.csv'
    dataset_completo.to_csv(output_file, index=False)