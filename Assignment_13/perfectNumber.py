def checkPerfectNumber(no):
  sum = 0;

  for i in range(1, no):
    if(no % i == 0):
      sum = sum + i
      print(sum)

  return sum == no

def main():
  no = int(input("Enter number "))

  ret = checkPerfectNumber(no)

  if(ret == True):
    print("Number is Perfect", )
  else:
    print("Number is not perfect")

if __name__ == '__main__':
  main()
