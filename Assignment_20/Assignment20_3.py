# 3: Design a Python application that creates two threads named EvenList and OddList.
# • Both threads should accept a list of integers as input.
# • The EvenList thread should:
# ◦ Extract all even elements from the list.
# ◦ Calculate and display their sum.
# • The OddList thread should:
# ◦ Extract all odd elements from the list.
# ◦ Calculate and display their sum.
# • Threads should run concurrently.

from threading import Thread
from functools import reduce

sumOfNumber = lambda no1, no2 : no1 + no2

def displayEvenSum(data):
  result = reduce(sumOfNumber,list(filter(lambda no: no % 2 == 0, data)),0)  
  print(result)

def displayOddSum(data):
  result = reduce(sumOfNumber,list(filter(lambda no: no % 2 != 0, data)), 0)  
  print(result)

def main():
  data = [1,2,3,4,5,6,7,8,9,10]
  tobj1 = Thread(target=displayEvenSum, args=(data,))
  tobj2 = Thread(target=displayOddSum, args=(data,))

  tobj1.start()
  tobj2.start()

  tobj1.join()
  tobj2.join()

  print("Exit from main thread")

if __name__ == '__main__':
  main()
