from pyspark.sql.session import SparkSession
from pyspark.sql.types import (BooleanType, IntegerType, StringType, TimestampType, StructType, StructField, ArrayType, FloatType)
import pyspark.sql.functions as F

#  outra opção para criar a sessão
spark = SparkSession.builder.appName('firstSession').config('spark.master', 'local[4]')\
    .config('spark.executor.memory', '1gb')\
    .config('spark.shuffle.partitions', 1)\
    .getOrCreate()

#  verificar o arquivo e definir o schema
schema = StructType([
    StructField('rank', FloatType()),
    StructField('name', StringType())
])

df = spark.read.schema(schema)\
    .json('')  # colocar o caminho do arquivo

df.printSchema()
df.show()

#  output = spark.sql('SELECT rank FROM zipcodes WHERE rank > 10')
df.registerTempTable('zipcodes')
output = spark.sql('SELECT * FROM zipcodes')  # tudo = * / específico = SELECT rank FROM zipcodes
output.show()
