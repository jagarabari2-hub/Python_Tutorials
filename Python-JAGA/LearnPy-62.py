print()
print("|========================================|"
      "| Exercise 2 "
      "||========================================|")
print()
try:
    a = int(input("Enter first number :"))
    b = int(input("Enter second number :"))
    c = a * b + a + b + b + b * a
    print(c)
except ValueError:
    print("Invalid input! Enter an integer")
except ArithmeticError:
    print("Invalid input! Divisor can't be zero")