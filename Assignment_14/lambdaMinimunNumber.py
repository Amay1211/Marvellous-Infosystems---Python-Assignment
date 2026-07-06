findMinNumber = lambda no1,no2 : no1 if no1 < no2 else no2

def main():
  no1 = int(input("Enter first number "))
  no2 = int(input("Enter second number "))

  ret = findMinNumber(no1, no2)
  print(f"min number is {ret}")

if __name__ == '__main__':
  main()
