# 3: Write a Python program to implement a class named Numbers with the following
# specifications:
# • The class should contain one instance variable:
# ◦ Value
# • Define a constructor (__init__) that accepts a number from the user and initializes Value.
# • Implement the following instance methods:
# ◦ ChkPrime() – returns True if the number is prime, otherwise returns False
# ◦ ChkPerfect() – returns True if the number is perfect, otherwise returns False
# ◦ Factors() – displays all factors of the number
# ◦ SumFactors() – returns the sum of all factors
# • Create multiple objects and call all methods.

class Numbers:
  def __init__(self, value):
    self.value = value 
  
  def chkPrime(self):
    isPrime = True
    for i in range(2,self.value):
       if self.value % i == 0:
         isPrime = False
         break
    print(isPrime)

  def factors(self):
    factors = list()
    
    for i in range(1,self.value):
       if self.value % i == 0:
         factors.append(i)
    
    print(factors)
  
  def sumFactors(self):
    sum = 0
    
    for i in range(1,self.value):
       if self.value % i == 0:
         sum = sum + i
    
    print(sum)

nobj = Numbers(12)
nobj.chkPrime()
nobj.factors()
nobj.sumFactors()

nobj2 = Numbers(24)
nobj2.chkPrime()
nobj2.factors()
nobj2.sumFactors()

nobj3 = Numbers(36)
nobj3.chkPrime()
nobj3.factors()
nobj3.sumFactors()

nobj3 = Numbers(48)
nobj3.chkPrime()
nobj3.factors()
nobj3.sumFactors()

nobj3 = Numbers(60)
nobj3.chkPrime()
nobj3.factors()
nobj3.sumFactors()
