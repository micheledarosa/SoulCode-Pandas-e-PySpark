import findspark
findspark.init()

from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql.types import *  #  pode colocar o tipo de dados que quer importar ex: float, str...

spark = SparkSession.builder \
    .master('local') \
    .appName('Aula introdutória PySpark') \
    .config('spark.executor.memory', '1gb') \
    .getOrCreate()

sc = spark.sparkContext

rdd = sc.textFile('/VSCode/Soul Code/vgsales.csv')  #  substituir as barras \ por barras /
rdd = rdd.map(lambda line: line.split(','))

df = rdd.map(lambda line: Row(Rank=line[0], Nome=line[1])).toDF()  # a variável se torna um data frame
#  df.show()

#  df.printSchema()  #  imprime os tipos de dados

def converterColuna(dataframe, nomes, novoTipo):
    for nome in nomes:
        dataframe = dataframe.withColumn(nome, dataframe[nome].cast(novoTipo))
    return dataframe

colunas = ['Rank']

df = converterColuna(df, colunas, FloatType())  #  convertendo a coluna rank para float
#  df.show()
#  df.printSchema()

#  df.filter(df['Rank'] > 16000).show()  #  mostra todas as colunas

#  df.select('Rank').filter(df['Rank'] > 16000).show()  #  mostra apenas a coluna Rank

#  df.filter((df['Rank'] > 16000) & (df['Rank'] < 16015)).show()  #  pode também filtrar outra coluna além do Rank

#  df.select('Nome').show(10)

#  df. groupby('Nome').count().sort('Nome', ascending=False).show()  #  assim ele mostra descendente

#  df.select('Nome').count()

#  df.describe().show()

#  df.describe('Nome').show()

#  df.collect()

'''rdd_new = rdd.map(lambda line: line.split(','))
rdd_new.take(7)''' #  tratamento de dados

#  rdd = rdd.map(lambda line: line.split(','))  #  nova atribuição/rdd

#  rdd.take(5)  #  pega os primeiros 5 dados

#  rdd.first()  #  pega a primeira linha
