isEvenNumber = lambda no : no % 5 == 0 

def main():
  data = [11,21,51,101, 10,2,4,5,120]

  ret = list(filter(isEvenNumber,data))
  print(f"minimun is {ret}")

if __name__ == '__main__':
  main()
