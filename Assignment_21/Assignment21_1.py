# 1: Design a Python application that creates two threads named Prime and NonPrime.
# • Both threads should accept a list of integers.
# • The Prime thread should display all prime numbers from the list.
# • The NonPrime thread should display all non-prime numbers from the list.

from threading import Thread, get_ident, current_thread

def isPrimeNumber(no):
  isPrime = True

  for i in range(2,no):
    if no % i == 0:
      isPrime = False
  
  return isPrime

def displayPrimeNumbers(data):
  for no in  data:
      if(isPrimeNumber(no)):
        print(f"thread id : {get_ident()}, thread name : {current_thread().name}, number : {no}")

def displayNonPrimeNumber(data):
  for no in data:
      if(isPrimeNumber(no) == False):
        print(f"thread id : {get_ident()}, thread name : {current_thread().name}, number : {no}")


def main():
  data = [1,2,3,4,5,6,7,8,9]
  tobj1 = Thread(target=displayPrimeNumbers, args=(data,))
  tobj2 = Thread(target=displayNonPrimeNumber, args=(data,))
  
  tobj1.start()
  tobj2.start()

  tobj1.join()
  tobj2.join()


  print("Exit from main thread")

if __name__ == '__main__':
  main()
