from functools import reduce

maximum = lambda no1,no2 : no1 if no1 > no2 else no2 

def main():
  data = [11,21,51,101, 10,2,4]

  ret = reduce(maximum,data)
  print(f"minimun is {ret}")

if __name__ == '__main__':
  main()
