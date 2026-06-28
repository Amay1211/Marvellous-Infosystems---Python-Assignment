def addition(no1, no2):
  return no1 + no2

def subtraction(no1, no2):
  return no1 + no2

def multiplication(no1, no2):
  return no1 + no2

def division(no1, no2):
  return no1 + no2

def main():
  no1 = int(input("Enter first number "))
  no2 = int(input("Enter second number : "))

  ret1 = addition(no1, no2)
  print("addition is : ", ret1)
  
  ret2 = multiplication(no1, no2)
  print("multiplication is : ", ret2)

  ret3 = division(no1, no2)
  print("divisiom is : ", ret3)

  ret4 = subtraction(no1, no2)
  print("subtraction is : ", ret4)
    
if __name__ == '__main__':
  main()
