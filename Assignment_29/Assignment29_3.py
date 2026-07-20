# Q3) Copy File Contents into a New File (Command Line)
# Problem Statement:
# Write a program which accepts an existing file name through command line arguments, creates a new file
# named Demo.txt, and copies all contents from the given file into Demo.txt.
# Input (Command Line):
# ABC.txt
# Expected Output:
# Create Demo.txt and copy contents of ABC.txt into Demo.txt.

import sys
import os

def copyFile(fileName,copyFileName):
  fobj1 = open(fileName,"r")
  lines = fobj1.readlines()
    
  fobj2 = open(copyFileName,"w")
  fobj2.writelines(lines)

  fobj1.close()
  fobj2.close()

def main():
  if(len(sys.argv) == 3):
    if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
      print("For better usage please check -u flag")
    elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
      print("please execute the script as ")
      print("python fileName.py fileName1 fileName2")
      print("fileName name should be absoulte path")
    else:
      fileName = sys.argv[1]
      copyFileName = sys.argv[2]
      copyFile(fileName,copyFileName)
  else:
    print("Invalid number of arguments")
    print("Please usage --h or --u for more information")

if __name__ == "__main__":
  main()