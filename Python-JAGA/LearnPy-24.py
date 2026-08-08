print("Creating a Dictionary")
print()
D1 = {}
print(D1)
D2 = {"Ricky" : "Manager", "Sia" : "Singer", "Simon" : "Producer", "Helly" : "Teachger", "Maggie" : "Chef", "John" : "Developer", "Java" : "Script"}
print(D2)
print(D2.keys())
print(D2.values())
print()
print("Use dict() Function")
animals = dict()
print(animals)
values = [('Lion','Wild'), ('Dog','Domestic'), ('Elephant','Wild'), ('Rabbit','Domestic'), ('Cow','Domestic')]
animals = dict(values)
print("Dictionary Created :",animals)
info = dict(name = 'Victor Von Doom', position = 'Scientist, Magisition')
print(info)
print()
print("Accessing a Dictionary")
study_details = dict()
study_details[156] = 'Parallax Scroll'
print("Dictionary :", study_details)
study_details[450] = 'GSAP'
print("Dictionary :", study_details)
print(study_details[156])
print(study_details[450])
print()
print("Deleting a Dictionary")
print("Dictionary Created :", D2)
del D2["Java"]
# Cleating a dictionary 
# D2.clear()
# print(D2)
# Deleating a Whole Dictionary
# del D2