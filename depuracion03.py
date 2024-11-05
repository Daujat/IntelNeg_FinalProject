import pandas as pd
import numpy as np


def impute_weather_data(file_name, rainfall_method='median'):
    # Leer el archivo CSV
    print(f"Leyendo archivo: {file_name}")
    df = pd.read_csv(file_name)

    # Imputar MaxTemp y MinTemp con la mediana
    df['MaxTemp'] = df['MaxTemp'].fillna(df['MaxTemp'].median())
    df['MinTemp'] = df['MinTemp'].fillna(df['MinTemp'].median())

    # Imputar Rainfall
    if rainfall_method == 'median':
        df['Rainfall'] = df['Rainfall'].fillna(df['Rainfall'].median())
    elif rainfall_method == 'zero':
        df['Rainfall'] = df['Rainfall'].fillna(0)

    # Guardar el archivo actualizado
    output_file = 'games_imputed.csv'
    df.to_csv(output_file, index=False)
    print(f"Archivo actualizado guardado como: {output_file}")

    # Verificar que no queden valores NaN
    nan_columns = df.columns[df.isna().any()].tolist()
    if nan_columns:
        print("Advertencia: Aún quedan valores NaN en las siguientes columnas:")
        for col in nan_columns:
            print(f"  - {col}: {df[col].isna().sum()} valores NaN")
    else:
        print("Todos los valores NaN han sido imputados exitosamente.")

    # Mostrar estadísticas descriptivas de las columnas imputadas
    print("\nEstadísticas descriptivas después de la imputación:")
    print(df[['MaxTemp', 'MinTemp', 'Rainfall']].describe())


# Ejecutar la función
impute_weather_data('games.csv', rainfall_method='median')