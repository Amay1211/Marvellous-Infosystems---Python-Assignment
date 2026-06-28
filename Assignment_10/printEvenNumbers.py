def main():
  no = int(input("Enter a number"))
  
  for no in range(0,no + 1):
    if(no % 2 == 0):
      print(no)

if __name__ == '__main__':
  main()
