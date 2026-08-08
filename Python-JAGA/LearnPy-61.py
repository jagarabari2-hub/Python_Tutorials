print()
print("|========================================|"
      "| Exercise 1 "
      "||========================================|")
print()
try:
    a = int(input("Enter first number :"))
    b = int(input("Enter second number :"))
    c = a/b
    print("The Multiplication of", a ,"and", b ,"is", c)
except ValueError:
    print("Invalid input! Enter non zero integer")
else:
    print("Success!")