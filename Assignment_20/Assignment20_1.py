# 1: Design a Python application that creates two separate threads named Even and Odd.
# • The Even thread should display the first 10 even numbers.
# • The Odd thread should display the first 10 odd numbers.
# • Both threads should execute independently using the threading module.
# • Ensure proper thread creation and execution.

from threading import Thread

def displayEven():
  count = 1
  no = 1
  while count != 10:
    if no % 2 == 0:
      print(f"even {count} -> " , no)
      count = count + 1
    no = no + 1


def displayOdd():
  count = 1
  no = 1
  while count != 10:
    if no % 2 != 0:
      print(f"odd {count} -> " , no)
      count = count + 1
    no = no + 1

def main():
  tobj1 = Thread(target=displayEven)
  tobj2 = Thread(target=displayOdd)

  tobj1.start()
  tobj2.start()

  tobj1.join()
  tobj2.join()

if __name__ == '__main__':
  main()
