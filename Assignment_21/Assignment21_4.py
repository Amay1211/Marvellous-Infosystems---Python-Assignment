# 10: Design a Python application that creates two threads.
# • Thread 1 should compute the sum of elements from a list.
# • Thread 2 should compute the product of elements from the same list.
# • Return the results to the main thread and display them.

from threading import Thread
from functools import reduce
from queue import Queue

def calculateSum(data, queue):
  queue.put({"sum": reduce(lambda no1, no2 : no1 + no2, data, 0)})

def calculateProduct(data, queue):
  queue.put({"Product": reduce(lambda no1, no2 : no1 * no2, data, 1)})

def main():
  data = [1,2,3,4,5,6,7,8,9]

  queue = Queue();
  tobj1 = Thread(target=calculateProduct, args=(data,queue,))
  tobj2 = Thread(target=calculateSum, args=(data,queue,))
  
  tobj1.start()
  tobj2.start()

  tobj1.join()
  tobj2.join()

  while not queue.empty():
    print(queue.get())

  print("Exit from main thread")

if __name__ == '__main__':
  main()
