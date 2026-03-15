from pyspark.sql import SparkSession
from pyspark.sql.functions import sum

spark = SparkSession.builder.appName("SalesPipeline").getOrCreate()

df = spark.read.csv("../data/clean_sales_data.csv", header=True, inferSchema=True)

df.show()

result = df.groupBy("category").agg(sum("total_value").alias("total_sales"))

result.show()

spark.stop()
