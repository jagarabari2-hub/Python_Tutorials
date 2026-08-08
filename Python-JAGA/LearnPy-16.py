# Annonymous/Lambda Function Example
print("| ========================================================================================= |")
print(" ")

print("This is a Example of a Annonymous/Lambda Function")
print(" ")
average = lambda num1, num2: (num1 + num2)/2
print("Average :-", average(87481987, 32663454))

print(" ")
# filter() function for finding odd numbers
num_list = [ 6, 34, 9, 71, 23, 46, 76, 11, 13, 15, 17, 19, 21]
odd_list = list (filter (lambda num: (num%2!=0), num_list))
print("The odd numbers are: ", odd_list)

print(" ")
# map () function to add 5 to all items in a list
num1_list = [ 6, 6448, 4946, 449, 449, 41854, 48666, 15616, 164165, 378944, 2244]
print("Initial list :-", num1_list)
new_list = list (map (lambda num: num+5, num1_list))
print("New List :-", new_list)

print(" ")
print("| ========================================================================================= |")