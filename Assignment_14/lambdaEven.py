isEvenNumber = lambda no : no % 2 == 0 

def main():
  no = int(input("Enter number "))

  ret = isEvenNumber(no)
  print(f"Is number Even - {ret}")

if __name__ == '__main__':
  main()
