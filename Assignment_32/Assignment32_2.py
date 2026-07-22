# 2: Write a Python program that monitors the size of a specified file
# every 30 seconds.
# Write the following details into:
# FileSizeLog.txt
# • File path
# • File size in bytes
# • Date and time
# Handle the situation where the file does not exist.

import schedule
import datetime
import os
import time

def logFileSize():
  BUFFER = "-" * 40 + "\n"
  
  currentDateTime = datetime.datetime.now()
  currentDate = currentDateTime.strftime("%d-%m-%Y")
  currentTime = currentDateTime.strftime("%H:%M:%S")
  fileName = f"FileSizeLog.txt"

  try:
    fileSize = os.path.getsize("Demo.txt")
    fobj = open(fileName,"a")
    fobj.write(f"File Size : {fileSize}\n")
    fobj.write(f"Creation time : {currentTime}\n")
    fobj.write(f"Creation date : {currentDate}\n")
    fobj.write(BUFFER)
    fobj.close()
  except FileNotFoundError as fileNotFoundError:
    print("FILE NOT FOUND ERROR : ",fileNotFoundError)
  except Exception as exception:
    print("SOMETHING WENT WRONG : ",exception)
  

def main():
  schedule.every(2).seconds.do(logFileSize)

  while True:
    schedule.run_pending()
    time.sleep(1)


if __name__ == '__main__':
  main()