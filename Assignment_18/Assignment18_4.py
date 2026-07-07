from MarvellousNum import listPrime

def main():
  noOfElements = int(input("Enter Number of elements "))
  data = list()

  for i in range(noOfElements):
    no = int(input(f"enter {i} -> "))
    data.append(no)


  ret = listPrime(data)

  print("answers is ",ret)
  
if __name__ == '__main__':
  main()
