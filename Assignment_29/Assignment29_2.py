# Q2) Display File Contents
# Problem Statement:
# Write a program which accepts a file name from the user, opens that file, and displays the entire contents on the
# console.
# Input:
# Demo.txt
# Expected Output:
# Display contents of Demo.txt on console.

import sys
import os

def countLines(fileName):
  fobj = open(fileName,"r")
  lines = fobj.readlines()
  for line in lines:
    print(line)
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
      countLines(fileName)
  else:
    print("Invalid number of arguments")
    print("Please usage --h or --u for more information")

if __name__ == "__main__":
  main()