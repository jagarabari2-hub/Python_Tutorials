print("Operations on tuples and Build in Function")
print()
lang1 = ('C', 'C++', 'C#', 'Java', 'Go', 'RUST', 'Swift', 'JavaScript')
for item in lang1:
    print(item)
lang2 = ('ASP.NET', 'PHP', 'Python', 'Ruby')
print("The remaining languages are:")
for item in lang2:
    print(item)
# Concatenation
print("After concatenation =, the final language are")
lang = lang1 + lang2
for item in lang:
    print("languages :", item)
# Repitition
wish = ('Hello',) * 4
print("Reapeating the element in tuple :", wish)
# Checking Membership
if "PHP" in lang:
    print("PHP is a language")
else:
    print("PHP is a not language")
# Slicing
print("The languages consists of", lang[5:])
# Comparing 
A = (4, 5)
print("This is a tuple A", A)
B = (5, 6)
print("This is a tuple B", B)
if A > B:
    print("The tuple A is greater than B")
elif A < B:
    print("The tuple B is greater than A")
else:
    print("The tuple A and B are equal")