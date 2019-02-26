"""
This is the solution for the Homework #4: Lists
Solution 1

"""

print("Solution 1 : Assignment on Lists")

myUniqueList = []
myLeftovers = []

print(myUniqueList)

def addToList(value) :
    result = False
    if(value in myUniqueList) :
        myLeftovers.append(value)
    else :
        myUniqueList.append(value)
        result = True
    return result

print(addToList(1))
print(addToList(2))
print(addToList(2))
print(addToList("Deepak"))
print(addToList("Deepak"))
print(addToList(3.2))
print(addToList(6))
print(addToList(1))
print(addToList(1))

print("myUniqueList : ", myUniqueList)
print("myLeftovers : ", myLeftovers)




