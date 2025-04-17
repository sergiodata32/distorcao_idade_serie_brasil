# Análise de Distorção Idade-Série - Brasil 2020 (VS Code)

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Leitura do arquivo CSV com caminho absoluto (VS Code)
caminho_arquivo = r"C:\Users\T-GAMER\Desktop\distorcao-idade-serie-2020-Brasil.csv"
df = pd.read_csv(caminho_arquivo, sep=";")

# Convertendo colunas numéricas de string para float
cols_numericas = [
    "Anos Iniciais", "Anos Finais",
    "1º ano", "2º ano", "3º ano", "4º ano", "5º ano",
    "6º ano", "7º ano", "8º ano", "9º ano",
    "1ª Série EM", "2ª Série EM", "3ª Série EM", "4ª Série EM"
]
for col in cols_numericas:
    df[col] = df[col].replace("--", np.nan)             # substitui "--" por NaN
    df[col] = df[col].str.replace(",", ".")            # troca vírgula por ponto
    df[col] = df[col].astype(float)                      # converte para float

# 1. Média da distorção por região (Anos Iniciais)
media_regiao = df.groupby("Região")["Anos Iniciais"].mean().sort_values()
media_regiao.plot(kind="barh", title="Média de Distorção - Anos Iniciais por Região")
plt.xlabel("% de Distorção")
plt.tight_layout()
plt.show()

# 2. Comparativo Urbana x Rural - Anos Iniciais
df_local = df.groupby("Localização")["Anos Iniciais"].mean().sort_values()
df_local.plot(kind="bar", title="Distorção - Localização Urbana x Rural")
plt.ylabel("% de Distorção")
plt.tight_layout()
plt.show()

# 3. Maiores valores por série do Ensino Médio
max_por_em = df[["1ª Série EM", "2ª Série EM", "3ª Série EM", "4ª Série EM"]].max()
max_por_em.plot(kind="bar", title="Maior Distorção por Série do Ensino Médio")
plt.ylabel("% de Distorção")
plt.tight_layout()
plt.show()

# 4. Linha com maior distorção no 6º ano
maior_6ano = df[df["6º ano"] == df["6º ano"].max()]
print("\nMaior distorção no 6º ano:")
print(maior_6ano[["Região", "Localização", "Dependência Administrativa", "6º ano"]])
