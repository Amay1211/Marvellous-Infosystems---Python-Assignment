def main():
  inputNo = int(input("Enter a char : "))
  
  for no in range(1,inputNo + 1):
    if(inputNo % no == 0):
      print(no)
    
if __name__ == '__main__':
  main()
