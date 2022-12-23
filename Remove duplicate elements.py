# Remove duplicate elements from the list

l=[10,1,2,3,4,1,2,3,4]
l_uniq=[]
for ele in range(len(l)):

    if l[ele] not in l_uniq:
        l_uniq.append(l[ele])

print(l_uniq)