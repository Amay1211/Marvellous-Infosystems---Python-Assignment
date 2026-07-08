from functools import reduce

def filterPrimeNumber(no):
  isPrime = True

  for i in range(2,no):
    if no % i == 0:
      isPrime = False
  
  return isPrime

def multiplyBy2(no):
  return no * 2
  
def findMaximum(no1, no2):
  return no1 if no1 > no2 else no2 
  
def main():
  noOfElements = int(input("Enter Number of elements "))
  data = list()

  for i in range(noOfElements):
    no = int(input(f"enter {i} -> "))
    data.append(no)

  filteredPrimNumbers = list(filter(filterPrimeNumber,data))
  multiplyBy2Numbers = list(map(multiplyBy2, filteredPrimNumbers))
  product = 0
  if len(data) != 0:
    product = reduce(findMaximum, multiplyBy2Numbers)
  print("answers is ",product)
  
if __name__ == '__main__':
  main()
