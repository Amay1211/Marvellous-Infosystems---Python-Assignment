def printSquare(no):
  return no * no

def main():
  no = int(input("Enter a number"))
  ret = printSquare(no)
  print(ret,"is Square")

if __name__ == '__main__':
  main()
