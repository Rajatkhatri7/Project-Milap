def Maxpair(arr):
    return arr[-1]*arr[-2]

    
if __name__ == "__main__":

    print("enter the nos: ")
    inp = [int(i) for i in input().split(" ")]
    res=Maxpair(sorted(inp))
    print("max pair product is: " , res)


