#seek(kuthe, kuthun)
#kuthun : 0/1/2


def main():
  try:
    fobj = open("Demo.txt","r")
    print("File gets open")
    
    fobj.seek(10,0)
    data = fobj.read()
    print(data)
    
    fobj.close()
  
  except FileNotFoundError as fobj:
    print("File is not present in current directory")
  
if __name__ == '__main__':
  main()
