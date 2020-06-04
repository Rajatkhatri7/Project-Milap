"""If the input is a leap year , output True;otherwise False"""

year = int(input("please enter the year: "))


is_leap = year%4==0 and year%100!=0 or year%400==0

print(is_leap)