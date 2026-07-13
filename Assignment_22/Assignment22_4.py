# 4. Write a program that calculates
# 1^5+2^5+3^5+.....+N^5
# for multiple values of N simultaneously using Pool.
# Input

# [1000000,
# 2000000,
# 3000000,
# 4000000]
# Measure total execution time.
  
from multiprocessing import Pool
from os import getpid, getppid

def multiply(data):  
  print(f"Process Id - {getpid()} and parent pid - {getppid()}")
  sum = 0
  for no in range(1,data + 1):
    sum = sum + (no ** 5)
  return sum

def main():
  numberOfInteger = int(input("Enter number of elements"))

  data = list()
  
  for _ in range(numberOfInteger):
    data.append(int(input()))  
  
  with Pool() as pool:
   result = pool.map(multiply,data)

  print(result)

if __name__ == '__main__':
  main()
