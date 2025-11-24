import snowflake.connector
import pandas as pd

conn = snowflake.connector.connect(
    user='xxxx',
    password='xxxx',
    account='xxxx',
    warehouse='xxxx',
    database='xxxx',
    schema='xxxx'
)


cur = conn.cursor().execute("SELECT * FROM FLIGHT")
df = pd.DataFrame.from_records(iter(cur), columns=[x[0] for x in cur.description])
df.to_csv('FLIGHTREPORT.csv', index=False)
conn.close()

import smtplib
from email.message import EmailMessage

EMAIL_FROM = 'xxxx@gmail.com'
EMAIL_TO = 'xxxx@gmail.com'  # Or a list of emails
EMAIL_SUBJECT = 'Daily Snowflake Report'
EMAIL_BODY = 'PFA'
EMAIL_PASSWORD = 'xxxx'  # For Gmail, use an App Password

msg = EmailMessage()
msg['Subject'] = EMAIL_SUBJECT
msg['From'] = EMAIL_FROM
msg['To'] = EMAIL_TO
msg.set_content(EMAIL_BODY)

with open('FLIGHTREPORT.csv', 'rb') as f:
    msg.add_attachment(f.read(), maintype='application', subtype='octet-stream', filename='FLIGHTREPORT.csv')

with smtplib.SMTP('smtp.gmail.com', 587) as server:  # For Gmail
    server.starttls()
    server.login(EMAIL_FROM, EMAIL_PASSWORD)
    server.send_message(msg)



