def Fastfib(n):
    f = []
    f.append(int(0))
    f.append(int(1))
    print(f)
    f[1]=1
    for i in range(2,n+1):
    
        f.append((f[i-1]+f[i-2]))
    print(f)
    return f[n]


if __name__ == "__main__":
    n=int(input("enter the no: "))
    
    res=Fastfib(n)
    
    print(f"sum of first {n} fibnocci no is with fastalgo : ",res)    