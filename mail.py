import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Replace with your credentials
GMAIL_USER = ""
GMAIL_PASS = "" 
TO_EMAIL = ""

def mail_init(userid,passkey,Dmailid):
    global GMAIL_USER,GMAIL_PASS,TO_EMAIL
    GMAIL_USER = userid
    GMAIL_PASS = passkey
    TO_EMAIL = Dmailid

# Build message


def SendMail(message):
    # Send Email
    global GMAIL_USER,GMAIL_PASS,TO_EMAIL
    msg = MIMEMultipart()
    msg['From'] = GMAIL_USER
    msg['To'] = TO_EMAIL
    msg['Subject'] = 'Pi Notification'
    msg.attach(MIMEText(message, 'plain'))
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server: #
            server.starttls() #
            server.login(GMAIL_USER, GMAIL_PASS)
            server.send_message(msg)
        print('Email sent!')
    except Exception as e:
        print(f'Error: {e}')
    
if __name__ == "__main__":
    SendMail("Hello")