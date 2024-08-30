import re
from datetime import datetime
import csv

# Lista de archivos
archivos = ['MOD_LSTD_E_2023-01-01.CSV', 'MOD_LSTD_E_2023-01-09.CSV', 'MOD_LSTD_E_2023-01-17.CSV',
            'MOD_LSTD_E_2023-01-25.CSV', 'MOD_LSTD_E_2023-02-02.CSV', 'MOD_LSTD_E_2023-02-10.CSV',
            'MOD_LSTD_E_2023-02-18.CSV', 'MOD_LSTD_E_2023-02-26.CSV', 'MOD_LSTD_E_2023-03-06.CSV',
            'MOD_LSTD_E_2023-03-14.CSV', 'MOD_LSTD_E_2023-03-22.CSV', 'MOD_LSTD_E_2023-03-30.CSV',
            'MOD_LSTD_E_2023-04-07.CSV', 'MOD_LSTD_E_2023-04-15.CSV', 'MOD_LSTD_E_2023-04-23.CSV',
            'MOD_LSTD_E_2023-05-01.CSV', 'MOD_LSTD_E_2023-05-09.CSV', 'MOD_LSTD_E_2023-05-17.CSV',
            'MOD_LSTD_E_2023-05-25.CSV', 'MOD_LSTD_E_2023-06-02.CSV', 'MOD_LSTD_E_2023-06-10.CSV',
            'MOD_LSTD_E_2023-06-18.CSV', 'MOD_LSTD_E_2023-06-26.CSV', 'MOD_LSTD_E_2023-07-04.CSV',
            'MOD_LSTD_E_2023-07-12.CSV', 'MOD_LSTD_E_2023-07-20.CSV', 'MOD_LSTD_E_2023-07-28.CSV',
            'MOD_LSTD_E_2023-08-05.CSV', 'MOD_LSTD_E_2023-08-13.CSV', 'MOD_LSTD_E_2023-08-21.CSV',
            'MOD_LSTD_E_2023-08-29.CSV', 'MOD_LSTD_E_2023-09-06.CSV', 'MOD_LSTD_E_2023-09-14.CSV',
            'MOD_LSTD_E_2023-09-22.CSV', 'MOD_LSTD_E_2023-09-30.CSV', 'MOD_LSTD_E_2023-10-08.CSV',
            'MOD_LSTD_E_2023-10-16.CSV', 'MOD_LSTD_E_2023-10-24.CSV', 'MOD_LSTD_E_2023-11-01.CSV',
            'MOD_LSTD_E_2023-11-09.CSV', 'MOD_LSTD_E_2023-11-17.CSV', 'MOD_LSTD_E_2023-11-25.CSV',
            'MOD_LSTD_E_2023-12-03.CSV', 'MOD_LSTD_E_2023-12-11.CSV', 'MOD_LSTD_E_2023-12-19.CSV',
            'MOD_LSTD_E_2023-12-27.CSV']

#Extrae las fechas usando una expresión regular
fechas = [re.search(r'\d{4}-\d{2}-\d{2}', archivo).group() for archivo in archivos]

#Convierte las fechas a objetos datetime
fechas_datetime = [datetime.strptime(fecha, '%Y-%m-%d') for fecha in fechas]

# Guardar las fechas en un archivo CSV
with open('fechas.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Fecha'])
    for fecha in fechas_datetime:
        writer.writerow([fecha.strftime('%Y-%m-%d')])
