def chkGreater(no1,no2):
  if(no1 > no2):
    return no1
  else:
    return no2

def main():
  ret = chkGreater(10,20)
  print(ret,"is greate number")

if __name__ == '__main__':
  main()

