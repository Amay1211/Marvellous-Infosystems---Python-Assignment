def main():
  no = int(input("Enter number"))
  i = 0
  temp = 2
  while(i != no):
    if temp % 2 == 0:
      print(temp)
      i = i + 1
    temp = temp + 1
    
  
if __name__ == '__main__':
  main()
