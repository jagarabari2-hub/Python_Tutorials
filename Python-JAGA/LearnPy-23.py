print("Built-in Functions for tuples")
print()
age1 = (26, 28, 30, 45, 75, 78, 98, 457, 454, 887, 548, 5, 32595)
print("The ages in first year are: ", age1)
print("The total number of items are: ", len(age1))
print("The maximum age in first year is: ", max(age1))
print("The minimum age in first year is: ", min(age1))
age2 = (79, 82, 100, 21, 15, 5156, 11515156, 15119899, 15118, 78994614, 44687789498)
print("The ages in second year are: ", age2)
print("The ages are saved in: ", type(age2))
age3 = tuple(age2)
print("Now, they are saved in :", type(age3))
print("The sorted ages in second year are: ", sorted(age3))
print("The total number of ages in second year are: ", sum(age3))
print()

print("Tuples as return value")
list = [('Tom', 496), ('Jerry', 784), ('Oggy', 967), ('Jack', 39748), ('Bhoot Boss', 484151666648)]
def sorting(list):
    new_list = sorted(list)
    i = len(new_list)
    first = new_list[0]
    last = new_list[i - 1]
    return (first, last)
(first, last) = sorting(list)
print("The first name in the list is: ", first)
print("The last name in the list is: ", last)