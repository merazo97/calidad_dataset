import pandas as pd
df_pandas = pd.read_csv("/kaggle/input/cyber-security-salaries/salaries_cyber.csv")
print(df_pandas.shape)
print(f"Tamano de dataset: {df_pandas.shape[0]} fila y {df_pandas.shape[1]} columnas:")

