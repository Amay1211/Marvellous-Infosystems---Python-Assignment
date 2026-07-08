# 2: Design a Python application that creates two threads.
# • Thread 1 should calculate and display the maximum element from an list.
# • Thread 2 should calculate and display the minimum element from the same list.
# • The list should be accepted from the user.

from threading import Thread, get_ident, current_thread
from functools import reduce

def displayMax(data):
  ret = reduce(lambda no1, no2 : no1 if no1 > no2 else no2,data, 0) 
  print("max" ,ret)
    
def displayMin(data):
  ret = reduce(lambda no1, no2 : no1 if no1 < no2 else no2,data, 0) 
  print("min" ,ret)

def main():
  data = [1,2,3,4,5,6,7,8,9]
  tobj1 = Thread(target=displayMax, args=(data,))
  tobj2 = Thread(target=displayMin, args=(data,))
  
  tobj1.start()
  tobj2.start()

  tobj1.join()
  tobj2.join()


  print("Exit from main thread")

if __name__ == '__main__':
  main()
