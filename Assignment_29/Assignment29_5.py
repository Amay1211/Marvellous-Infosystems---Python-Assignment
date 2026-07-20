# Q5) Frequency of a String in File
# Problem Statement:
# Write a program which accepts a file name and one string from the user and returns the frequency (count of
# occurrences) of that string in the file.
# Input:
# Demo.txt Marvellous
# Expected Output:
# Count how many times "Marvellous" appears in Demo.txt.

import sys
import os

def searchWord(fileName, searchText):
  fobj = open(fileName,"r")
  lines = fobj.readlines()
  count = 0
  for line in lines:
    print(line.find(searchText), searchText)
    if line.find(searchText) != -1:
      count = count + 1
  
  print(count)
  fobj.close()

def main():
  if(len(sys.argv) == 3):
    if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
      print("For better usage please check -u flag")
    elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
      print("please execute the script as ")
      print("python fileName.py fileName")
      print("fileName name should be absoulte path")
    else:
      fileName = sys.argv[1]
      searchText = sys.argv[2]
      searchWord(fileName,searchText)
  else:
    print("Invalid number of arguments")
    print("Please usage --h or --u for more information")

if __name__ == "__main__":
  main()