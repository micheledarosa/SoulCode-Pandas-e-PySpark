import plotly.express as px

#  Dataset geral
df = px.data.gapminder().query("country=='Canada'")  #  puxa o banco de dados q diz respeito ao Canadá

#  Linha
'''fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada')
fig.show()'''

#  Histograma
'''df = px.data.tips()
fig = px.histogram(df, x = 'total_bill')
fig.show()'''

#  Scatter
fig = px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])
fig.show()