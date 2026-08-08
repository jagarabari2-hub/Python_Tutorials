# if-else Function 
def ageTrack ():
    """
    Purpose: Age Tracking Input Function
    """
    age = int (input("Enter Your Age : "))
    
    if(age > 18):
        print("You can Vote ")
    else:
        print("You Can't Vote")
        
ageTrack()
# end def