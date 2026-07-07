def main():
  no = int(input("Enter first number"))
  
  for i in range(1, no + 1):
    for j in range(1,i + 1):
      print(j, end=" ")
    print("\n")
  
if __name__ == '__main__':
  main()
