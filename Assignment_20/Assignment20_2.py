# 2: Design a Python application that creates two threads named EvenFactor and
# OddFactor.
# • Both threads should accept one integer number as a parameter.
# • The EvenFactor thread should:
# ◦ Identify all even factors of the given number.
# ◦ Calculate and display the sum of even factors.
# • The OddFactor thread should:
# ◦ Identify all odd factors of the given number.
# ◦ Calculate and display the sum of odd factors.
# • After both threads complete execution, the main thread should display the message:
# “Exit from main”

from threading import Thread

def displayEvenFactors(no):
  for i in range(1,no):
    if no % i  == 0 and i % 2 == 0:
      print("Even factors", i)

def displayOddFactors(no):
  for i in range(1,no):
    if no % i  == 0 and i % 2 != 0:
      print("odd factors", i)

def main():
  no = 100
  tobj1 = Thread(target=displayEvenFactors, args=(no,))
  tobj2 = Thread(target=displayOddFactors, args=(no,))

  tobj1.start()
  tobj2.start()

  tobj1.join()
  tobj2.join()

  print("Exit from main thread")

if __name__ == '__main__':
  main()
