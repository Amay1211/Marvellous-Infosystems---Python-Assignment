isEvenNumber = lambda no : no % 5 == 0 

def main():
  no = int(input("Enter number "))

  ret = isEvenNumber(no)
  print(f"Is Divisble By Five - {ret}")

if __name__ == '__main__':
  main()
