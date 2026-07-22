def main():
  try:
    fobj = open("Demo.txt","r")
    
    print("Fle gets open")
    
    data = fobj.read(10)
    print(data)

    fobj.close()
  except FileNotFoundError as fobj:
    print("File is not present in current directory")
  
if __name__ == '__main__':
  main()
