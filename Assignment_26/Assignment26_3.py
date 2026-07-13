# 3: Write a Python program to implement a class named Arithmetic with the following
# characteristics:
# • The class should contain two instance variables: Value1 and Value2.
# • Define a constructor (__init__) that initializes all instance variables to 0.
# • Implement the following instance methods:
# ◦ Accept() – accepts values for Value1 and Value2 from the user.
# ◦ Addition() – returns the addition of Value1 and Value2.
# ◦ Subtraction() – returns the subtraction of Value1 and Value2.
# ◦ Multiplication() – returns the multiplication of Value1 and Value2.
# ◦ Division() – returns the division of Value1 and Value2 (handle division by zero
# properly).

# • Create multiple objects of the Arithmetic class and invoke all the instance methods.

class Arithmetic:
  def __init__(self):
    self.value1 = 0 
    self.value2 = 0
  
  def accept(self, value1, value2):
    self.value1 = value1
    self.value2 = value2

  def addition(self):
    return self.value1 + self.value2  

  def subtraction(self):
    return self.value1 - self.value2  
  
  def multiplication(self):
    return self.value1 * self.value2  

  def divison(self):
    try:
      return self.value1 / self.value2 
    except ZeroDivisionError as zobj:
      print("second input should not be zero", zobj)

aobj1 = Arithmetic()
aobj1.accept(3,4)
print(aobj1.addition())
print(aobj1.multiplication())
print(aobj1.divison())
print(aobj1.subtraction())

aobj1.accept(4,3)
print(aobj1.addition())
print(aobj1.multiplication())
print(aobj1.divison())
print(aobj1.subtraction())
