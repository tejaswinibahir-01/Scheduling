from datetime import date
import pandas as pd
from send_emails import send_email
import schedule
import time
from schedule import repeat

SHEET_ID="1YlwSGrGaUrTy--OBcHCuSMKjuWfePAXC4Dj9UVn0Llo"
SHEET_NAME="Scheduler"
URL=f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"


def load_df(url):
    parse_dates=["due_date","reminder_date"]
    df=pd.read_csv(url,parse_dates=parse_dates)
    return df

#print(load_df(URL))

#to query data and send emails

#@repeat(schedule.every(10).seconds)
def query_send(df):
    present =date.today()
    email_counter=0
    for _, row in df.iterrows():
        if(row["status"] =="No"):
            send_email(
                subject=f"[Task Reminder]",
                reciever_email=row["email"],
                name=row["name"],
                due_date=row["due_date"].strftime("%d, %b %Y"),
                invoice_no=row["invoice_no"],
                taskNos=row["taskNos"],
            )
            email_counter+=1
            print("hii")
    return f"Total Emails Sent:{email_counter}"


df=load_df(URL)
#result=query_send(df)
#print(result)
print(query_send(df))
schedule.every(1).minute.do(query_send,df)


while True:
    schedule.run_pending()
    time.sleep(1)

