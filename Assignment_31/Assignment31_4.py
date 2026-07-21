# 4: Write a program that creates a new log file after every ten minutes.
# The filename should contain the current date and time.
# Example:
# MarvellousLog_25_07_2026_16_30_00.txt
# The file should contain:
# Log file created successfully.
# Creation Time: 25-07-2026 04:30:00 PM

import schedule
import time
import datetime
import sys
import shutil
import os

def logFiles(destinationDirectory):
  backupTime = datetime.datetime.now()
  backFileName = f"MarvellousLog_{backupTime}".replace(":","_").replace("-","_").replace(".","_") + ".txt"
  backupFileNamePath = os.path.join("Marvellous", backFileName)
  print(backupFileNamePath)
  
  fobj = open(backupFileNamePath,"a")
  fobj.write(f"Log file created successfully{backupTime}\n")
  fobj.write(f"Creation time : {backupTime}\n")
  fobj.close()

def main():
  BORDER = '-' * 40
  print(BORDER)
  print("Marvellous automation script")
  print(BORDER)

  if(len(sys.argv) == 2):
    if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
      print("This automation use to copy the source file to the destination directory. ")
      print("For better usage please check -u flag")
    elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
      print("please execute the script as ")
      print("python fileName.py destinationDirectory")
    else:
      schedule.every(5).seconds.do(logFiles,sys.argv[1])

      while True:
        schedule.run_pending()
        time.sleep(1)
  else:
    print("Invalid number of arguments")
    print("Please usage --h or --u for more information")

  print(BORDER)
  print("Thanks you of using Marvellous automation script")
  print(BORDER)


if __name__ == "__main__":
  main()
