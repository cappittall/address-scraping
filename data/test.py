from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, expr

# Initialize Spark Session
spark = SparkSession.builder.appName("RecordProcessing").getOrCreate()

# Load the data
data = [
    "A345621236745HAWAII",
    "B245639GHIWRT236745 &1 HI",
    "C8768134484MN 09239",
    "D677188HD78SFI89012"
]

# Create DataFrame
df = spark.createDataFrame(data, "string").toDF("record")

# Separate the records based on their type
df_a = df.filter(col("record").startswith("A")).withColumn("key_field_a", col("record").substr(8, 6)).withColumn("value_field_a", col("record").substr(14, 8)).alias("df_a")
df_b = df.filter(col("record").startswith("B")).withColumn("key_field_b", col("record").substr(14, 6)).alias("df_b")

# Join the DataFrames on the key_field
df_joined = df_b.join(df_a, col("df_b.key_field_b") == col("df_a.key_field_a"), "inner")

# Replace the '&1' string in record 'B' with the corresponding value from record 'A'
df_result = df_joined.withColumn("updated_record", when(col("df_b.record").startswith("B"), expr("regexp_replace(df_b.record, '&1', df_a.value_field_a)")).otherwise(col("df_b.record")))

# Selecting the final output columns and sorting by the original 'record' column to maintain the order
final_df = df_result.select("updated_record").sort("updated_record")

# Show the final result
final_df.show(truncate=False)

# Stop the Spark session
spark.stop()
