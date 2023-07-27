import pandas as pd
df = pd.read_parquet('input.parquet')
df.to_csv('data.csv', index=False)  