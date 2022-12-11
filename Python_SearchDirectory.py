
# file=open("test.txt",'w')
# file.write("write something")
# file.close()
# file=open("test.txt",'r')
# print(file.read())
# file.close()

import os
def listfile(directory_path):
    l=os.listdir(directory_path)
    print(l)
listfile(input("Enter directory to search : "))

######################################################

import os
def listfiles(directory_path1):
    for x in os.listdir(directory_path1):
        print(x)
listfiles(input("Enter directory name to list files: "))

#######################################################

import os
def listfiles(directory_path):
    try:
        for i in os.listdir(directory_path):
            if i.endswith(".pdf1"):
                print(i)
        else:
            pass
        print("nothing found")
    except Exception as e:
        print("nothing found", e)
listfiles(input("Enter directory name to list files: "))
