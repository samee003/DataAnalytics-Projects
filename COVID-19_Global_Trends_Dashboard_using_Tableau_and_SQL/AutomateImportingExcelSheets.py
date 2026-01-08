import pandas as pd
#df = pd.read_excel("E:\\samee\\B.Sc. CS\\Projects\\DataAnalytics\\DataExploration(covid dataset)\\CovidDeaths.xlsx", engine='openpyxl')
#df = pd.read_excel("E:\\samee\\B.Sc. CS\\Projects\\DataAnalytics\\DataExploration(covid dataset)\\CovidVaccinations.xlsx", engine='openpyxl')
df = pd.read_excel(
    "E:\\samee\\B.Sc. CS\\Projects\\DataAnalytics\\DataCleaning(Tech_Layoffs dataset)\\Tech_Layoffs_March2023_Dataset.xlsx",
    engine='openpyxl'
)

print(df.columns.tolist())  # See your column names

import pyodbc

# Connect to SQL Server
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost\\SQLEXPRESS;DATABASE=tech_layoffs_db;Trusted_Connection=yes;"
)
cursor = conn.cursor()

# Generate SQL table schema dynamically
table_name = "global_company_layoffs" # Write the Table Name
columns_sql = []
for col in df.columns:
    dtype = df[col].dtype
    if pd.api.types.is_integer_dtype(dtype):
        sql_type = "INT"
    elif pd.api.types.is_float_dtype(dtype):
        sql_type = "FLOAT"
    elif pd.api.types.is_bool_dtype(dtype):
        sql_type = "BIT"
    elif pd.api.types.is_datetime64_any_dtype(dtype):
        sql_type = "DATETIME"
    else:
        sql_type = "NVARCHAR(MAX)"  # Default for text or mixed types
    columns_sql.append(f"[{col}] {sql_type}")

# Create table SQL
create_table_sql = f"""
IF OBJECT_ID('{table_name}', 'U') IS NOT NULL DROP TABLE {table_name};
CREATE TABLE {table_name} (
    {', '.join(columns_sql)}
)
"""
cursor.execute(create_table_sql)
conn.commit()


placeholders = ', '.join(['?' for _ in df.columns])
insert_sql = f"INSERT INTO {table_name} ({', '.join('[' + col + ']' for col in df.columns)}) VALUES ({placeholders})"

df = df.fillna(value=pd.NA)  # replaces all NaNs with <NA> (better for handling missing data)

for _, row in df.iterrows():
    values = []
    for val in row:
        if pd.isna(val):  # Replace NaN/NA with None
            values.append(None)
        else:
            values.append(val)
    cursor.execute(insert_sql, tuple(values))


conn.commit()
cursor.close()
conn.close()
print("All data inserted successfully.")