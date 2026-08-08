print("| :-=========================================================================================-: |")
print(" ")
# Local and Global Variables
print("This is a example of a Scope Of Variables")
print(" ")
add = 0
def addtion(a, b):
    add = a + b
    print("This is local scope of add :-", add)
addtion(2005, 2017)
print("This is the global scope of add :-", add)
print(" ")
print("This is a Recursive Function Example")
print(" ")
def fibn(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return fibn (num-1) + fibn (num-2)
print("Fibonacci of 3 :-", fibn(3))
print("Fibonacci of 1 :-", fibn(1))
print("Fibonacci of 0 :-", fibn(0))

print(" ")
print("| :-=========================================================================================-: |")