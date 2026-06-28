def calculateAreaOfRectangle(length, width):
  return length *  width

def main():
  no1 = int(input("Enter first number "))
  no2 = int(input("Enter second number : "))

  ret1 = calculateAreaOfRectangle(no1, no2)
  print("Area is ", ret1)

if __name__ == '__main__':
  main()
