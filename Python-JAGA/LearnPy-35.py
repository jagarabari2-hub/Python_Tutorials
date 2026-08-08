print("| -/=================================================================================\- |")
print()
print("|==================================================================================|" 
      "| Recursive Function "
      "|==================================================================================|")
print()
def PrintNote(count):
    if count < 1:
        return
    print("Hello World From Python 3.14")
    PrintNote(count - 1)

PrintNote(5)
print()
print("|==================================================================================|"
      "| Recursive Function for calculating factorial of a number "
      "|==================================================================================|")

def fact(num):
    print(" Function called with num = " + str(num))
    if num == 1:
        return 1
    else:
        ans = num * fact(num - 1)
        print("Intermediate result for", num, "* fact(", num - 1, "):", ans)
        return ans

print("Factorial = :", fact(4))
print()
print("|==================================================================================|"
      "| Source Code Without Recursion "
      "|==================================================================================|")
print()
def calcsum(List):
    total = 0
    for flag in List:
        total = total + flag
    return total

List = [1, 3, 5, 7, 9, 11]
print("Given List is :", List)
print("Sum of list of numbers is :", calcsum(List))
print()
print()
print("|==================================================================================|"
      "| Recursive Function for Fibonacci Numbers "
      "|==================================================================================|")
print()
def rec_fib(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return rec_fib(num-1) + rec_fib(num-2)
num = 34
print("Given Number is :", num)
print("Fibonacci Number :", rec_fib(num))
print()
print("|==================================================================================|"
      "| Iterative Function for Fibonacci Numbers "
      "|==================================================================================|")
print()
def iter_fib(num):
    if num < 2:
        return num
    x,y = 0,1
    while num >1:
        z = y
        y = x + y
        x = z
        num -= 1
    return y
num = 89
print("Given Number is :",num)
print("Fibonacci Number :",iter_fib(num))
print()
print("|==================================================================================|"
      "| Fixing Recursive Function "
      "|==================================================================================|")
print()
memory = {0:0, 1:1}
def mem_fib(num):
    if not num in memory:
        memory[num] = mem_fib(num-1) + mem_fib(num-2)
    return memory[num]
num = 987
print("Given Number is :",num)
print("Fibonacci Number :",mem_fib(num))
print("| -/==================================================================================\- |")