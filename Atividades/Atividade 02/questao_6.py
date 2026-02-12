import pandas as pd
import numpy as np

np.random.seed(42)
dados_normais = np.random.normal(loc=50, scale=10, size=100)
outliers = [150, 200, 5, 2]
todos_dados = np.concatenate([dados_normais, outliers])
df = pd.DataFrame({'valor': todos_dados})

print("DataFrame original:")
print(df.describe())
print("\nPrimeiras linhas:")
print(df.head(10))
print("-" * 60)

print("\nIdentificação por desvio padrão:")

media = df['valor'].mean()
desvio = df['valor'].std()
z_scores = (df['valor'] - media) / desvio
outliers_z = df[np.abs(z_scores) > 3]
print("Outliers:")
print(outliers_z)

print("\nIdentificar por quartis:")
Q1 = df['valor'].quantile(0.25)
Q3 = df['valor'].quantile(0.75)
IQR = Q3 - Q1
limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR
outliers_iqr = df[(df['valor'] < limite_inferior) | (df['valor'] > limite_superior)]

print(f"Q1 = {Q1:.2f}, Q3 = {Q3:.2f}, IQR = {IQR:.2f}")
print(f"Limites: [{limite_inferior:.2f}, {limite_superior:.2f}]")
print("Outliers:")
print(outliers_iqr)


mask_normal = (df['valor'] >= limite_inferior) & (df['valor'] <= limite_superior)
df_sem_outliers = df[mask_normal].copy()
print("Outliear removidos:")
print(df_sem_outliers.describe())
print(f"Linhas originais: {len(df)} | Linhas após remoção: {len(df_sem_outliers)}")


print("\nSubstituir pelos limites:")

df_capping = df.copy()
df_capping['valor'] = df_capping['valor'].clip(lower=limite_inferior, upper=limite_superior)
print(df_capping['valor'].describe())