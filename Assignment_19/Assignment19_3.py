from functools import reduce

def main():
  noOfElements = int(input("Enter Number of elements "))
  data = list()

  for i in range(noOfElements):
    no = int(input(f"enter {i} -> "))
    data.append(no)

  data1 = list(filter(lambda no: no >= 70 and no <= 90,data))
  print(data1)
  data2 = list(map(lambda no : no + 10,data1))
  product = 0

  if len(data) != 0:
    product = reduce(lambda no1, no2 : no1 * no2, data2)

  print("answers is ",product)
  
if __name__ == '__main__':
  main()
