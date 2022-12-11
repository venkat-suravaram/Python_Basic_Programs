"""Given an array containing a range of numbers from 0 to n with a missing number, find the missing number in the input array."""
def findmissing(l):
    numbers=list(l)
    length=len(l)
    output=[]
    for i in range(1,l[-1]): # with in range index 1 to last (l[-1])
        if i not in numbers:
            output.append(i)
    return output
print(findmissing([1,2,3,4,6,7,9,10,11,14]))

"""OP: [5, 8, 12, 13] """
