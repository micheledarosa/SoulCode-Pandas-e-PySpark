import numpy as np 
import pandas as pd 

notas = pd.Series([10, 5, 7.5, 9, 10])
print(notas)
print(notas.values)
print(notas.index)

notas2 = pd.Series([10, 5, 7.5, 9, 10], index=['José', 'Carlos', 'André', 'João', 'Débora'])
print(notas2)

print(notas.describe)
print(notas.mean())
print(notas ** 2)