import pandas as pd
from sqlalchemy import create_engine

# Datos de conexión para SQL Server
DB_SERVER = 'DESKTOP-ABV50VN\\MSSQLSERVER01'
DB_NAME = 'AustralianFootballLeague'
DB_USER = ''
DB_PASSWORD = ''

# Crear el string de conexión
connection_string = f"mssql+pyodbc://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}/{DB_NAME}?driver=ODBC+Driver+17+for+SQL+Server"

# Crear la conexión con la base de datos
engine = create_engine(connection_string)

# Ruta del archivo CSV - games
games_csv_path = 'games_without_time.csv'

# Leer el archivo CSV con delimitador explícito
games_df = pd.read_csv(games_csv_path, delimiter=',')

# Convertir la columna 'Attendance' a float eliminando las comas
games_df['Attendance'] = games_df['Attendance'].str.replace(',', '').astype(int)

# Asegurarnos de que el resto de las columnas se conviertan adecuadamente a enteros
columns_to_convert = [
    'HomeTeamScoreQT', 'HomeTeamScoreHT', 'HomeTeamScore3QT', 'HomeTeamScoreFT',
    'AwayTeamScoreQT', 'AwayTeamScoreHT', 'AwayTeamScore3QT', 'AwayTeamScoreFT'
]

for column in columns_to_convert:
    games_df[column] = pd.to_numeric(games_df[column], errors='coerce').fillna(0).astype(int)

# Escribir el DataFrame en la tabla 'games'
games_df.to_sql('games', con=engine, if_exists='append', index=False)

print("Datos de 'games' cargados exitosamente en la base de datos.")