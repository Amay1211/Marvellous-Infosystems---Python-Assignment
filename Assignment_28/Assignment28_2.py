# Q2) Count Words in a File
# Problem Statement:
# Write a program which accepts a file name from the user and counts the total number of words in that file.
# Input:
# Demo.txt
# Expected Output:
# Total number of words in Demo.txt.

import sys
import os

def countWords(fileName):
  fobj = open(fileName,"r")
  numberOfLines = len(fobj.read())
  print(f"Number of lines in {fileName} is {numberOfLines}")
  fobj.close()

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
      countWords(fileName)
  else:
    print("Invalid number of arguments")
    print("Please usage --h or --u for more information")

if __name__ == "__main__":
  main()