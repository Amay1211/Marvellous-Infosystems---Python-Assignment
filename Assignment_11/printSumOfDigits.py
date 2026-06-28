def sumOfDigits(no):
  sum = 0

  for digit in str(no):
    sum = sum + int(digit)
  
  return sum

def main():
  no = int(input("Enter a number"))
  ret = sumOfDigits(no)
  print(ret)

if __name__ == '__main__':
  main()
