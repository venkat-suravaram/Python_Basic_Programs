# Remove duplicate elements from the list

l=[10,1,2,3,4,1,2,3,4,3,3,3,3,3,3]
count=0
Search_ele=3
for i in range(len(l)):
    if (Search_ele==l[i]) :
        count=count+1

print("Actual list elements: ",l)
print("searching element :",Search_ele)
print("elements count: ",count )