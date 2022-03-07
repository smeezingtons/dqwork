#from boto3 import client

from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark import SparkConf


spark = SparkSession.builder.appName('sparkdf').getOrCreate()

# list  of college data with two lists
data = [["java", "dbms", "python"],
        ["Spark", "SQL", "Machine Learning"]]

# giving column names of dataframe
columns = ["Subject 1", "Subject 2", "Subject 3"]

# creating a dataframe
dataframe = spark.createDataFrame(data, columns)

# show data frame
dataframe.show()


