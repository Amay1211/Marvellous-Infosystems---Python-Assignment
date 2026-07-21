# 7: Write a Python program that performs a file backup every hour.
# The program should:
# 1. Accept the source file path.
# 2. Accept the destination directory path.
# 3. Copy the source file to the destination directory.
# 4. Add the current date and time to the backup filename.
# 5. Write the backup operation details into:
# backup_log.txt
# Example backup filename:
# Data_25_07_2026_16_30_00.txt
# Example log entry:
# Backup completed successfully at 25-07-2026 04:30:00 PM
# Use the shutil module for file copying.

import schedule
import time
import datetime
import sys
import shutil
import os

def copyFile(sourceFile, destinationDirectory):
  backupTime = datetime.datetime.now()
  backFileName = f"Data_{backupTime}".replace(":","_").replace("-","_").replace(".","_") + ".txt"
  backupFileNamePath = os.path.join(destinationDirectory, backFileName)

  shutil.copy(sourceFile,backupFileNamePath)
  
  fobj = open("backup_log.txt","a")
  fobj.write(f"Backup completed successfully at {backupTime}\n")
  fobj.close()

def main():
  BORDER = '-' * 40
  print(BORDER)
  print("Marvellous automation script")
  print(BORDER)

  if(len(sys.argv) == 3):
    if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
      print("This automation use to copy the source file to the destination directory. ")
      print("For better usage please check -u flag")
    elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
      print("please execute the script as ")
      print("python fileName.py SourceFile destinationDirectory")
    else:
      schedule.every(1).hours.do(copyFile,sys.argv[1],sys.argv[2])

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
