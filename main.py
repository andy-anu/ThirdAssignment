def checkEquality(one,two,three):
    one = int(one)
    two = int(two)
    three = int(three)

    if(one == two):
        return True
    elif(two == three):
        return True
    elif(three == one):
        return True
    else:
        return False

Equal=checkEquality(6,5,"5")
if(Equal == True):
    print("Two values entered are equal")
else:
    print("Two values entered are not equal")


