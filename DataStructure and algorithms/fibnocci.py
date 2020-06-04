# grows via 2^n/2
# fn= {  0             ; n=0
#       1             ; n=1
#       f(n-1)+f(n-2) ; n>1}

def fib(n):
    if n<=1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

# for  f(n)>n it will take very long time to compute
# bad algo
"""
                   F(n)
                  /    \
            f(n-1)       f(n-2)
             /  \          /   \ 
        f(n-2)   f(n-3)   f(n-3) f(n-4)
        / \       /   \     /  \     /  \
        /  \      /    \    /    \ f(n-5) f(n-6)
        /   \     /     \  f(n-4) f(n-5)
    f(n-3) f(n-4) f(n-4) f(n-5)

Above we can see that we are computing same thing again(look on (f-3)) which is not required

"""


def Fastfib(n):
    f = []
    f.append(int(0))
    f.append(int(1))
    print(f)
    f[1]=1
    for i in range(2,n):
    
        f.append((f[i-1]+f[i-2]))
    print(f)
    return sum(f)

"""it takes less time it is more powerful"""


if __name__ == "__main__":
    n=int(input("enter the no: "))
    res=fib(n)
    res2=Fastfib(n)
    print(f"sum of first {n} fibnocci no is with recursion : ",res)
    print(f"sum of first {n} fibnocci no is with fastalgo : ",res2)