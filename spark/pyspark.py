import findspark
findspark.init()

from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

parDF1=spark.read.parquet("data/bdf6370f3c8e4182a97cd930996df1b7.snappy.parquet")