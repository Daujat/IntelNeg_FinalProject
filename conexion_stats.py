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

# Ruta del archivo CSV - stats
stats_csv_path = 'stats_updated.csv'

# Leer el archivo CSV
stats_df = pd.read_csv(stats_csv_path)

# Renombrar las columnas para que coincidan con la base de datos
column_rename_mapping = {
    '%Played': 'PlayedPercentage'
}
stats_df.rename(columns=column_rename_mapping, inplace=True)

print(f"Total de registros antes del filtrado: {len(stats_df)}")

# Filtrar registros de 'stats' para que solo se incluyan aquellos cuyos 'GameId' y 'PlayerId' existen en la base de datos
with engine.connect() as connection:
    # Obtener GameIds válidos desde la tabla 'games'
    valid_game_ids = pd.read_sql("SELECT GameId FROM games", connection)['GameId'].tolist()
    print(f"Total de GameIds válidos: {len(valid_game_ids)}")

    # Obtener PlayerIds válidos desde la tabla 'players'
    valid_player_ids = pd.read_sql("SELECT PlayerId FROM players", connection)['PlayerId'].tolist()
    print(f"Total de PlayerIds válidos: {len(valid_player_ids)}")

# Filtrar el DataFrame de 'stats' basado en los GameIds y PlayerIds válidos
stats_df = stats_df[stats_df['GameId'].isin(valid_game_ids) & stats_df['PlayerId'].isin(valid_player_ids)]

print(f"Total de registros después del filtrado: {len(stats_df)}")

# Verificar si el DataFrame está vacío antes de intentar insertarlo en la base de datos
if not stats_df.empty:
    # Escribir el DataFrame en la tabla 'stats'
    stats_df.to_sql('stats', con=engine, if_exists='append', index=False)
    print("Datos de 'stats' cargados exitosamente en la base de datos.")
else:
    print("No se encontraron registros para cargar después del filtrado.")
