# 6: Write a script that schedules the following tasks:
# • Print Lunch Time! every day at 1:00 PM.
# • Print Wrap up work every day at 6:00 PM.
# Both tasks should be handled by separate functions.

import schedule
import time
import datetime

def displayLunchTime():
  print("Lunch Time")

def displayWrapUp():
  print("Wrap Up")

def main():
  print("Authomation script started")
  schedule.every().days.at("13:00").do(displayLunchTime)
  schedule.every().days.at("18:00").do(displayWrapUp)

  while True:
    schedule.run_pending()
    time.sleep(1)

if __name__ == '__main__':
  main()