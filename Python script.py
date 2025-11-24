import pandas as pd
import snowflake.connector

conn = snowflake.connector.connect(
    user='xxxx',
    password='xxxx',
    account='xxxx',
    warehouse='xxxx',
    database='xxxx',
    schema='xxxx'
)
sql = "SELECT * FROM FLIGHT"
df = pd.read_sql(sql, conn)
df.to_csv('FLIGHTREPORT.csv', index=False)
conn.close()

