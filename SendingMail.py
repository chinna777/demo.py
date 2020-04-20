import smtplib
from email.mime.text import MIMEText
body="Hi venkey how are you \n and how was your health \n iam worried about you"
msg=MIMEText(body)
msg['From']='venkey6808@gmail.com'
msg['To']='venkey36808@gmail.com'
msg['Subject']='greeting'
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('venkey6808@gmail.com','8464036808@v')
server.send_message(msg)
print('message sucessfully sent')
server.quit()
