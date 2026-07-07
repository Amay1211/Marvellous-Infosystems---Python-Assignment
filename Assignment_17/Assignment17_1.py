from Arithmatics import addition,subtraction,multiplication,division

def main():
  no1 = int(input("Enter first number"))
  no2 = int(input("Enter second number"))

  ret1 = addition(no1, no2)
  ret2 = multiplication(no1, no2)
  ret3 = division(no1, no2)
  ret4 = subtraction(no1, no2)

  print(f"Addition is {ret1}")
  print(f"Multiplication is {ret2}")
  print(f"Division is {ret3}")
  print(f"Subtraction is {ret4}")
  
if __name__ == '__main__':
  main()
