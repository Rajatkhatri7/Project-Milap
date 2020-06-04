"""The daffodil number is also called super complete number invariant number, narcissistic number, self power, and Armstrong number.
 It is a three-digit number, and the sum of the cubes of the digits in each digit of the number is exactly equal to itself. : $ 1 ^ 3 + 5 ^ 3 + 3 ^ 3 = 153 $."""


number= int(input("enter a positive no: "))

low=number%10
mid=number//10%10
high=number//100

if number==low**3+mid**3+high**3:
    print(f"yes {number} is a daffodil no ")

else:
    print("IT is not a daffodils n0")    