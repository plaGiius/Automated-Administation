from email.header    import Header
from email.mime.text import MIMEText
from getpass         import getpass
from smtplib         import SMTP_SSL


login, password = 'psgcspro00@gmail.com', getpass('Gmail password:')

# create message
msg = MIMEText("We are sorry to inform that 20Z302 has failed to clear his odd semester exams .PS also we havent recieved sem fees !", 'plain', 'utf-8')
msg['Subject'] = Header("Announcement", 'utf-8')
msg['From'] = login
msg['To'] = "20z302@psgtech.ac.in"

# send it via gmail
s = SMTP_SSL('smtp.gmail.com', 465, timeout=10)
s.set_debuglevel(1)
try:
    s.login(login, password)
    s.sendmail(msg['From'], msg['To'], msg.as_string())
finally:
    s.quit()
