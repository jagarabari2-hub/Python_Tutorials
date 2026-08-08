# Arbitrary Arguments
print("| ====================================================================== |")
print(" ")

def printdetail(argt, *var):
    print("Output is : ")
    print(argt)
    for flag in var:
        print(flag)
    return; 
    # end for
# end def
printdetail(25)
printdetail(20, 85, 41098, 109848, 8949, 801484, 4801, 84894, 84844 ,59416151491, 115155847874)

print(" ")
print("| ====================================================================== |")