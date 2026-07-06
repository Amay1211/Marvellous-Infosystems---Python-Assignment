from functools import reduce

addition = lambda no1,no2 : no1 + no2

def main():
  data = [11,21,51,101, 10,2,4]

  ret = reduce(addition,data)
  print(f"square is {ret}")

if __name__ == '__main__':
  main()
