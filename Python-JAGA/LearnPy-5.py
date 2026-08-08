print("Arithmetic Operators")
Num1 = 25
Num2 = 65
Res = Num1 + Num2
print("Addition Operator + :", Res)
Str1 = "Python"
Str2 = "Programming"
Res = Str1 + " " + Str2
print("Concatenation of two strings ")
print(Res)
Res = Num1 - Num2
print("Subtraction Operator - :", Res)
Res = Num1 * Num2
print("Multiplication Operator * :", Res)
Res = Str1 * 8
print(Res) #Repetition of a string
print("Division of two number / :", Num1/Num2)
print("Reminder of two number % :", Num1%Num2)
print("Floor Values // :", Num1//Num2)
print(" ")
print("Relational Operators")
Num1 = 745
Num2 = 456
print(" > ", Num1 > Num2)
print(" < ", Num1 < Num2)
print(" == ", Num1 == Num2)
print(" != ", Num1 != Num2)
print(" >= ", Num1 >= Num2)
print(" <= ", Num1 <= Num2)
print(" ")
X = True
Y = False
print(" AND ", X and Y)
print(" OR ", X or Y)
print(" NOT ", not Y)
print(" ")
print("Bitwise Operator")
a = 5
b = 9
print("AND ", a & b)
print("OR ", a | b)
print("NOT ", ~a)
print("XOR ", a ^ b)
print("Right Shift ", a >> b)
print("Left Shift ", a << b)
print(" ")
print("Assignment Operator")
Num = 4786
Num+=1
print(Num)
Num-=10
print(Num)
Num*=2
print(Num)
Num/=2                          
print(Num)
Num%=4
print(Num)
print(" ")
print("Membership Operator")
Str = "I Love Python Programming"
Find =  'Love' in Str
print("Love in Str : ", Find)
Str ={1: 'Jaga', 2: 'Rabari'}
Find1 = 2 not in Str
print("Not In : ", Find1)
print(" ")
print("Identity Operator")
jaga1 = ["Jaga", 123]
jaga2 = ["Rabari", 456]
F1 = jaga1 is jaga2
print("is Operator :", F1)
F2 = jaga1 is not jaga2
print("is not Operator :", F2)
print(" ")
print("Precedence Of Operators")
A = 4876
B = 8799
C = 1478
D = 5478
E = (A - B) * C
print(E)
E = A + (B * C) /D
print(E)
print(" ")
print("Program of illustrate associativity of operators")
A = 1234
B = 4567
C = 7890
print(A * B // C)
print(A * (B // C))
print((C ** B) ** C)
print(C ** B ** C)
print(" ")
print("Non-associative Operators")
V = 1
J = 1
V = J = 2
print(V)
print(J)
