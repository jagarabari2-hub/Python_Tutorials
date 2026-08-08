print("List and Tuples - Managing Data Systemetically")
print(" ")
mylist = ['Jaga',123, 'John',24, 'Kim',31]
myList2 = ['HTML', 'CSS', 'JavaScript', 'Bootstrap', 'jQuery', 'JSON', 'AJAX', 'PHP', 'Laravel', 'Python']
myList3 = ['dellist', 'dellist element', 'test', 1, 1, 1, 2, 7, 8, 1, 1, 'element']
print("Accessing the item with index 4 :", mylist[4])
print(" ")
print("Updating List")
mylist[3] = 25
print("The Updated List is :", mylist)
print(" ")
print("Concatemsting String")
Concatenated_list = mylist+myList2
print("Result of Concatenating ", Concatenated_list)
print(" ")
print("Reapeating List")
ReapetedList = myList2*2
print("List has been repeated :", ReapetedList)
print(" ")
print("Calculating String Length")
print("The Length of list is :", len(myList2))
print(" ")
print("Deleting List and element")
print(myList3)
del myList3[2]
print("List Element After Delete", myList3)
print(" ")
print("List Slices")
print(mylist[1:3])
print(myList2[2:6])
print(myList3[3:5])
print(" ")
print("List Method")
print(" ")
print("append() method")
myList3.append('MySQL')
print(myList3)
print(" ")
print("Count() method")
myList3.count(1)
print(myList3)
print(" ")
print("Extend Method")
myList3.extend(myList2)
print(myList3)
print(" ")
print("index() method")
myList3.index(1)
print(myList3)
print(" ")
print("Remove method")
myList3.remove('element')
print(myList3)
print(" ")
print("Reverse Method")
myList3.remove(2)
print(myList3)
print(" ")
print("Sort Method")
myList2.sort()
print(myList2)
print(" ")
print("List Aliasing")
list1 = [125, 47, 4848, 448, 484, 64, 484, 444, 444, 4, 4, 44, 6, 498, 48, 4498, 48]
print("The Sorted List is :", list1)
list2 = list1
print("After Alising the List is :", list2)
list2[10] = 66
print("List After changes in list 2 :", list1)
print(" ")
print("List Cloning")
list3 = list1[:]
print("The Cloned List is :", list3)
list3[10] = 88
print("List After changes in list 3 :", list1)  
print(" ")
print("List Comnprehension")
squares = [x**2 for x in range(10)]
print("The List of Squares is :", squares)
print(" ")
print("Creating a Tuples")
myTuple = ('Jaga',123, 'John',24, 'Kim',31)
print("The Tuple is :", myTuple)    
print(" ")
print("Accessing the item with index 4 :", myTuple[4])
print(" ")
print("Updating Tuple")
try:    myTuple[3] = 25
except TypeError:    print("Tuples are immutable, cannot be updated")
print(" ")
print("Concatemsting String")
Concatenated_tuple = myTuple + ('HTML', 'CSS', 'JavaScript')
print("Result of Concatenating ", Concatenated_tuple)   
print(" ")
print("Reapeating Tuple")
Reapeted_tuple = myTuple * 2
print("Tuple has been repeated :", Reapeted_tuple)
print(" ")
print("Calculating Tuple Length")
print("The Length of tuple is :", len(myTuple))
print(" ")
print("Deleting Tuple and element")
try:    del myTuple[2]
except TypeError:    print("Tuples are immutable, cannot be deleted")








































































































































