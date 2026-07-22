# 4: Write a program that copies all .txt files from one directory to
# another every ten minutes.
# The program should:
# • Accept source and destination directories
# • Validate both directories
# • Copy only .txt files
# • Maintain a log of copied files
# • Avoid terminating if one file cannot be copied

import sys
import os
import schedule
import time
import shutil

def copyFiles(sourceFolder, destinationFolder):
  fobj = open("CopyFileLogs.txt","a")

  for folderName, subfolder, fileName in os.walk(sourceFolder):
    for fName in fileName:
      filePath = os.path.join(folderName, fName)
      absolutePath = os.path.abspath(filePath)
      if filePath.endswith(".txt"):
        shutil.copy(absolutePath,destinationFolder)
        absolutePathInDestination = os.path.join(destinationFolder,fName)
        fobj.write(f"File copied from {absolutePath} to {absolutePathInDestination}\n")

  fobj.close()

def main():
  BORDER = '-' * 40
  print(BORDER)
  print("Marvellous automation script")
  print(BORDER)

  if(len(sys.argv) == 3):
    if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
      print("This automation script is use to Write a program that copies all .txt files from one directory to another every ten minutes.")
      print("For better usage please check -u flag")
    elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
      print("please execute the script as ")
      print("python fileName.py sourceFolderName destinationFolderName")
      print("Directory name should be absoulte path")
    else:
     schedule.every(5).seconds.do(copyFiles,sys.argv[1], sys.argv[2])

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