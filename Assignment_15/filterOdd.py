filterOdd = lambda no :  no % 2 != 0

def main():
  data = [11,21,51,101, 10,2,4]

  ret = list(filter(filterOdd,data))
  print(f"Odd numbers {ret}")

if __name__ == '__main__':
  main()
