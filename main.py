import pandas as pd
from sqlalchemy import create_engine

csv_file_path = "statement.csv"
df = pd.read_csv(csv_file_path)

with open("connectionstring.auth", "r") as file:
    connectionstring = file.read()
    # example: postgresql+psycopg2://username:password@localhost:5432/dbname

engine = create_engine(connectionstring)
table_name = "transactions"

df.to_sql(table_name, engine, if_exists="replace", index=False)
