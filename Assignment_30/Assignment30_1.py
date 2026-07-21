# 1: Write a Python program that prints:
# Jay Ganesh...
# every two seconds.
# Use:
# schedule.every(2).seconds.do(...)
# Expected output:
# Jay Ganesh...
# Jay Ganesh...
# Jay Ganesh...

import schedule
import time

def display():
  print("Jay Ganesh...")

def main():
  print("Authomation script started")
  schedule.every(2).seconds.do(display)

  while True:
    print("Inside the while loop")
    schedule.run_pending()
    time.sleep(3)
if __name__ == '__main__':
  main()