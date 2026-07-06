def isDivisibleBy5(no):
  return no % 5 == 0

def main():
  no = int(input("Enter number"))
  ret = isDivisibleBy5(no)
  print(ret)
  
if __name__ == '__main__':
  main()
