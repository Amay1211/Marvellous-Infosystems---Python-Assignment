def main():
  no = int(input("Enter first number"))
  ans = 1
  for i in range(1,no + 1):
    ans = ans * i
  
  print(ans)

if __name__ == '__main__':
  main()
