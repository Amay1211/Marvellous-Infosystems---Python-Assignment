def reverNumber(no):
  temp = no
  ans = 0
  while(temp != 0):
    lastDigit = temp % 10
    ans = (ans * 10) + lastDigit
    temp = int(temp / 10)
  return ans

def main():
  str = int(input("Enter a number"))
  ret = reverNumber(str)
  print(ret)

if __name__ == '__main__':
  main()
