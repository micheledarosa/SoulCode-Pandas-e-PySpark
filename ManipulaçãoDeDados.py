import numpy as np
import pandas as pd

df_csv = pd.read_csv("")

print(df_csv['bairro'].unique())
print(df_csv['bairro'].value_counts())  # imprime o valor que existe na coluna
print(df_csv.groupby("bairro").mean())  # ordena pela media do grupo

#---------------------------

df2 = df_csv.head()  #  novo df com os primeiros itens do outro
print(df2)
df3 = df2.replace({"pm2":{12031.25:np.nan}})  #  utilize esse comando para substituição (nan = not a number)
print(df3)
df4 = df3.dropna()  # remove linhas que tem o erro NaN (not a number)
print(df4)
