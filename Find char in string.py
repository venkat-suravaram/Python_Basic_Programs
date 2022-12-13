s = "ABCDEFGHsTUV"
searching_char = 's'
count = int(0)
for i in s:

    if i == searching_char:
        print("Searching char position: ", s.index(i))
        count = count + 1

print("no.of chars found: ", count)