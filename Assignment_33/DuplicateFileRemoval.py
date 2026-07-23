import sys
import schedule
import os
import datetime
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from constants import BORDER
from utils import validation, calculateChecksum



def sendEmail(receiverEmail , fileName,filePath, currentDateTime, completionTime,directoryName, totalNumberOfFileScanned, totalNumberOfDuplicates, totalNumberOfDuplicatesDelete):
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
  msg['Subject'] = f"Directory Cleaner Automation - Report {currentDateTime.strftime("%d_%m_%Y_%H_%M_%S")}"

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
        <table role="presentation" border="0" cellpadding="0" cellspacing="10px" style="padding: 30px 30px 30px 60px;">
            <tr>
                <td>
                    <h2>Custom stylized email</h2>
                    <p>Starting time of scanning:{currentDateTime}</p>
                    <P>Completion time of scanning: {completionTime}</p>
                    <P>Directory scanned: {directoryName}</p>
                    <P>Total number of files scanned : {totalNumberOfFileScanned}</p>
                    <P>Total number of duplicate files found: {totalNumberOfDuplicates}</p>
                    <P>Total number of duplicate files deleted: {totalNumberOfDuplicatesDelete}</p>
                </td>
            </tr>
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

def duplicateFileRemovalTask(directoryName, email):
  logFolderName = "Logs"

  if os.path.exists(logFolderName) == False or os.path.isdir(logFolderName) == False:
    os.mkdir("Logs")
  
  currentDateTime = datetime.datetime.now()
  fileName = f"DuplicateFileRemovalLog_{currentDateTime.strftime("%d_%m_%Y_%H_%M_%S")}.txt"
  filePath = os.path.join(logFolderName,fileName)
  fobj = open(filePath,"a")
  fobj.write(f"Starting Time Of Directory Scanning : {currentDateTime.strftime("%d_%m_%Y_%H_%M_%S")}\n")
  fobj.write(f"Name of Directory Scan : {directoryName}\n")
  
  checkSumList = set()
  totalNumberOfFileScanned = 0
  totalNumberOfDuplicates = 0
  totalNumberOfDuplicatesDelete = 0

  for folderName, subFolder, fileNames in os.walk(directoryName):
    for fName in fileNames:
      totalNumberOfFileScanned = totalNumberOfFileScanned + 1
      absolutePath = os.path.abspath(os.path.join(folderName,fName))
      checkSum = calculateChecksum(absolutePath)
      if checkSum in checkSumList:
        totalNumberOfDuplicates = totalNumberOfDuplicates + 1
        totalNumberOfDuplicatesDelete = totalNumberOfDuplicatesDelete + 1
        fobj.write(f"Delete file with checksum: {checkSum} and path : {absolutePath}\n")
        os.remove(absolutePath)
      else:
        checkSumList.add(checkSum)

  completionTime = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
  fobj.write(f"Total Number of files Scanned : {totalNumberOfFileScanned}\n")
  fobj.write(f"Total Number of duplicates: {totalNumberOfDuplicates}\n")
  fobj.write(f"Total Number of duplicated deleted : {totalNumberOfDuplicatesDelete}\n")
  fobj.write(f"Completion Time Of Directory Scanning : {completionTime}\n")

  fobj.close()

  sendEmail(email, fileName,filePath,  currentDateTime, completionTime, directoryName, totalNumberOfFileScanned, totalNumberOfDuplicates, totalNumberOfDuplicatesDelete)

def scheduleDuplicateFileRemoval(directoryName,intervalInMinutes, email):
  # intervalInMinutes
  schedule.every(5).seconds.do(duplicateFileRemovalTask, directoryName, email)

  while True:
    schedule.run_pending()
    time.sleep(1)

def main():
  print(BORDER)
  print("DUPLICATE FILE REMOVAL AUTOMATION SCRIPT")
  print(BORDER)

  argvLength = len(sys.argv)

  if(argvLength == 4):
    argv1 = sys.argv[1]
    argv2 = sys.argv[2]
    argv3 = sys.argv[3]

    if(argv1 == "--h" or argv1 == "--H" or argv1 == "--help" or argv1 == "--HELP" ):
      print("This automation script is use to deletes all empty files from a specified directory every hour.")
      print("For better usage please check -u flag")
    elif(argv1 == "--u" or argv1 == "--U" or argv1 == "--usage" or argv1 == "--U"):
      print("please execute the script as ")
      print("python fileName.py DirectoryName IntervalInMinutes Email")
      print("Directory name should be absoulte path")
    else:
      # sendEmail()
     if(validation(argv1,argv2,argv3)):
      directoryName = argv1
      intervalInMinutes = int(argv2)
      email = argv3
      scheduleDuplicateFileRemoval(directoryName, intervalInMinutes, email)
     else:
       print("Invalid arguments")  
  else:
    print("Invalid number of arguments")
    print("Please usage --h or --u for more information")

  print(BORDER)
  print("Thanks you of using Duplicate file removal automation script")
  print(BORDER)

if __name__ == "__main__":
  main()
  