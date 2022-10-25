#code is working but google don't allow unidentified loggings
import smtplib

s = smtplib.SMTP("smtp.gmail.com",587)
s.starttls()

s.login("sender_mail","password")

msg= '''Hello,I am sending this email via Python Automation'''

s.send("sender-mail","receiver_mail",msg)

s.quit()
