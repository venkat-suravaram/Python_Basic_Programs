import random
options= ["rock","paper","scissors"]

comp_pick=0
while True:
  user_input = input("Enter your choice in rock,paper,scissors,q : ")
  if user_input == 'q':
   print(" your chose to QUIT ")
   quit()
  if user_input not in options:
   continue

  ran_num=random.randint(0,2)
  comp_pick=options[ran_num]
  print("User pick is: ", user_input , " computer pick is : ", comp_pick)

  if user_input=='rock' and comp_pick=='scissors' :
   print("you win")
  if user_input == 'paper' and comp_pick == 'scissors':
    print("you win")
  if user_input == 'scissors' and comp_pick == 'paper':
    print("you loose")
  if user_input==comp_pick:
   print("haaa , match")


