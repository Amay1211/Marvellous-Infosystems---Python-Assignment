# 5: Write a program that deletes all empty files from a specified
# directory every hour.
# The program should:
# • Scan the directory recursively
# • Detect files whose size is zero bytes
# • Delete the empty files
# • Store deleted file paths in a log file
# • Handle permission errors
# Test the program only on a sample directory.

import sys
import os
import schedule
import time

def deleteEmptyFiles(directoryPath):
  fobj = open("DeleteFileLogs.txt","a")

  for folderName, subfolder, fileName in os.walk(directoryPath):
    for fName in fileName:
      filePath = os.path.join(folderName, fName)
      absolutePath = os.path.abspath(filePath)
      size = os.path.getsize(filePath)
      if size == 0:
        fobj.write(f"{absolutePath}\n")
        os.remove(filePath)
  fobj.close()

def main():
  BORDER = '-' * 40
  print(BORDER)
  print("Marvellous automation script")
  print(BORDER)

  if(len(sys.argv) == 2):
    if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
      print("This automation script is use to deletes all empty files from a specified directory every hour.")
      print("For better usage please check -u flag")
    elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
      print("please execute the script as ")
      print("python fileName.py DirectoryName")
      print("Directory name should be absoulte path")
    else:
     schedule.every(1).hours.do(deleteEmptyFiles,sys.argv[1])

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