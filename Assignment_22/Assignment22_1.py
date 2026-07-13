# 1. Write a program that accepts a list of integers and uses Pool.map()
# to calculate the sum of squares from 1 to N for every element in the
# list.
# Example Input
# [1000000,2000000,3000000,4000000]
# Expected Output
# [333333833333500000,
# 2666668666667000000,
# ...
# ]

from multiprocessing import Pool
from os import getpid, getppid

def sumOfSquares(data):  
  print(f"Process Id - {getpid()} and parent pid - {getppid()}")

  sum = 0
  for no in range(data):
    sum = sum + no
  return sum 

def main():
  numberOfInteger = int(input("Enter number of elements"))

  data = list()

  for _ in range(numberOfInteger):
    data.append(int(input()))  
  
  with Pool() as pool:
    result = pool.map(sumOfSquares,data)

  print(result)

if __name__ == '__main__':
  main()

