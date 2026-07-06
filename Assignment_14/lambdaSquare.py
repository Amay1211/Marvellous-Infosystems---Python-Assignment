square = lambda no: no * no

def main():
  value = int(input("Enter a number "))
  ret = square(value)
  print(f"Square of {value} is {ret}")

if __name__ == '__main__':
  main()
