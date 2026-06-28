def areaOfCircle(radius):
  pi = 3.14
  return 2 * pi * radius

def main():
  radius = int(input("Enter radious "))

  ret1 = areaOfCircle(radius)
  print("Area of circle is ", ret1)

if __name__ == '__main__':
  main()
