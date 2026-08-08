# This is a return in function example
def CitizenInfo():
    Name = input("Enter Your Name : ")
    Age = int (input("Enter Your Age : "))
    if (Age > 18):
        print("Eligible To Vote")
    else:
        print("Not Eligible To Vote") 
CitizenInfo()