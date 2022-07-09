from email.header    import Header
from email.mime.text import MIMEText
from getpass         import getpass
from smtplib         import SMTP_SSL

login, password = 'psgcspro00@gmail.com', getpass('Gmail password:')

msg = MIMEText("We are sorry to inform that 20Z302 has critically low attendance.\nWe are extremely disappointed to inform that 20Z302 won't be able to take his end semester exams.\nHe has also been caught playing VALORANT during class hours,for which actions will be taken accordingly.", 'plain', 'utf-8')
msg['Subject'] = Header("ATTENTION!", 'utf-8')
msg['From'] = login
msg['To'] = "20Z302@psgtech.ac.in"

s = SMTP_SSL('smtp.gmail.com', 465, timeout=10)
s.set_debuglevel(1)
try:
    s.login(login, password)
    s.sendmail(msg['From'], msg['To'], msg.as_string())
finally:
    s.quit()
