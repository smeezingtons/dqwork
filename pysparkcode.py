#from boto3 import client
from awsglue.context import GlueContext
from pyspark.context import SparkContext
from pyspark import SparkConf
from pyspark.sql import SparkSession

sc = SparkContext()
glueContext = GlueContext(sc)
logger = glueContext.get_logger()

logger.warn("warn message")
logger.error("error message")

my_conf = SparkConf()
my_conf.set("spark.app.name","myfirstapplication")


spark = SparkSession.builder.config(conf=my_conf).getOrCreate()

data = [1,2,3,4,5,6,7,8,9,10]
rdd = spark.sparkContext.parallelize(data)

logger.info(rdd.collect())

spark.stop()

