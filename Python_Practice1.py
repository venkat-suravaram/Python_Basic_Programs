#Q76. Write a Python program to find the factorial of a given number.
"""
The factorial of a number is the product of all the integers from 1 to that number.
For example, the factorial of 6 is 1*2*3*4*5*6 = 720. Factorial is not defined for negative numbers, and the factorial of zero is one, 0! = 1.
"""
num=6 # finding factorial of 6
factorial=1
if num<0 :
    print("-ve numbers doeesn't have factorial ")
elif  num==0:
    print("factorial of 0 is 1")
else:

    for i in range(1,num+1) :
       factorial=factorial*i # i=1 -> 1*1=1 ; i=2 -> 1*2=2 ; i=3 -> 2*3=6 ... 120*6=720
    print("factorail of 7: ", factorial)


## Q77. Write a Python program to calculate the simple interest. Formula to calculate simple interest is SI = (PRT)/100
def simple_interest(p, t, r):
    print('The principal is', p)
    print('The time period is', t)
    print('The rate of interest is', r)

    si = (p * t * r) / 100

    print('The Simple Interest is', si)
    return si
# Driver code
simple_interest(10000, 6, 7)


## Q78. Write a Python program to calculate the compound interest. Formula of compound interest is A = P(1+ R/100)^t.
def comp_interest(p, t, r):
    print('The principal is', p)
    print('The time period is', t)
    print('The rate of interest is', r)

    A=p(1+r/100)^t

    print('The comp Interest is', A)
    return A
# Driver code
simple_interest(10000, 6, 7)

##Q79. Write a Python program to check if a number is prime or not.
num = 29
# To take input from the user
#num = int(input("Enter a number: "))
# define a flag variable
flag = False
# prime numbers are greater than 1
if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break
# check if flag is True
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")

####Q80. Write a Python program to check Armstrong Number.
   # 153 = 1 * 1 * 1 + 5 * 5 * 5 + 3 * 3 * 3 // 153 is an     Armstrong   number.
# take input from the user
num = int(input("Enter a number: "))
# initialize sum
sum = 0
# find the sum of the cube of each digit
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
# display the result
if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")


################################################################### Search in Directory for pdfs
import os
def listfiles(directory_path):
    try:
        for i in os.listdir(directory_path):
            if i.endswith(".pdf"):
                print(i)
        else:
            pass
        print("nothing found")
    except Exception as e:
        print("nothing found", e)
listfiles(input("Enter directory name to list files: "))
############################################################### List all files in dict
import os
def listfiles(directory_path1):
    for x in os.listdir(directory_path1):
        print(x)
listfiles(input("Enter directory name to list files: "))

###### 1. Write a Python program to print "Hello Python"?
import logging
def HelloWorld():
    logging.basicConfig(filename="Practice_Logging.log", level=logging.INFO, format='%(asctime)s %(message)s')
    logging.info("this is my information logging")
    try:
        print ("Hello world")
    except :
        print(" Error found from hello world")
HelloWorld()

#####  2. Write a Python program to do arithmetical operations addition and division.?
import logging
def arithmatic(a,b):
    logging.basicConfig(filename="Practice_Logging.log", level=logging.INFO, format='%(asctime)s %(message)s')
    logging.info("Write a Python program to do arithmetical operations addition and division")
    try:
        print ("Add", a+b)
        print ("div", a/b)
    except :
        print(" Error found: in Arithmatic code")
arithmatic(20,30)


##### Write a Python program to swap two variables?

import logging
def swapping(a,b):
    logging.basicConfig(filename="Practice_Logging.log", level=logging.INFO, format='%(asctime)s %(message)s')
    logging.info("Write a Python program to do swapping")
    try:
        print("Before swap: ",a ,b)
        temp=a
        a=b
        b=temp
        print ("After Swap", a,b)
    except :
        print(" Error found: in swapping")
swapping(202,303)

###### Write a program to display calander
import calendar
year = 2022
month = 11
print(calendar.month(year, month))

######### Sum of a list
import logging
def sumlist(a):
    logging.basicConfig(filename="Practice_Logging.log", level=logging.INFO)
    logging.info("sum of list ")
    try:
        temp=0
        for i in a:
            temp=temp+i
        print(temp)

    except :
        print(" Error found: in sum of list")
sumlist([1,2,3,4,5])

########################### Mul of a list

import logging
logging.basicConfig(filename="Practice_Logging.log", level=logging.INFO)
logging.info("write mul of a list")

def mullist(a):
    try:
        temp=1
        for i in a:
            temp=temp*i
        print("mul value: ",temp)
    except:
        print("found error in mul list program")
mullist([1,2,3,4,5])

### Q82. Write a Python program to interchange the first and last element in a list.

def intchange(l):
    temp1 =[]
    temp2=[]
    print("list before swap of 1st and last: ", l)
    if type(l)== list:
        l1=l[0]
        llast=l[len(l)-1]
        print("first index ",l1,"\nLast Index: ",llast)
        temp1=l1
        l1=llast
        llast=temp1
        print("first index ", l1, "\nLast Index: ", llast)
        l[0]=l1
        l[len(l) - 1]=llast

    print ("list after swap 1st and last: ",l)
intchange([2,5,6,7,8])

#### Q84. Write a Python program to find N largest element from a list.
# Python program to find largest
# number in a list


def myMax(list1):

	# Assume first number in list is largest
	# initially and assign it to variable "max"
	max = list1[0]
# Now traverse through the list and compare
	# each number with "max" value. Whichever is
	# largest assign that value to "max'.
	for x in list1:
		if x > max:
			max = x
	# after complete traversing the list
	# return the "max" value
	return max
# Driver code
list1 = [10, 20, 4, 45, 99]
print("Largest element is:", myMax(list1))

