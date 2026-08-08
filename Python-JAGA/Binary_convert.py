print("|========================================|"
      "| Convert Numbers into Binary "
      "||========================================|")
print()
alist = []
def bin_convert(num):
    if(num==0):
        return alist
    digit = num % 2
    alist.append(digit)
    bin_convert(num // 2)

Numbers = int(input("Enter a number to convert into binary: "))
bin_convert(Numbers)
alist.reverse()
print("Binary Equivalent of ", Numbers,": ")
for flag in alist:
    print(flag, end=" ")