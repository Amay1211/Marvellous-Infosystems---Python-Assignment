cube = lambda no: no ** 3

def main():
  value = int(input("Enter a number "))
  ret = cube(value)
  print(f"Cube of {value} is {ret}")

if __name__ == '__main__':
  main()
