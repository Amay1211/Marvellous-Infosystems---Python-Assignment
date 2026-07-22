# 1: Write a program that creates a new text file every minute.
# The filename should contain the current timestamp.
# Example:
# File_25_07_2026_16_30_00.txt
# Write the following information into the file:
# • Filename
# • Creation date
# • Creation time

import schedule
import datetime
import os
import time

def createFile():
  currentDateTime = datetime.datetime.now()
  currentDate = currentDateTime.strftime("%d-%m-%Y")
  currentTime = currentDateTime.strftime("%H:%M:%S")
  fileName = f"File_{currentDate.replace("-","_")}_{currentTime.replace(":","_")}.txt"

  fobj = open(os.path.join("folder",fileName),"w")
  fobj.write(f"File Name : {fileName}")
  fobj.write(f"Creation time : {currentTime}")
  fobj.write(f"Creation date : {currentDate}")
  fobj.close()

def main():
  schedule.every(10).minutes.do(createFile)

  while True:
    schedule.run_pending()
    time.sleep(1)


if __name__ == '__main__':
  main()