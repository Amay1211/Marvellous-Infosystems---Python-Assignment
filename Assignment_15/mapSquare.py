square = lambda no :  no ** 2

def main():
  data = [11,21,51,101]

  ret = list(map(square,data))
  print(f"square is {ret}")

if __name__ == '__main__':
  main()
