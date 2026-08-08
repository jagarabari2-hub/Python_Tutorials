# Calculating Simple Interest Using Pyhon
P = input('Enter Principal : ')
R = input('Enter Rate : ')
T = input('Enter Time In Years : ')
P = int(P)
R = int(R)
T = int(T)
SI = (P*R*T)/100
print('Principal : ', P)
print('Rate of interest : ', R)
print('Time : ', T)
print('Simple Interest : ', SI)
