print()
print("|========================================|"
      "| Prime Nnumbers Series "
      "||========================================|")
print()
class MyClass:
    def primeNum(self,p):
        primeSeries = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        if p not in primeSeries:
            print("This is not Prime Number")
        else:
            print("This is a Prime Number")
obj = MyClass()
obj.primeNum(int(input("Enter Number :")))
