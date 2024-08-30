import os
import pandas as pd

# Directorio de entrada donde se encuentran los archivos
input_directory = 'LAND_SURFACE_TEMPERATURE_2023'
# Directorio donde se guardarán las carpetas 1 a 63
cuadrantes_directory = 'Cuadrantes'
in_path = 'LAND_SURFACE'


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

# Obtener una lista de archivos en el directorio de entrada
files = [f for f in os.listdir(input_directory) if os.path.isfile(os.path.join(input_directory, f))]

# Convertir las llaves en una lista para facilitar el acceso
keys = list(mi_diccionario.keys())
sorted_file = sorted(files)
# Contador para los archivos generados

file_counter = 1

# Iterar sobre los archivos
for file in sorted_file:
    file_path = os.path.join(input_directory, file)
    
    file_dir = 1
    # Cargar el archivo CSV
    data = pd.read_csv(file_path)

    # Convertir la columna 'lat/lon' a valores numéricos
    data['lat/lon'] = pd.to_numeric(data['lat/lon'], errors='coerce')
    
    # Iterar sobre las llaves en pares
    for i in range(len(keys) - 1):
        key1 = keys[i]
        key2 = keys[i + 1]
        
        # Iterar sobre los elementos de los dos identificadores en pares solapados
        for j in range(len(mi_diccionario[key1]) - 1):
            elem1_key1 = mi_diccionario[key1][j]
            elem2_key1 = mi_diccionario[key1][j + 1]
            elem1_key2 = mi_diccionario[key2][j]
            elem2_key2 = mi_diccionario[key2][j + 1]

            # Definir los rangos de latitud y longitud
            lat_min = key1
            lat_max = key2
            lon_min = elem1_key1
            lon_max = elem2_key2

            # Filtrar las filas que caen dentro del rango de latitud
            filtered_data = data[(data['lat/lon'] >= lat_min) & (data['lat/lon'] <= lat_max)]

            # Filtrar las columnas que caen dentro del rango de longitud
            lon_columns = [col for col in data.columns if col != 'lat/lon' and lon_min <= float(col) <= lon_max]
            filtered_data = filtered_data[['lat/lon'] + lon_columns]

            # Directorio de salida
            output_directory = os.path.join(cuadrantes_directory, str(file_dir))
            if not os.path.exists(output_directory):
                os.makedirs(output_directory)

            # Nombre del archivo de salida
            output_file_path = os.path.join(output_directory, in_path, f'{in_path}_{file_counter}.csv')

            # Guardar los datos filtrados en un nuevo archivo CSV
            filtered_data.to_csv(output_file_path, index=False)

            # Incrementar el contador
            file_dir += 1 
            # Detener si el contador supera 63
            if file_dir > 63:
                break
        
        # Detener si el contador supera 63
        if file_dir > 63:
            break
    file_counter += 1