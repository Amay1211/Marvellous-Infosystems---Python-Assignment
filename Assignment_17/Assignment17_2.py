def main():
  no = int(input("Enter first number"))

  for _ in range(no):
    for _ in range(no):
      print("*",end=" ")
    print("\n")
 
if __name__ == '__main__':
  main()
