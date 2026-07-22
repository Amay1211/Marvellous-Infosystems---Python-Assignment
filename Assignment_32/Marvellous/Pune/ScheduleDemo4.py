import schedule
import time
import datetime

def display():
  print("Jay Ganesh...", datetime.datetime.now())

def main():
  print("Authomation script started")

  schedule.every(10).seconds.do(display)

  while True:
    schedule.run_pending()
    time.sleep(1)

if __name__ == "__main__":
  main()

