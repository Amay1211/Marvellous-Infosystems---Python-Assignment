# 2. Write a program that calculates factorials of multiple numbers
# simultaneously using Pool.map().
# Input
# [10,15,20,25]
# Display
# • Process ID
# • Input Number
# • Factorial

from multiprocessing import Pool
from os import getpid, getppid

def factorial(data):  
  print(f"Process Id - {getpid()} and parent pid - {getppid()}")
  mul = 1
  for no in range(1,data + 1):
    mul = mul * no
  return mul

def main():
  numberOfInteger = int(input("Enter number of elements"))

  data = list()
  
  for _ in range(numberOfInteger):
    data.append(int(input()))  
  
  with Pool() as pool:
    result = pool.map(factorial,data)

  print(result)

if __name__ == '__main__':
  main()

