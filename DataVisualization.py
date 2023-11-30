import pandas as pd
import seaborn as sns  #  para mostrar gráficos
import matplotlib.pyplot as plt  #  graficos

iris = pd.read_csv('Iris.csv', names=['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm', 'Species'])
#  print(iris.head())
wine_reviews = pd.read_csv('winemag-data-130k-v2.csv', index_col=0)
wine_reviews.head()

#  sns.scatterplot(x='SepalLengthCm', y='SepalWidthCm', data=iris)
#  sns.displot(wine_reviews['price'], bins=10, kde=True)
#  sns.countplot(wine_reviews['price'])

'''fig, ax = plt.subplots();
data = wine_reviews['style'].value_counts()  #  criando um gráfico de barras

style = data.index
frequency = data.values

ax.bar(style, frequency)
ax.set_title('Wine Review Scores')
ax.set_xlabel('Style')
ax.set_ylabel('Frequency')'''

'''fig, ax = plt.subplots();

ax.hist(wine_reviews['winery'])  #   criando um histograma

ax.set_title('Wine Review Scores')
ax.set_xlabel('Style')
ax.set_ylabel('Frequency')'''

'''columns = iris.columns.drop(['Species'])  #  eliminando a coluna que não tem valor numérico / drop para deletar
x_data = range(0, iris.shape[0])
fig, ax = plt.subplots()  #  criando um gráfico de linhas

for column in columns:
    ax.plot(x_data, iris[column], label=column)

ax.set_title('Iris Dataset')
ax.legend()'''

fig, ax = plt.subplots()

ax.scatter(iris['SepalLengthCm'], iris['SepalWidthCm'])

ax.set_title('Iris Dataset')
ax.set_xlabel('SepalLengthCm')
ax.set_ylabel('SepalWidthCm')