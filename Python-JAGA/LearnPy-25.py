print("Implementation of operator on Dictionary")
print()
students = {
    '123': {
        'Name' : 'John Doe',
        'Ph' : '45864554',
        'Percentage' : '100%'
    },
    '456': {
        'Name' : 'Adma',
        'Ph' : '45864554',
        'Percentage' : '81%'
    },
    '789': {
        'Name' : 'DOMS',
        'Ph' : '45864554',
        'Percentage' : '55%'
    }
}
labels = {
    'Name' : 'Name of the Student',
    'Ph' : 'Phone Number',
    'Percentage' : ' Percentage'
}
print("The Total number of students are : ",len(students))
roll_no = input('Student ID : ')
req = input('Name (n) or Phone Number (ph) or Percentage (p) ? ')
if req == 'n': key = 'Name'
if req == 'ph': key = 'Ph'
if req == 'p': key = 'Percentage'
if roll_no in students:
    print("The %s with roll no: %s is %s." % (labels[key], roll_no, students[roll_no][key]))
