# Program to find even numbers
l=[11,2,33,34,54,67,37,88]
for i in l:
    if(i%2==0):
        print (i, "is even number \n")
    else:
        print(i, "is odd number ")

"""OP:
11 is odd number 
2 is even number 

33 is odd number 
34 is even number 

54 is even number 

67 is odd number 
37 is odd number 
88 is even number 
"""


# Program to print all even numbers
l=[11,2,33,34,54,67,37,88]
even=[]
for i in l:
    if(i%2==0):
        even.append(i)
print("Even numbers list: ",even)

"""OP:
Even numbers list:  [2, 34, 54, 88]
"""


