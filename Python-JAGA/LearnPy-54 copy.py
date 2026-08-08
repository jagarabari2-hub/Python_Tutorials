import os

myfile = open("myfile.txt", "r")
myfile.close()

# os.rename("pyex.txt", "myfile.txt")

# print("File renamed successfully")
# os.remove("student.html")
# print("File removed successfully")
# os.mkdir("mydir")
print("Directory created successfully")
os.rmdir("mydir")
print("Directory removed successfully")
os.getcwd()

