import pandas as pd
data = pd.read_csv('stats.csv')

# Reemplazar los valores vacíos, "-" y "0" por "Not applicable"
data['Subs'] = data['Subs'].fillna('Not applicable')
data['Subs'] = data['Subs'].replace(['', '-', '0'], 'Not applicable')

data.to_csv('stats_updated.csv', index=False)
print('Archivo modificado correctamente')