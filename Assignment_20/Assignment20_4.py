# 4: Design a Python application that creates three threads named Small, Capital, and
# Digits.
# • All threads should accept a string as input.
# • The Small thread should count and display the number of lowercase characters.
# • The Capital thread should count and display the number of uppercase characters.
# • The Digits thread should count and display the number of numeric digits.
# • Each thread must also display:
# ◦ Thread ID
# ◦ Thread Name

from threading import Thread, get_ident, current_thread
from functools import reduce

sumOfNumber = lambda no1, no2 : no1 + no2

def displayCapital(string):
  for char in string:
    if char.isupper():
      print(f"thread id : {get_ident()}, thread name : {current_thread().name}, char : {char}")

def displaySmall(string):
  for char in string:
    if char.islower():
      print(f"thread id : {get_ident()}, thread name : {current_thread().name}, char : {char}")

def displayNumbers(string):
  for char in string:
    if char.isnumeric():
      print(f"thread id : {get_ident()}, thread name : {current_thread().name}, char : {char}")

def main():
  data = "safSDFsddsfd34124sadf"
  tobj1 = Thread(target=displayCapital, args=(data,))
  
  tobj2 = Thread(target=displaySmall, args=(data,))
  
  tobj3 = Thread(target=displayNumbers, args=(data,))

  tobj1.start()
  tobj2.start()
  tobj3.start()

  tobj1.join()
  tobj2.join()
  tobj3.join()

  print("Exit from main thread")

if __name__ == '__main__':
  main()
