# 2: Write a Python program to implement a class named Circle with the following
# requirements:
# • The class should contain three instance variables: Radius, Area, and Circumference.
# • The class should contain one class variable named PI, initialized to 3.14.
# • Define a constructor (__init__) that initializes all instance variables to 0.0.
# • Implement the following instance methods:
# ◦ Accept() – accepts the radius of the circle from the user.
# ◦ CalculateArea() – calculates the area of the circle and stores it in the Area variable.
# ◦ CalculateCircumference() – calculates the circumference of the circle and stores it in
# the Circumference variable.

class Cirle:
  pi = 3.14

  def __init__(self):
    self.radius = 0.0 
    self.area = 0.0
    self.circumference = 0.0
  
  def accept(self, radius):
    self.radius = radius

  def calulateArea(self):
    self.area = Cirle.pi * self.radius * self.radius  

  def calulateCircumference(self):
    self.circumference = 2 * Cirle.pi * self.radius  
  
  def display(self):
    print(self.radius)
    print(self.area)
    print(self.circumference)
    
obj1 = Cirle()
obj1.accept(2)
obj1.calulateArea()
obj1.calulateCircumference()
obj1.display()

obj2 = Cirle()
obj2.accept(4)
obj2.calulateArea()
obj2.calulateCircumference()
obj2.display()
