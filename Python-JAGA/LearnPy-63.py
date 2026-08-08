print()
print("|========================================|"
      "| Exercise 3 "
      "||========================================|")
print()
try:
    a = input("Enter a Value :")
    if(a == "anger"):
        raise ValueError
    print("The Value is :", a)
except ValueError:
    print("anger word is prohibited")