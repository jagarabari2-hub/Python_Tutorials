# Recursive Pascal Triangle

def pascal(n, r):

    if r == 0 or r == n:
        return 1

    return pascal(n - 1, r - 1) + pascal(n - 1, r)


rows = 7
cols = 7

print("\nPascal Triangle\n")

for i in range(rows):

    # Center spacing
    # print("  " * (rows - i), end="")

    # Numbers
    for j in range(i + 1):
        if(j <= i):
            print(j)
        else:
            print(" ", j)
rows = 10
cols = 20

for i in range(rows):

    for j in range(cols):
        print(j + 1, end=" ")

    print()