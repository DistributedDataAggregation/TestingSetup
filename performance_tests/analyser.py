import pandas as pd
import pyarrow.parquet as pq
file_path = "/home/data/benchmark/file_0.parquet"
df = pd.read_parquet(file_path)

print(df.columns.tolist())

parquet_file = pq.ParquetFile(file_path)


print(parquet_file.schema.names)

schema = parquet_file.schema

print(schema)