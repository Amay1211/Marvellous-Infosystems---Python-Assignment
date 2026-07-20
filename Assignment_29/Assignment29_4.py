# Q4) Compare Two Files (Command Line)
# Problem Statement:
# Write a program which accepts two file names through command line arguments and compares the contents of
# both files.
# • If both files contain the same contents, display Success
# • Otherwise display Failure
# Input (Command Line):
# Demo.txt Hello.txt
# Expected Output:
# Success OR Failure

import sys
import hashlib


def compareFiles(fileName1, fileName2):
  fobj1 = open(fileName1,"rb")
  buffer1 = fobj1.read(1000)
  hobj1 = hashlib.md5()

  while len(buffer1) > 0:
    hobj1.update(buffer1)
    buffer1 = fobj1.read(1000)

  fobj2 = open(fileName2,"rb")
  buffer2 = fobj2.read(1000)
  hobj2 = hashlib.md5()

  while len(buffer2) > 0:
    hobj2.update(buffer2)
    buffer2 = fobj2.read(1000)


  print(fileName1, fileName2)
  fobj1.close()
  fobj2.close()

  return hobj1.hexdigest() == hobj2.hexdigest()

def main():
  if(len(sys.argv) == 3):
    if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
      print("For better usage please check -u flag")
    elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
      print("please execute the script as ")
      print("python fileName.py fileName1 fileName2")
      print("fileName name should be absoulte path")
    else:
      fileName1 = sys.argv[1]
      fileName2 = sys.argv[2]
      ret = compareFiles(fileName1, fileName2)
      if ret:
        print("Same file")
      else:
        print("Not a same file")
  else:
    print("Invalid number of arguments")
    print("Please usage --h or --u for more information")

if __name__ == "__main__":
  main()