# 4. Design automation script which accept directory name and mail id from user and create log
# file in that directory which contains information of running processes as its name, PID,
# Username. After creating log file send that log file to the specified mail.
# Usage : ProcInfoLog.py Demo Marvellousinfosystem@gmail.com
# Demo is name of Directory.
# marvellousinfosystem@gmail.com is the mail id.

import os
import sys
import psutil
import time
import schedule
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib

def sendEmail(fileName,receiverEmail):
  SMTP_USER="example@gmail.com"
  SMTP_APP_PASSWORD="password"
  SMTP_RECEIVER_EMAIL = receiverEmail

  # instance of MIMEMultipart
  msg = MIMEMultipart("alternative")

  # storing the senders email address  
  msg['From'] = SMTP_USER

  # storing the receivers email address 
  msg['To'] = SMTP_RECEIVER_EMAIL

  # storing the subject 
  msg['Subject'] = f"Directory Cleaner Automation - Report {time.strftime("%d_%m_%Y_%H_%M_%S")}"

  part1 = MIMEText(f'''
    <!DOCTYPE html>
    <html>
    <head>
        <link rel="stylesheet" type="text/css" hs-webfonts="true" href="https://fonts.googleapis.com/css?family=Lato%7CLato:i,b,bi">
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style type="text/css">
          h1{"font-size:56px"}
          h2"{"font-size:28px;font-weight:900"}
          p{"font-weight:100"}
          td{"vertical-align:top"}
          #email{"margin:auto;width:600px;background-color:#fff"}
        </style>
    </head>
    <body bgcolor="#F5F8FA" style="width: 100%; font-family:Lato, sans-serif; font-size:18px;">
    <div id="email">
        <table role="presentation" width="100%">
            <tr>
                <td bgcolor="#00A4BD" align="center" style="color: white;">
                    <h1> Jay Ganesh...</h1>
                </td>
        </table>
    </div>
    </body>
    </html>''', 'html')

  msg.attach(part1)
  # open the file to be sent 
  attachment = open(filePath, "rb")

  # instance of MIMEBase and named as p
  p = MIMEBase('application', 'octet-stream')

  # To change the payload into encoded form
  p.set_payload((attachment).read())

  # encode into base64
  encoders.encode_base64(p)
  
  filename = fileName
  p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

  # attach the instance 'p' to instance 'msg'
  msg.attach(p)

  # creates SMTP session
  s = smtplib.SMTP('smtp.gmail.com', 587)

  # start TLS for security
  s.starttls()

  # Authentication
  s.login(SMTP_USER, SMTP_APP_PASSWORD)

  # Converts the Multipart msg into a string
  text = msg.as_string()

  # sending the mail
  s.sendmail(SMTP_USER, SMTP_RECEIVER_EMAIL, text)

  # terminating the session
  s.quit()
  
def processScan():
  listProcess = []

  for proc in psutil.process_iter():
    info = proc.as_dict(attrs=["name","pid", "status"])
    listProcess.append(info)
  return listProcess

def procInfo(folderName, ProcessName, receiverEmail):
  BORDER = "-" * 50
  RUNNING_STATUS = "runnig"
  ret = False
  ret = os.path.exists(folderName)

  if ret == True:
    ret = os.path.isdir(folderName)
    if(ret == False):
      print("Unable to process as directory name is exist not its not a directory")
      return
  else:
    os.mkdir(folderName)
    print("Directory for log file gets created successfully")

  timeStamp = time.strftime("%Y-%m-%d_%H-%M-%S")
  fileName = os.path.join(folderName,"Marvellous_%s.log" %timeStamp)
  fobj = open(fileName,"w")
  print(f"Log file gets created sucessfully with name {fileName}")

  fobj.write(BORDER + "\n")
  fobj.write("----Marvellous Platform Survillence System----\n")
  fobj.write(f"Log file gets created : {timeStamp}\n")
  fobj.write(BORDER + "\n\n")

  data = processScan()
  runnigProcess = list(filter(lambda data: data["name"] == ProcessName, data))
  for info in runnigProcess:
    fobj.write("PID: %s\n" %info.get("pid"))
    fobj.write("Name: %s\n" %info.get("name"))
    fobj.write("Status: %s\n" %info.get("status"))
    fobj.write(BORDER + "\n\n")

  fobj.write("-------------------------System Report------------------------\n")
  fobj.write("\n\n\n\n\n\n\n\n\n\n\n\n\n")
  fobj.write(BORDER + "\n\n")
  fobj.write("-------------------------End of log fle-----------------------\n")
  fobj.write(BORDER + "\n\n")

  fobj.close()

  sendEmail(fileName, receiverEmail)

def main():
  BORDER = "-" * 50
  print(BORDER)
  print("----Welcome to proc info system")
  print(BORDER)

  if(len(sys.argv) == 2):
    if sys.argv[1] == "--h" or sys.argv[1] == "--H":
      print("This automation script is use to perform")
      print("1 : It fetch the information of running processes")
      print("2 : it maintain all recorsd in to log file")
      print("3 :  it send log file through main periodically")
    elif sys.argv[1] == "--u" or sys.argv[1] == "--U":
      print("Use the automation script as : ")
      print(f"python {sys.argv[0]} timeInterval folderName processName")
      print("timeIntval :  Time interval in minutes for periodic execution")
      print("folderName : Name of log file folder")
      print("ProcessName : Name of process")
      print("Email of Receiver :  Email id of receiver")
    else:
      print("Unable to proceed as there is not maching args")
    pass
  # actual project code
  elif(len(sys.argv) == 4):
    print("Schedular started sucessfully")
    print("Press ctrl + C to abort the automation script")
    procInfo(sys.argv[2], sys.argv[3])
    schedule.every(int(sys.argv[1])).minutes.do(procInfo,sys.argv[2], sys.argv[3], sys.argv[4])
    while True:
      schedule.run_pending()
      time.sleep(1)

  else:
    print("Invalid number of arguments")
    print("Unable to proceed as argument are not maching")
    print("Please use --u or --h flag for more getting information")

  print(BORDER)
  print("----Thank you for using our automation system")
  print(BORDER)
  

if __name__ == "__main__":
  main()