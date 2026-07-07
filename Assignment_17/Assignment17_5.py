def main():
  no = int(input("Enter first number"))
  isPrime = True
  for i in range(2,no):
    if no % i == 0:
     isPrime = False
     break
  
  print(isPrime)

if __name__ == '__main__':
  main()
