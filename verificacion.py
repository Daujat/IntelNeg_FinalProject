import pandas as pd


def check_nan_in_file(file_name):
    print(f"\nVerificando archivo: {file_name}")
    df = pd.read_csv(file_name)

    nan_columns = df.columns[df.isna().any()].tolist()

    if nan_columns:
        print("Columnas con valores NaN:")
        for col in nan_columns:
            nan_count = df[col].isna().sum()
            print(f"  - {col}: {nan_count} valores NaN")
    else:
        print("No se encontraron valores NaN en ninguna columna.")


# Lista de archivos a verificar
files_to_check = ['games.csv', 'players_updated.csv', 'stats_updated.csv']

# Verificar cada archivo
for file in files_to_check:
    check_nan_in_file(file)