import pandas as pd
import numpy as np

n_linhas = 10
n_colunas = 4

dados = np.random.randint(0, 101, size=(n_linhas, n_colunas))

df_original = pd.DataFrame(dados, columns=['col_A', 'col_B', 'col_C', 'col_D'])

df_original.to_csv('dados_aleatorios.csv', index=False)
print("Arquivo 'dados_aleatorios.csv' gerado com sucesso!")

df_lido = pd.read_csv('dados_aleatorios.csv')

print("\nPrimeiras 5 linhas do DataFrame:")
print(df_lido.head())

print("\nDataFrame completo:")
print(df_lido)
