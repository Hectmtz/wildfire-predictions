import pandas as pd

# Diccionario con los pares de latitudes y longitudes
mi_diccionario = {
    21.0: [-102.5, -102.0, -101.5, -101.0, -100.5, -100.0, -99.5, -99.0, -98.5, -98.0], 
    21.5: [-102.5, -102.0, -101.5, -101.0, -100.5, -100.0, -99.5, -99.0, -98.5, -98.0],
    22.0: [-102.5, -102.0, -101.5, -101.0, -100.5, -100.0, -99.5, -99.0, -98.5, -98.0],
    22.5: [-102.5, -102.0, -101.5, -101.0, -100.5, -100.0, -99.5, -99.0, -98.5, -98.0],
    23.0: [-102.5, -102.0, -101.5, -101.0, -100.5, -100.0, -99.5, -99.0, -98.5, -98.0],
    23.5: [-102.5, -102.0, -101.5, -101.0, -100.5, -100.0, -99.5, -99.0, -98.5, -98.0],
    24.0: [-102.5, -102.0, -101.5, -101.0, -100.5, -100.0, -99.5, -99.0, -98.5, -98.0],
    24.5: [-102.5, -102.0, -101.5, -101.0, -100.5, -100.0, -99.5, -99.0, -98.5, -98.0]
}

# Cargar el archivo fire_nrt
fire_nrt = pd.read_csv('./FIRE_DATA_2023/fire_nrt_M-C61_468944.csv')

# Asegurarse de que las fechas están en formato datetime
fire_nrt['acq_date'] = pd.to_datetime(fire_nrt['acq_date'])

# Convertir las llaves en una lista para facilitar el acceso
keys = list(mi_diccionario.keys())

# Iterar sobre las llaves en pares para recorrer cada cuadrante
cuadrante_num = 1
for i in range(len(keys) - 1):
    key1 = keys[i]
    key2 = keys[i + 1]
    
    # Iterar sobre los elementos de los dos identificadores en pares solapados
    for j in range(len(mi_diccionario[key1]) - 1):
        elem1_key1 = mi_diccionario[key1][j]
        elem2_key1 = mi_diccionario[key1][j + 1]
        elem1_key2 = mi_diccionario[key2][j]
        elem2_key2 = mi_diccionario[key2][j + 1]

        # Definir los rangos de latitud y longitud para el cuadrante
        lat_min = key1
        lat_max = key2
        lon_min = elem1_key1
        lon_max = elem2_key2

        # Cargar el dataset correspondiente al cuadrante
        dataset_path = f'dataset_completo_{cuadrante_num}.csv'
        dataset_completo = pd.read_csv(dataset_path)
        
        # Asegurarse de que las fechas están en formato datetime
        dataset_completo['date'] = pd.to_datetime(dataset_completo['date'])
        
        # Crear una nueva columna para almacenar los conteos de incendios
        dataset_completo['fire_count'] = 0

        # Iterar sobre cada fila del dataset_completo
        for k in range(len(dataset_completo) - 1):
            # Definir el rango de fechas (desde la fecha actual hasta la fecha de la siguiente fila)
            start_date = dataset_completo.loc[k, 'date']
            end_date = dataset_completo.loc[k + 1, 'date']
            
            # Filtrar los incendios que caen dentro de este rango de fechas y en el cuadrante actual
            incendios_en_rango = fire_nrt[
                (fire_nrt['acq_date'] >= start_date) & 
                (fire_nrt['acq_date'] < end_date) & 
                (fire_nrt['latitude'] >= lat_min) & 
                (fire_nrt['latitude'] < lat_max) & 
                (fire_nrt['longitude'] >= lon_min) & 
                (fire_nrt['longitude'] < lon_max)
            ]
            
            # Contar los incendios en el rango de fechas y en el cuadrante
            conteo = len(incendios_en_rango)
            
            # Asignar el conteo a la columna fire_count en la fila actual
            dataset_completo.at[k, 'fire_count'] = conteo
        
        # Guardar el dataset con la nueva columna
        output_file = f'./datasets_finales/dataset_completo_{cuadrante_num}_con_conteo.csv'
        dataset_completo.to_csv(output_file, index=False)
        
        print(f"Archivo actualizado: {output_file}")
        
        # Incrementar el número de cuadrante
        cuadrante_num += 1