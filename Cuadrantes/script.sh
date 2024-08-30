#!/bin/bash

# Ruta donde están las 63 carpetas
base_path="."

# Lista de subcarpetas a crear
subcarpetas=("LAND_SURFACE" "NDVI" "PRECIPITATION" "WATER_VAPOR")

# Itera sobre cada una de las 63 carpetas
for i in {1..63}
do
  mkdir -p "$i"
  # Ruta a la carpeta actual
  carpeta="$base_path/$i"
  
  # Crea las subcarpetas en la carpeta actual
  for subcarpeta in "${subcarpetas[@]}"
  do
    mkdir -p "$carpeta/$subcarpeta"
  done
done
