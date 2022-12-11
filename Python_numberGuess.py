import random
range_num =  input("Enter a number: ")

if range_num.isdigit():
    range_num = int(range_num)
    randam_num = random.randint(0,range_num)
    print("Random number is: ", randam_num)
elif range_num <= 0 :
    print("Enter a valid positive number")
else:
    print("please type a number next time")
    quit()
guess=0
while True:
    guess=guess+12
    user_guess = int(input("Enter a random guess number: "))
    if user_guess == randam_num :
        print("you got it! ")
        break
    else:
        print("you got it wrong - correct is: ",randam_num)
print("you got it in ",guess," guesses")
  # keep asking the user until the guess is correct
# Enter a number: 2
# Random number is:  1
# Enter a random guess number: 1
# you got it!
