# Integrate Spark with Kafka

import findspark
findspark.init()

from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType, FloatType, IntegerType, TimestampType


# Intialize Spark Session
