def printCube(no):
  return no * no * no

def main():
  no = int(input("Enter a number"))
  ret = printCube(no)
  print(ret,"is cube")

if __name__ == '__main__':
  main()
