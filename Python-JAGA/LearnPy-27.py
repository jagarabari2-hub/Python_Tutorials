from copy import deepcopy

print("Dictionary All Functions")
print()
print("String Formatting")
print()
fav_animal = {'Alex': 'Dog', 'Bob': 'Cat', 'Charlie': 'Rabbit'}
print("The favourite animal of %s is %s." % ('Alex', fav_animal['Alex']))
print()
print("Methods in Dictionary")
print()
emp_details = {
    'Name' : 'John Doe',
    'Age' : 30,
    'Department' : 'IT'
}
emp_new = emp_details.copy()
print("The copied dictionary is : ", emp_new)
emp_new['Name'] = 'Adam'
print("The original dictionary is : ", emp_details)
print("The updated dictionary is : ", emp_new)
print()
emp_deep = deepcopy(emp_details)
emp_deep['Name'] = 'DOMS'
print("The original dictionary is : ", emp_details)
print("The updated dictionary is : ", emp_deep)
print()
{}.fromkeys(['a', 'b', 'c'], 0)
print() 
dict.fromkeys(['a', 'b', 'c'], 0)
print() 
print(emp_details.get('Name', 'Not Found'))
print()
marks = {'name': 'Jaga', 'marks': 95, 'Zoology': 85, 'grade': 'A', 'percentage': '95%', 'status': 'Pass', 'remarks': 'Excellent', 'attendance': '90%'}
print(marks.items())
print(marks.keys())
print(marks.values())
print()
marks.pop('Zoology')
print(marks)
marks.popitem()
print(marks)
marks.setdefault('Physics', 'unknown')
print(marks.get('Physics'))
marks['Physics'] = 90
print(marks)
print()
new_marks = {'Chemistry': 88, 'Biology': 92, 'English': 89, 'History': 91}
marks.update(new_marks)
print(marks)
