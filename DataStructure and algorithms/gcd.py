#euvlidian algo
# gcd(a,b)=gcd(a',b)=gcd( b,a')


def gcd(a,b):
    if b==0:
        return a
    a1= a%b # a1 is reminder 
            # as gcd  of reminder obained by dividing  a  by b  is same as as gcd of a,b
            # because as by division property "a = a1+bq" something that divides a1 will also divide a   

    return gcd(b,a1)

    
if __name__ == "__main__":
    a,b= input("enter two no's : ").split()
    res = gcd(int(a),int(b))
    print(res)

"""run time  = O(ab) becoz everytime in calculating reminder we r reducing the no by a factor of 2"""  


