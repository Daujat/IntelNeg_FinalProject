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

# Ruta del archivo CSV - dimensions_by_time
dimensions_csv_path = 'dimensions_by_time.csv'

# Leer el archivo CSV con delimitador explícito
dimensions_df = pd.read_csv(dimensions_csv_path, delimiter=',')

# Escribir el DataFrame en la tabla 'dimensionstime'
dimensions_df.to_sql('dimensionstime', con=engine, if_exists='append', index=False)

print("Datos de 'dimensionstime' cargados exitosamente en la base de datos.")