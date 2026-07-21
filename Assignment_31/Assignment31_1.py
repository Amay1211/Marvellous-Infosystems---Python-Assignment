# 1: Write a program that accepts:
# • A message from the user
# • A time interval in seconds
# Schedule the program to display the message repeatedly after the specified interval.
# Example input:
# Enter message: Jay Ganesh
# Enter interval in seconds: 5
# Expected output:
# Jay Ganesh
# every five seconds.

# Validate that the interval is greater than zero.

import schedule
import time
import datetime
import sys
import shutil
import os

def display(Message):
  print(Message)

def main():
  BORDER = '-' * 40
  print(BORDER)
  print("Marvellous automation script")
  print(BORDER)

  if(len(sys.argv) == 3):
    if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
      print("This automation use to Schedule the program to display the message repeatedly after the specified interval.. ")
      print("For better usage please check -u flag")
    elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
      print("please execute the script as ")
      print("python fileName.py Message interval")
    else:
      interval = int(sys.argv[2])
      schedule.every(interval).seconds.do(display,sys.argv[1])

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
