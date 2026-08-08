def subtract (a, b):
    return b - a
a=10
b=20
result = subtract(a,b)

print(result)

print("| ====================================================================== |")

# illustration of Pass-by-reference 
def referencedemo(list):
    list.append(90)
    list.append(100)
myList = [50, 60, 70, 80]
print('The initial list is : ', myList)
referencedemo(myList)
print('The final list is : ', myList)
print("| ====================================================================== |")

# Illustration of Default Arguments
def empinfo(name, age = 40, sal = 45000):
    print("Employee Name : ", name)
    print("Employee Age : ", age)
    print("Employee Salary : ", sal)
    return
empinfo(age=23, name="Christin")

print("| ====================================================================== |")

# Keyword Argument 
def key_function(a, b=25, c=40):
    print("The Value of a is :", a)
    print("The Value of b is :", b)
    print("The Value of c is :", c)
key_function(15151, 5116485, 5666484)