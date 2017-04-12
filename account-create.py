import boto.iam
import string
import random
import subprocess
import smtplib
import time
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

def generate_pass(pass_length):
  password = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(pass_length))
  return password

def user_create(email_id):
  username = email_id[:-13]
  password = generate_pass(8)
  user = conn.create_user(username)
  conn.create_login_profile(username,password)
  conn.add_user_to_group("ManagerTraining",username)
  print "Created user %s" %username
  send_email(username,password)

def send_email(username,password):
  toaddr = username+"@ggktech.com"
  print "Sending email to %s" %toaddr
  fromaddr = "<<ENTER EMAIL ID HERE>>"
  msg = MIMEMultipart()
  msg['From'] = fromaddr
  msg['To'] = toaddr
  msg['Subject'] = "AWS Login Credentials"
  body = """Here are your AWS login credentials for todays session.
  Login url: https://ggk1.signin.aws.amazon.com/console
  Account: ggk1
  Username: %s
  Password: %s
  """ % (username,password)
  msg.attach(MIMEText(body, 'plain'))
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.starttls()
  sender_pass = ""
  with open('password') as p:
    for line in p:
      sender_pass = line
  server.login(fromaddr, sender_pass)
  text = msg.as_string()
  server.sendmail(fromaddr, toaddr, text)
  server.quit()

conn = boto.iam.connect_to_region("universal")

with open('emails') as f:
  for line in f:
    user_create(line)
  f.close()
