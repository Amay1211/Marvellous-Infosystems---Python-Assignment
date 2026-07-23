import hashlib
import os
import validators

def validation(directoryName,interval,email):
  print(email)
  if os.path.exists(directoryName) == False or os.path.isdir(directoryName) == False: 
    print("Directory does not exists")
    return False;
  elif int(interval) <= 0:
    print("Invalid interval")
    return False
  elif validators.email(email) == False:
    print("Invalid email")
    return False
  return True


def calculateChecksum(fileName):
  fobj = open(fileName, "rb")
  buffer = fobj.read(1000)

  hobj = hashlib.md5() 

  while len(buffer) > 0:
    hobj.update(buffer)
    buffer = fobj.read(1000)

  fobj.close()

  return hobj.hexdigest()