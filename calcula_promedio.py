import pandas as pd
import os
import re

def procesa_csv(directorio_archivo):
    #Cargar el archivo CSV
    df = pd.read_csv(directorio_archivo)
    
    #Elimina la primera columna y la primera fila
    limpiar_df = df.iloc[1:, 1:]
    
    #Calcula el promedio de los datos restantes
    valor_promedio = limpiar_df.mean().mean()
    
    return valor_promedio

def extraer_numero(nombre_archivo):
    #Busca si la coincidencia con la expresion regular para saber el numero del archivo
    coincide = re.search(r'(\d+)', nombre_archivo)
    return int(coincide.group(1)) if coincide else float('inf')

#Directorio principal
directorio_principal = './Cuadrantes/'

#Recorre todos los subdirectorios y archivos de Cuadrantes
for actual, dirs, archivos in os.walk(directorio_principal):
    #Almacenar los promedios de un directorio específico
    resultado = []
    
    #Para cada archivo del directorio valida que existen archivos csv y despues calcula el promedio
    for archivo in archivos:
        if archivo.endswith(".csv"):
            directorio_archivo = os.path.join(actual, archivo)
            promedio = procesa_csv(directorio_archivo)
            #Guarda el nombre del archivo y su promedio
            resultado.append({'Archivo': archivo, 'Promedio': promedio})
    
    #Si se encontraron archivos CSV, ordenar y guardar los promedios en un archivo en ese directorio
    if resultado:
        # Convierte la lista de resultados a un DataFrame
        resultado_df = pd.DataFrame(resultado)
        
        #Ordena el DataFrame por el nombre
        resultado_df['Numero'] = resultado_df['Archivo'].apply(extraer_numero)
        resultado_df = resultado_df.sort_values(by='Numero').drop(columns=['Numero'])
        
        #Guarda el DataFrame ordenado en un archivo CSV en el directorio actual.
        dataset_promedios = os.path.join(actual, 'promedios.csv')
        resultado_df.to_csv(dataset_promedios, index=False)
        print(f'Los promedios se han guardado en {dataset_promedios}')