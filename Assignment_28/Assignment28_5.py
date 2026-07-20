# Q5) Search a Word in File
# Problem Statement:
# Write a program which accepts a file name and a word from the user and checks whether that word is present in
# the file or not.
# Input:
# Demo.txt Marvellous
# Expected Output:
# Display whether the word Marvellous is found in Demo.txt or not.

import sys
import os

def searchWord(fileName, searchText):
  fobj = open(fileName,"r")
  lines = fobj.readlines()
  isWordFound = False
  for line in lines:
    print(line.find(searchText), searchText)
    if line.find(searchText) != -1:
      isWordFound = True
      break

  if isWordFound:
    print("Word found")
  else:
    print("Word not found")

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