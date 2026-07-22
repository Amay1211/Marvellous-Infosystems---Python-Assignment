# 3: Write a program that reads and displays the contents of a specified
# text file every minute.
# Handle the following conditions:
# • File does not exist
# • File is empty
# • Permission is denied
# • File cannot be opened

import schedule
import datetime
import os
import time

def logFileSize():
  fileName = "Demo.txt"

  if os.path.exists(fileName) and os.path.isfile(fileName):
    if os.path.getsize("Demo.txt") != 0:
      try:
        fobj = open(fileName,"r")
        buffer = fobj.read()
        print(buffer)
      except ValueError as valueError:
        print("Invalid mode : ", valueError)
      except Exception as exception:
        print("Some thing went wrong : ", exception)
    else:
      print("File is empty")
  else:
    print("File Not Exists")

def main():
  schedule.every(2).seconds.do(logFileSize)

  while True:
    schedule.run_pending()
    time.sleep(1)


if __name__ == '__main__':
  main()