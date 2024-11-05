import pandas as pd
data = pd.read_csv('players.csv')

# Calcular la moda de la columna "Origin"
mode = data['Origin'].mode()[0]

# Reemplazar los valores faltantes y "-" con la moda
data['Origin'] = data['Origin'].fillna(mode)
data['Origin'] = data['Origin'].replace('-', mode)

data.to_csv('players_updated.csv', index=False)
print('Archivo modificado correctamente')