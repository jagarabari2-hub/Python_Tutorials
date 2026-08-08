print()
print("|========================================|"
      "| Example of syntax error "
      "||========================================|")
print()
x = 2
y = 8
z = y/x
if(z == 4):
    print("Quotient:", z)
print("Till now, the program is syntactically correct but won't be executed because of the syntax error in the next line")
print ("I will destroy everything")
print()
print("|========================================|"
      "| Example of an Exception "
      "||========================================|")
print() 
x = 2
y = 8
z = y/x
if(z == 4):
    print("Quotient:", z)
print("I shall be executed this time irrespective of the next statement")
s = int(input("Enter a number: "))
print("My execution depends on the precending statement")
print()
print("|========================================|"
      "| Implementing try and except block "
      "||========================================|")
print() 
x = 2
y = 8
z = y/x
print("Quotient:", z)
try:
    s = int(input("Enter a number: "))
    z = y/s
    print("Quotient:", z)
except ValueError:
    print("Invalid input! Enter an integer")
print()
print("|========================================|"
      "| Using multiple except blocks "
      "||========================================|")
print() 
x = 2
y = 8
z = y/x
print("Quotient:", z)
try:
    s = int(input("Enter a number: "))
    z = y/s
    print("Quotient:", z)
except ValueError:
    print("Invalid input! Enter an integer")
except ArithmeticError:
    print("Arithmetic error! Enter a non-zero integer")
print()
print("|========================================|"
      "| Using an empty except statement "
      "||========================================|")
print()
x = 2
y = 8
z = y/x
print("Quotient:", z)
try:
    s = int(input("Enter a number :"))
    z = z/s
    print("quotient is :",z)
except:
    print("Invalid input! Enter a non zero integer")
print()
print("|========================================|"
      "| Using 'else' clause with 'try-except' block "
      "||========================================|")
print()
x = 2
y = 8
z = y/x
print("Quotient:", z)
try:
    s = int(input("Enter a number :"))
    z = z/s
    print("quotient is :",z)
except:
    print("Invalid input! Enter a non zero integer")
else:
    print("Success!")
print()
print("|========================================|"
      "| Using 'finally' clause  "
      "||========================================|")
print()
x = 2
y = 8
z = y/x
print("Quotient:", z)
try:
    s = int(input("Enter a number :"))
    z = z/s
    print("quotient is :",z)
except ValueError:
    print("Invalid input! Enter a non zero integer")
except ArithmeticError:
    print("Invalid input! Divisor can't be zero")
else:
    print("Success!")
finally:
    print("I'm independant and will always be executed. HAHA")
print()
print("|========================================|"
      "| Argument of an exception  "
      "||========================================|")
print()
x = 2
y = 8
z = y/x
print("Quotient:", z)
try:
    s = int(input("Enter a number :"))
    z = z/s
    print("quotient is :",z)
except ValueError as arg:
    print("Invalid input! Enter an integer", arg)
except ArithmeticError as arg:
    print("Invalid input! Divisor can't be zero", arg)
print()
print("|========================================|"
      "| Raising an exception  "
      "||========================================|")
print()
x = int(input("Enter level :"))
try:
    if(x>10 or x<1):
        raise ValueError
    else:
        print("Wait while the game is loading...")
except ValueError:
    print("The game consits of 10 levels only ranging from 1 to 10")
print()
print("|========================================|"
      "| User-defined exception  "
      "||========================================|")
print()
class MyException(Exception):
    def __init__(self):
        self.argument = "I'm a user defined exception"
    
try:
    print("Example of a user defined exception\n----------------------------------------")
    raise MyException
except MyException:
    print(MyException().argument)