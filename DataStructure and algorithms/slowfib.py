
def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)

if __name__ == "__main__":
    n=int(input("enter the no: "))
    res=fib(n)
  
    print(f"sum of first {n} fibnocci no is with recursion : ",res)
