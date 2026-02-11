import numpy as np
import pandas as pd

def detectar_outliers_zscore(df, coluna, limiar=3):
    media = df[coluna].mean()
    std = df[coluna].std()
    z_scores = (df[coluna] - media) / std
    outliers = df[np.abs(z_scores) > limiar]
    return outliers

def detectar_outliers_iqr(df, coluna):
    Q1 = df[coluna].quantile(0.25)
    Q3 = df[coluna].quantile(0.75)
    IQR = Q3 - Q1
    lim_inf = Q1 - 1.5 * IQR
    lim_sup = Q3 + 1.5 * IQR
    outliers = df[(df[coluna] < lim_inf) | (df[coluna] > lim_sup)]
    return outliers, lim_inf, lim_sup

def winsorizar(df, coluna):
    Q1 = df[coluna].quantile(0.25)
    Q3 = df[coluna].quantile(0.75)
    IQR = Q3 - Q1
    lim_inf = Q1 - 1.5 * IQR
    lim_sup = Q3 + 1.5 * IQR
    df[coluna] = df[coluna].clip(lower=lim_inf, upper=lim_sup)
    return df

def main():
    # Dados de exemplo
    np.random.seed(42)
    dados = {
        'valor': np.concatenate([np.random.normal(50, 10, 100), [150, 200, 5, 2]])
    }
    df = pd.DataFrame(dados)

    # Identificação por IQR
    outliers_iqr, li, ls = detectar_outliers_iqr(df, 'valor')
    print(f"Outliers (IQR): {len(outliers_iqr)}")
    print(outliers_iqr)

    # Tratamento por winsorização
    df_wins = df.copy()
    df_wins['valor'] = df_wins['valor'].clip(lower=li, upper=ls)
    print(f"\nApós winsorização:\n{df_wins['valor'].describe()}")


if __name__ == "__main__":
    main()
