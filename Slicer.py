# email slicer
#string.strip([chars]) to slice any char
message = input("enter something: ").strip()
print(message)
def slicer():
    email = input("Enter Your Email: ").strip() #The strip() method # remove leading and trailing whitespaces

    username = email[:email.index('@')]
    domain = email[email.index('@') + 1:]

    print(f"Your username is {username} & domain is {domain}")
slicer()

# Slice string based on cahr ;
message=input("Enter string for slice: ")
firstname=message[:message.index(';')]
lastname=message[message.index(';')+1:]
print(f"Full name is {firstname} {lastname}")