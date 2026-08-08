print("Implemntation of Strings")
strings = "string"
print(strings)
print([2])
print(strings[2])
print(strings[2:4])
print("List Data Type")
MyList =  [7, 78.6, 'Python']
print(MyList)
print(MyList[2])
print("Python Dictionary")
MyDict = {'id':1, 'Name':'Jaga',
'Role':'Developer'}
print(MyDict)
print(MyDict.keys())
print(MyDict.values())
print("Examples Of Tuples")
MyTuples = ('Python', 12, 12.8)
print(MyTuples)
print("Pyhon Sets")
MySet = {11,33}
print(MySet)
MySet.add(22)
print(MySet)
MySet.remove(11)
print(MySet)
print("Python FrozenSet")
FSet1 = frozenset([11,22,33,44])
print(FSet1)
FSet2 = frozenset([22,33,44,55])
print(FSet2)
FSet1.isdisjoint(FSet2)
print("Opening a file in python")
file = open("jagatest.txt","r+")
str=file.read()
print("read  string", str)
file.close()



