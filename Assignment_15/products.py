from functools import reduce

product = lambda no1,no2 : no1 * no2

def main():
  data = [1,2,3,4,5]

  ret = reduce(product,data)
  print(f"product is {ret}")

if __name__ == '__main__':
  main()
