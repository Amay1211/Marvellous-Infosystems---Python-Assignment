# 3. For every number in the given list, count how many prime numbers
# exist between 1 and N using multiprocessing Pool.
# Example
# 10000
# 20000
# 30000
# 40000
# Display total prime count for each number.
  
from multiprocessing import Pool
from os import getpid, getppid

def countPrimNumber(data):  
  print(f"Process Id - {getpid()} and parent pid - {getppid()}")
  count = 0
  for no in range(2,data + 1):
    isPrime = True
    for i in range(2,no):
       if no % i == 0:
         isPrime = False
         break
    if isPrime == True:
      count = count + 1
  
  return count

def main():
  numberOfInteger = int(input("Enter number of elements"))

  data = list()
  
  for _ in range(numberOfInteger):
    data.append(int(input()))  
  
  with Pool() as pool:
   result = pool.map(countPrimNumber,data)

  print(result)

if __name__ == '__main__':
  main()

