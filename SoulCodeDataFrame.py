import numpy as np
import pandas as pd

df = pd.DataFrame({'Aluno':["José", "Carlos", "Ana", "Júlia", "Débora"],
                   'Faltas':[3, 4, 2, 4, 3],
                   'Provas':[2, 7, 8, 5.5, 9.2],
                   'Seminário':[8.5 ,5 , 8.2, 6, 9.5]})

#  EXEMPLOS DE EXIBIÇÃO DE DADOS
#  print(df)
#  print(df.dtypes)
#  print(df.columns)
#  print(df['Aluno'])
#  print(df.describe())
#  print(df.sort_values(by = 'Seminário'))
#  print(df.loc[3])
#  print(df[df['Seminário'] > 8.0])
print(df[(df["Seminário"] > 8.0 ) & (df["Provas"] > 3)])