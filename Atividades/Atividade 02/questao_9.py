import pandas as pd
import numpy as np

np.random.seed()
dados = np.random.randint(0, 101, size=(10, 2))
df = pd.DataFrame(dados, columns=['idade', 'salario'])

print("=== DATAFRAME GERADO ===")
print(df)
print()
print()

print("Coluna 'salario':")
coluna = df['salario']
print(coluna)
print()
print()

print("Filtro pessoas mais de 50 anos:")
filtro_idade = df['idade'] > 50
df_filtrado = df[filtro_idade]
print(df_filtrado)