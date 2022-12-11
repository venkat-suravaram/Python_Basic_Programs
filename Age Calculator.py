# Find age based on input DOB
# Using datetime we can find the age by subtracting birth year from current year. Along with this, we need to focus on the birth month and birthday. For this, we check if current month and date are less than birth month and date. If yes subtract 1 from age, otherwise 0.
import datetime

dob='2021-11-11' #input("Enter your DOB in format YYYY-MM-DD: ")

(year,month,day)=dob.split('-')
year_int=int(year)
month_int=int(month)
day_int=int(day)

today=datetime.date.today()

if (today.year >= year_int):
    age = today.year - year_int -((today.month, today.day) <(month_int, day_int))
    print( "Age: ",age)
else:
    print("Enter a correct DOB")


