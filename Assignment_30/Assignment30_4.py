# 4: Create a task that executes every day at 9:00 AM and prints:
# Namskar...
# Use:
# schedule.every().day.at(“09:00").do(...)

import schedule
import time

def display():
  print("Namaskar")

def main():
  print("Authomation script started")
  schedule.every().days.at("22:30").do(display)

  while True:
    schedule.run_pending()
    time.sleep(1)

if __name__ == '__main__':
  main()