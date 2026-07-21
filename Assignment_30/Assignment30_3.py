# 3: Write a program that schedules a function to print:
# Coding Kar..!
# every 30 minutes.

import schedule
import time

def display():
  print("Coding Kar")

def main():
  print("Authomation script started")
  schedule.every(30).minute.do(display)

  while True:
    print("Inside the while loop")
    schedule.run_pending()
    time.sleep(1)
if __name__ == '__main__':
  main()