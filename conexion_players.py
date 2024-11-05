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

# Ruta del archivo CSV
csv_path = 'players_updated.csv'

# Leer el archivo CSV
players_df = pd.read_csv(csv_path)

# Convertir la columna de fecha 'Dob' al formato ISO (YYYY-MM-DD)
players_df['Dob'] = pd.to_datetime(players_df['Dob'], errors='coerce').dt.strftime('%Y-%m-%d')

# Escribir el DataFrame en la tabla 'players'
players_df.to_sql('players', con=engine, if_exists='append', index=False)

print("Datos de 'players' cargados exitosamente en la base de datos.")