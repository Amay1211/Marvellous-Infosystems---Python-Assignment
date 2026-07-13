# 2: Write a Python program to implement a class named BankAccount with the following
# requirements:
# • The class should contain two instance variables:
# ◦ Name (Account holder name)
# ◦ Amount (Account balance)
# • The class should contain one class variable:
# ◦ ROI (Rate of Interest), initialized to 10.5
# • Define a constructor (__init__) that accepts Name and initial Amount.
# • Implement the following instance methods:
# ◦ Display() – displays account holder name and current balance
# ◦ Deposit() – accepts an amount from the user and adds it to balance
# ◦ Withdraw() – accepts an amount from the user and subtracts it from balance
# (Ensure withdrawal is allowed only if sufficient balance exists)
# ◦ CalculateInterest() – calculates and returns interest using formula:
# Interest = (Amount * ROI) / 100
# • Create multiple objects and demonstrate all methods.

class BankAccount:
  ROI = 10.5

  def __init__(self, name, initialAmt):
    self.name = name
    self.amount = initialAmt

  def display(self):
    print(f"Name : {self.name} and ammount : {self.amount}")
  
  def deposit(self, depositAmt):
    self.amount = self.amount + depositAmt

  def withdraw(self, withdrawAmt):
    self.amount = self.amount - withdrawAmt

  def calculareInterest(self):
    intereast = (BankAccount.ROI * self) % 100
    print("Interest : ", intereast)  
    
bobj1 = BankAccount("Amay", 10000)
bobj1.display()
bobj1.deposit(100)
bobj1.display()
bobj1.withdraw(50)
bobj1.display()


bobj2 = BankAccount("Rahul", 50000)
bobj2.display()
bobj2.deposit(12000)
bobj2.display()
bobj2.withdraw(50)
bobj2.display()
bobj2.deposit(100)
bobj2.display()
bobj2.withdraw(5000)
bobj2.display()

