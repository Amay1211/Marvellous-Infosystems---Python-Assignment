# 2: Write a Python program that displays the current date and time
# after every one minute.
# Use the datetime module.
# Expected output:
# Current Date and Time: 25-07-2026 04:30:00 PM

import schedule
import datetime
import time

def display():
  print(f"Current Date and Time: {datetime.datetime.now()}")

def main():
  print("Authomation script started")
  schedule.every(1).minute.do(display)

  while True:
    print("Inside the while loop")
    schedule.run_pending()
    time.sleep(1)

if __name__ == '__main__':
  main()