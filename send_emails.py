import os
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path
from dotenv import load_dotenv

PORT=587
EMAIL_SERVER="smtp-mail.outlook.com"


#load the env variables
current_dir=Path(__file__).resolve().parent if "__file__" in locals() else Path.cwd()
envars=current_dir/ ".env"
load_dotenv(envars)


#read environment variables
sender_email=os.getenv("EMAIL")
password_email=os.getenv("PASSWORD")






#fun to send email

def send_email(subject,reciever_email,name,due_date,invoice_no,taskNos):
    msg=EmailMessage()
    msg["Subject"]=subject
    msg["From"]=formataddr(("Atlas CopCo",f"{sender_email}"))
    msg["To"]=reciever_email
    msg["BCC"]= sender_email

    msg.set_content(
        f"""\
        Hi {name},
        This is just a quick note to remind you that {taskNos} out of your total tasks of current projects are pending.
        Due for your task is {due_date}.
        Best regards,
        ATLAS COPCO.
        """
    )

    msg.add_alternative(
        f"""\
        <html>
            <body>
            <p>Hi {name},</p>
            <p>This is just a quick note to remind you that <strong> {taskNos} </strong> out of your total tasks of current projects are pending.
            <p> Due for your task is <strong> {due_date} </strong>.</p>
            <p> Best regards,</p>
            <p> ATLAS COPCO.</p>
            </body>
        </html>
        """,
        subtype='html',
    )

    with smtplib.SMTP(EMAIL_SERVER,PORT) as server:
        server.starttls()
        server.login(sender_email,password_email)
        server.sendmail(sender_email,reciever_email,msg.as_string())


if __name__=="__main__":
    send_email(
        subject="Task Reminder",
        name="Rahul Khade",
        reciever_email="rahulkhade306@gmail.com",
        due_date="18,Aug 2023",
        invoice_no="INV-21-12-009",
        taskNos="4",
    )
