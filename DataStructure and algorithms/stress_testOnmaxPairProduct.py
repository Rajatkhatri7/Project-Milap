"""stress test are used to generate test cases to comeup with better solution"""

import random

def Maxpair(n,arr):
    result=0
    for i in range(1,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]*arr[j] > result:
                result = arr[i]*arr[j]   
    return result

def Maxpairfast(n,arr):
    arr2=sorted(arr)
    return arr2[-1]*arr2[-2]




if __name__ == "__main__":
    for i in range(10):

        n = random.randint(2,11)
        print("n is:" ,n)
        result = 0;fast=0
        inp=list(random.randint(0,99999) for r in range(n))
        print("inp is : ",inp)
        assert(len(inp)==n)

        
        res=Maxpair(n,inp)
        res2 = Maxpairfast(n,inp)
        if(res!=res2):
            print("wrong answer: ",res," ",res2,"\n")
        else:
            print("OK both solutions are correct: ",res," ",res2)


