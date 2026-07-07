def checkPrime(no):
  isPrime = True
  for i in range(2, no):
    if(no % i == 0):
      isPrime = False
  return isPrime

def listPrime(data):
  return list(filter(checkPrime, data))
