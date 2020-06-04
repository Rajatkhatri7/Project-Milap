"""
Check a no is prime or not
"""

from math import sqrt
num = int(input("enter a  positive no: "))

end=int(sqrt(num))
is_prime=True
for x in range(2,end+1):
    if num%x==0:
        is_prime=False
        break
if is_prime and num!=1:
    print(f"{num} is a prime no")

else:
    print(f"{num} is not a prime no")        