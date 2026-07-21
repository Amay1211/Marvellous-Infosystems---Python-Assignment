# 6: Write a program that schedules the following messages:
# • Monday at 9:00 AM: Start your weekly goals
# • Wednesday at 5:00 PM: Review your weekly progress
# • Friday at 6:00 PM: Weekly work completed
# Use:
# schedule.every().monday.at(...)
# schedule.every().wednesday.at(...)
# schedule.every().friday.at(...)

import schedule
import time
import datetime

def displayWeeklyGoals():
  print("Start your weekly goals")

def displayWeeklyProgress():
  print("Review your weekly progress")

def displayWeeklyWork():
  print("Weekly work completed")

def main():
  print("Authomation script started")
  schedule.every().monday.at("13:00").do(displayWeeklyGoals)
  schedule.every().wednesday.at("17:00").do(displayWeeklyGoals)
  schedule.every().friday.at("18:00").do(displayWeeklyProgress)

  while True:
    schedule.run_pending()
    time.sleep(1)

if __name__ == '__main__':
  main()