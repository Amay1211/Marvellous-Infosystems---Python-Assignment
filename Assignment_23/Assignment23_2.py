# 2: Write a Python program using multiprocessing.Pool to calculate the
# sum of all odd numbers from 1 to N.
# Input
# Data = [1000000, 2000000, 3000000, 4000000]
# Expected Task
# For each number N, calculate:

# 1 + 3 + 5 + ... + N
# Expected Output Format

# Process ID : 1235
# Input Number : 1000000
# Sum of Odd Numbers : 250000000000

from multiprocessing import Pool

def sumOfOdd(data):  
  sum = 0
  for no in range(data):
    if no % 2 != 0:
      sum = sum + no
  return sum 

def main():
  numberOfInteger = int(input("Enter number of elements"))

  data = list()

  for _ in range(numberOfInteger):
    data.append(int(input()))  
  
  pobj = Pool()

  result = pobj.map(sumOfOdd,data)

  pobj.close()
  pobj.join()

  print(result)

if __name__ == '__main__':
  main()

