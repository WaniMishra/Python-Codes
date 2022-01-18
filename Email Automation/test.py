import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase

report_file = open(r'C:\Users\tejas.shete\Desktop\HR.html')
html = report_file.read()

# me == my email address
# you == recipient's email address
sender = "HROps.Automation@ikshealth.com"
rec_list =  ['wani.mishra@ikshealth.com', 'rathish.pillai@ikshealth.com','tejas.shete@ikshealth.com']
rec =  ', '.join(rec_list)
subject = 'HR BOT Run Report'

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = subject
msg['From'] = sender
msg['To'] = rec

# Create the body of the message (a plain-text and an HTML version).
text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttps://www.python.org"

# Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
#msg.attach(part1)
msg.attach(part2)

#attaching the files
filename = "output.csv"
attachment = open(r'C:\Users\tejas.shete\Desktop\Output.csv')
  
# instance of MIMEBase and named as p
p = MIMEBase('application', 'octet-stream')
  
# To change the payload into encoded form
p.set_payload((attachment).read())
  
# encode into base64
#encoders.encode_base64(p)
   
p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
  
# attach the instance 'p' to instance 'msg'
msg.attach(p)

# Send the message via local SMTP server.
server = smtplib.SMTP('smtp-relay.gmail.com:587')
server.starttls()

server.sendmail(sender,rec_list,msg.as_string())
server.quit()