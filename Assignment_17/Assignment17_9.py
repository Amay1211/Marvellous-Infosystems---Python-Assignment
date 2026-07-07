def main():
  no = int(input("Enter first number"))
  sum = 1
  while no > 0:
    mod = no % 10
    sum = sum + 1 
    no = int((no - mod) / 10)
  
  print(sum) 
  
if __name__ == '__main__':
  main()

