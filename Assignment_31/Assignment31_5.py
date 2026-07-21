# 5:Write a program that accepts a directory name from the user and
# counts the number of files inside it every five minutes.
# Write the result into:
# DirectoryCountLog.txt
# Each entry should contain:
# • Directory path
# • Number of files
# • Date and time

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

  fobj = open("DirectoryCountLog.txt","a")
  fobj.write(f"Directory Scanned : {os.path.abspath(dirName)}\n")
  fobj.write(f"Total Files : {fileCount}\n")
  fobj.write(f"Total Subdirectories : {folderCount}\n")
  fobj.write(f"Scan Time : {datetime.datetime.now()}\n\n")

def main():
  BORDER = '-' * 40
  print(BORDER)
  print("Marvellous automation script")
  print(BORDER)

  if(len(sys.argv) == 2):
    if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
      print("This automation use to accepts a directory name from the user and counts the number of files inside it every five minutes.")
      print("For better usage please check -u flag")
    elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
      print("please execute the script as ")
      print("python fileName.py DirectoryName")
    else:
      schedule.every(5).seconds.do(scanDirectory,sys.argv[1])

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
