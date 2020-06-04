"""
Guess the number

"""


import random

answer=random.randint(1,100)
counter=0

while True:
    counter=0

    while True:
        counter+=1
        num=int(input("please guess a no between 1-100"))
        if num<answer:
            print("bigger")
        elif num>answer:
            print("smaller")

        else:
            print("congratulations , you guessed it!")
            break

print("you guessed %d times in total "% counter)
if counter>7:
    print("your IQ balance is obviously insufficient")

