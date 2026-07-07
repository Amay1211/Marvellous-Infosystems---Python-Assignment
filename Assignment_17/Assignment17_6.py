def main():
  no = int(input("Enter first number"))
  
  for i in range(no,0,-1):
    for _ in range(i):
      print("*", end=" ")
    print("\n")
  
if __name__ == '__main__':
  main()
