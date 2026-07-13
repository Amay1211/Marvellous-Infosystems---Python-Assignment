# 4: Write a program that counts how many odd numbers exist between
# 1 and N.
# Input
# Data = [1000000, 2000000, 3000000, 4000000]
# Expected Output Format
# Process ID : 1237
# Input Number : 1000000
# Odd Number Count : 500000

from multiprocessing import Pool

def countEvenNumber(data):  
  count = 0
  for no in range(data):
    if no % 2 == 0:
      count = count + 1
  return count 

def main():
  numberOfInteger = int(input("Enter number of elements"))

  data = list()

  for _ in range(numberOfInteger):
    data.append(int(input()))  
  
  pobj = Pool()

  result = pobj.map(countEvenNumber,data)

  pobj.close()
  pobj.join()

  print(result)

if __name__ == '__main__':
  main()

