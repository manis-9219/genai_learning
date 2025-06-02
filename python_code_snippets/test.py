from pyspark.sql import SparkSession

try:
    spark = SparkSession.builder.appName("TestPySpark").getOrCreate()
    print("PySpark is set up correctly!")
    df = spark.createDataFrame([(1, "Alice"), (2, "Bob")], ["id", "name"])
    df.show()
    spark.stop()
except Exception as e:
    print("PySpark is not set up correctly:", e)