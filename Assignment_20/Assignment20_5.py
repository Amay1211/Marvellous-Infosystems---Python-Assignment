# 5: Design a Python application that creates two threads named Thread1 and Thread2.
# • Thread1 should display numbers from 1 to 50.
# • Thread2 should display numbers from 50 to 1 in reverse order.
# • Ensure that:
# ◦ Thread2 starts execution only after Thread1 has completed.
# • Use appropriate thread synchronization

from threading import Thread, get_ident, current_thread

def display():
  for i in range(1, 10 + 1):
      print(f"thread id : {get_ident()}, thread name : {current_thread().name}, number : {i}")

def displayReverse():
  for i in range(10,0,-1):
      print(f"thread id : {get_ident()}, thread name : {current_thread().name}, number : {i}")

def main():
  tobj1 = Thread(target=display)
  
  tobj2 = Thread(target=displayReverse)
  
  tobj1.start()
  tobj1.join()

  tobj2.start()
  tobj2.join()


  print("Exit from main thread")

if __name__ == '__main__':
  main()
