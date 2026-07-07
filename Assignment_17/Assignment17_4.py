def main():
  no = int(input("Enter first number"))
  ans = 0
  for i in range(1,no):
    if no % i == 0:
      ans = ans + i
  
  print(ans)

if __name__ == '__main__':
  main()
