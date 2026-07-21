# 5: Schedule a task that executes every five minutes.
# The task should write the current date and time into a file named:
# Marvellous.txt
# New entries should be appended without removing previous entries.
# Example file contents:
# Task executed at: 25-07-2026 04:30:00 PM
# Task executed at: 25-07-2026 04:35:00 PM

import schedule
import time
import datetime

def display():
  fobj = open("Marvellous.txt","a") 
  fobj.write(f"Task executed at : {datetime.datetime.now()}\n")
  fobj.close()

def main():
  print("Authomation script started")
  schedule.every(5).minutes.do(display)

  while True:
    schedule.run_pending()
    time.sleep(1)

if __name__ == '__main__':
  main()