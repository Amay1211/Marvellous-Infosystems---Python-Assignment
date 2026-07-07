def main():
  no = int(input("Enter first number"))
  sum = 0
  while no > 0:
    mod = no % 10
    sum = sum + mod
    no = int((no - mod) / 10)
  
  print(sum) 
  
if __name__ == '__main__':
  main()

