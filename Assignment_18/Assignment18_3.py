from functools import reduce

def main():
  noOfElements = int(input("Enter Number of elements"))
  data = list()

  for _ in range(noOfElements):
    no = int(input())
    data.append(no)

  elementToSearch = int(input("Enter the number to search "))

  ret = len(list(filter(lambda no: no == elementToSearch, data)))
  print("answers is ",ret)
  
if __name__ == '__main__':
  main()
