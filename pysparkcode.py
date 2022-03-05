#from boto3 import client
from pyspark import SparkConf
from pyspark.sql import SparkSession

my_conf = SparkConf()
my_conf.set("spark.app.name","myfirstapplication")


spark = SparkSession.builder.config(conf=my_conf).getOrCreate()

data = [1,2,3,4,5,6,7,8,9,10]
rdd = spark.sparkContext.parallelize(data)
print(rdd.collect())


spark.stop()

