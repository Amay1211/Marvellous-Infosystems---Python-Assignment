# Q1) Check File Exists in Current Directory
# Problem Statement:
# Write a program which accepts a file name from the user and checks whether that file exists in the current
# directory or not.
# Input:
# Demo.txt
# Expected Output:
# Display whether Demo.txt exists or not.

import sys
import os

def checkFileExistOrNot(searchFileName):
  currentDirectory = os.curdir

  isFileExist = False
  for folderNames, subFolders, fileNames in os.walk(currentDirectory):
    if searchFileName in fileNames:
      isFileExist = True
      break
  return isFileExist

def main():
  if(len(sys.argv) == 2):
    if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
      print("For better usage please check -u flag")
    elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
      print("please execute the script as ")
      print("python fileName.py fileName")
      print("fileName name should be absoulte path")
    else:
      fileName = sys.argv[1]
      ret = checkFileExistOrNot(fileName)
      if ret == True:
        print("file exist")
      else:
        print("File not Exist")
  else:
    print("Invalid number of arguments")
    print("Please usage --h or --u for more information")

if __name__ == "__main__":
  main()