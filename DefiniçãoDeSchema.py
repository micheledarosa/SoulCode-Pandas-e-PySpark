from pyspark.sql.session import SparkSession
from pyspark.sql.types import (BooleanType, IntegerType, StringType, TimestampType, StructType, StructField, ArrayType, FloatType)
import pyspark.sql.functions as F

#  outra opção para criar a sessão
spark = SparkSession.builder.appName('firstSession')\
    .config('spark.master', 'local[4]')\
    .config('spark.executor.memory', '1gb')\
    .config('spark.shuffle.partitions', 1)\
    .getOrCreate()

#  setando os schemas no data frame
schema = StructType([
                StructField('rank', IntegerType()),
                StructField('name', StringType()),
                StructField('plataform', StringType()),
                StructField('year', IntegerType()),
                StructField('genre', StringType()),
                StructField('publisher', StringType()),
                StructField('na_sales', FloatType())
])

path = '/VSCode/Soul Code/Pandas e PySpark/vgsales.csv'
df = spark.read.format('csv')\
    .schema(schema)\
    .load(path)

#  df.printSchema()

#  cases = df.withColumnRenamed('rank', 'Ranks')  #  modificando uma única coluna
#  cases = df.toDF(*['Ranks', 'Nomes', 'Plataformas', 'Ano', 'Gênero'])  #  modificando várias colunas
#  cases.show()

df2 = df.select('rank', 'name', 'plataform')  #  novo data frame com apenas essas colunas
df2.show()
'''df3 = df.sort(F.desc('confirmed'))
df3.show()'''