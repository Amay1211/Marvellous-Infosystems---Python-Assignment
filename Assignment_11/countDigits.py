def countDigits(no):
  temp = no
  count = 0
  while(temp != 0):
    count = count + 1    
    temp = int(temp / 10)
  return count

def main():
  no = int(input("Enter a number"))
  ret = countDigits(no)
  print(ret)

if __name__ == '__main__':
  main()
