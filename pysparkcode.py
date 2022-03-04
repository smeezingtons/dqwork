from boto3 import client
from pyspark import SparkConf
from pyspark.sql import SparkSession
import boto3

conn = client('s3')

s3 = boto3.resource('s3')

my_conf = SparkConf()
my_conf.set("spark.app.name","myfirstapplication")
my_conf.set("spark.master","local[*]")

spark = SparkSession.builder.config(conf=my_conf).getOrCreate()
orderDf = spark.read.csv("s3://dq-landing-b1/orders.csv")
orderDf.show()

spark.stop()

