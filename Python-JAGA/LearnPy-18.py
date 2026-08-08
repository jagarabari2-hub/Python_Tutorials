a = int(input("Enter Number :- "))
b = int(input("Enter Number :- "))
c = a / b 
def divide(a, b):
    c = a / b
    print("This is local scope \n The Divition of ", a, "and" , b, "is", c)

divide(a, b)
print("This is global scope \n The Divition of ", a, "and" , b, "is", c)
