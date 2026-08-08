print("|========================================|"
      "| Fibonacci Series"
      "||========================================|")
print()
n = int(input('Enter n'))
x = i = 0
y = 1

while i < n:
    print(x)
    x = x + y
    y = x - y
    i += 1
