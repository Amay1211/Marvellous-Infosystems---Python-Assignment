from functools import reduce

def main():
  noOfElements = int(input("Enter Number of elements"))
  data = list()

  for _ in range(noOfElements):
    no = int(input())
    data.append(no)

  ret = reduce(lambda no1, no2 : no1 if no1 > no2 else no2, data)
  print("answers is ",ret)
  
if __name__ == '__main__':
  main()
