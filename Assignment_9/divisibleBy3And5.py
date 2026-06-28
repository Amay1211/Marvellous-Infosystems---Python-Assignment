def divisibleByThreeAndFive(no):
  return no % 3 == 0 and no % 5

def main():
  no = int(input("Enter a number"))
  ret = divisibleByThreeAndFive(no)
  if(ret == True):
    print(ret,"is divisible by 3 and 5")
  else:
    print(ret,"is not divisible by 3 and 5")

if __name__ == '__main__':
  main()
