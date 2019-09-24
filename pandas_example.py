import pandas as pd
import numpy as np

data = {
    'Nombre': ['Maria', 'Marcela', 'Pola'],
    'Calificacion': ['100', '50', '22'],
    'Deporte': ['Futbol', 'Basqueball', 'Esgrima'],
    'Materia': ['Ingles', 'Quimica', 'Fisica']
}

df = pd.DataFrame(data)
print(df)
print('\n' * 2)

# Datos no validos
data2 = {
    'Nombre': ['Maria', 'Marcela', 'N/A'],
    'Calificacion': ['100', np.nan, '22'],
    'Deporte': ['N/A', 'Basqueball', 'Esgrima'],
    'Materia': ['Ingles', 'N/A', 'Fisica']
}
df2 = pd.DataFrame(data2)
print(df2)
print(df2.info())
print('\n' * 2)
print(df2.describe())

# Estadisticas basicas
nuevo = pd.DataFrame(df2)
nuevo = nuevo.replace(np.nan, '0')
print(nuevo)
print('\n' * 2)

nuevo2 = pd.DataFrame(df2)
nuevo2.dropna(how='any', inplace=True)
print(nuevo2)
print('\n' * 2)

# Eliminar registro
Columna = df2[df2['Nombre'] != 'N/A']
print(Columna)
print('\n' * 2)

# Llenar con ceros valor nan
nuevo3 = pd.DataFrame(df2)
nuevo3.fillna(0, inplace=True)
print(nuevo3)
print('\n' * 2)

# Estadisticas
print(nuevo3.describe())
print('\n' * 2)

# Convertir a numeros enteros
nuevo2['Calificacion'] = nuevo2.Calificacion.astype(int)
print(nuevo2)
print('\n' * 2)

# Estadisticas
print(nuevo2.describe())
print('\n' * 2)

# Estadisticas individuales
print(nuevo2['Calificacion'].max())
print('\n' * 2)