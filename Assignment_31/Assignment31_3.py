# 3: Write a program that scans a specified directory every minute.
# The task should display:
# • Directory name
# • Number of files
# • Number of subdirectories
# • Date and time of scanning
# Use the os module.
# Example output:
# Directory Scanned: E:/Data
# Total Files: 15
# Total Subdirectories: 4
# Scan Time: 25-07-2026 04:30:00 PM

import schedule
import time
import datetime
import sys
import shutil
import os

def scanDirectory(dirName):
  fileCount = 0
  folderCount = 0

  for folderName, subFolders, fileName in os.walk(dirName):
    fileCount = fileCount + len(fileName)
    folderCount = folderCount + len(subFolders)

  print(f"Directory Scanned : {os.path.abspath(dirName)}")
  print(f"Total Files : {fileCount}")
  print(f"Total Subdirectories : {folderCount}")
  print(f"Scan Time : {datetime.datetime.now()}")

def main():
  BORDER = '-' * 40
  print(BORDER)
  print("Marvellous automation script")
  print(BORDER)

  if(len(sys.argv) == 2):
    if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
      print("This automation use to scans a specified directory every minute.")
      print("For better usage please check -u flag")
    elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
      print("please execute the script as ")
      print("python fileName.py DirectoryName")
    else:
      schedule.every(1).seconds.do(scanDirectory,sys.argv[1])

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
