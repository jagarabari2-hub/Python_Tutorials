# Calculating squre of a number
def square (num):
    sq = num * num
    result = ('The square of {} is {}.'). format(num,sq)
    print(result)
# function call
def main ():
    square (125)
    square (78456)
    input1 = int (input("Enter Number : "))
    square (input1)
main()