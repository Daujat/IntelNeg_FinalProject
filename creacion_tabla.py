import pandas as pd

def create_dimensions_by_time(input_file, output_file):
    # Leer el archivo CSV
    print(f"Leyendo archivo: {input_file}")
    df = pd.read_csv(input_file)

    # Convertir la columna 'Date' a datetime
    df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')

    # Extraer Year, Month y Day
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    df['Day'] = df['Date'].dt.day

    # Crear el DataFrame dimensions_df con las columnas requeridas
    dimensions_df = df[['GameId', 'Day', 'Month', 'Year', 'StartTime']].copy()

    # Agregar la columna TimeId auto-incremental
    dimensions_df.insert(0, 'TimeId', range(1, len(dimensions_df) + 1))

    # Reordenar las columnas según lo especificado
    dimensions_df = dimensions_df[['TimeId', 'GameId', 'Day', 'Month', 'Year', 'StartTime']]

    # Guardar el nuevo archivo CSV
    dimensions_df.to_csv(output_file, index=False)
    print(f"Archivo creado: {output_file}")

# Ejecutar la función
create_dimensions_by_time('games_imputed.csv', 'dimensions_by_time.csv')