def main():
  no = int(input("Enter a number"))
  
  sum = 0
  for i in range(1,no):
    sum = sum + i
  
  print("sum is : ", sum)

if __name__ == '__main__':
  main()
