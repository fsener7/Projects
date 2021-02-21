import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
fromaddr = ""
toaddr = ""
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Test Mail"
body = "Test mail from python"
msg.attach(MIMEText(body, 'plain'))
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(fromaddr, "")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
