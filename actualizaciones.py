import pandas as pd
def remove_time_columns(input_file, output_file):
    # Leer el archivo CSV
    print(f"Leyendo archivo: {input_file}")
    df = pd.read_csv(input_file)

    # Eliminar las columnas 'Date' y 'StartTime'
    columns_to_drop = ['Date', 'StartTime']
    df_without_time = df.drop(columns=columns_to_drop)

    # Guardar el nuevo archivo CSV
    df_without_time.to_csv(output_file, index=False)
    print(f"\nArchivo creado: {output_file}")

# Ejecutar la función
remove_time_columns('games_imputed.csv', 'games_without_time.csv')