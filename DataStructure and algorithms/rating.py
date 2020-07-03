rating = int(input("enter the rating please: "))
while rating>5 or rating<1:
	print("enter the rating between 1 and 5")
	rating = int(input())
if rating==5:
	print("thnx")
elif rating==4:
	print("improve")
else:
	feedback = input("please tell us what went wrong: ")
	print(feedback)
 
