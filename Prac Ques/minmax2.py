#!/usr/bin/env python3
import time

start = time.time()

def getMin(arr, n): 
    res = arr[0] 
    for i in range(1,n): 
        res = min(res, arr[i]) 
    return res 
  
# Maximum Function 
def getMax(arr, n): 
    res = arr[0] 
    for i in range(1,n): 
        res = max(res, arr[i]) 
    return res 
  
# Driver Program 
arr = [10,88,1,9,846,496,79,3,53545,45,542,454,54,5,4,5,454,254,254,25,456,546562,0]

n = len(arr) 
print ("Minimum element of array:", getMin(arr, n)) 
print ("Maximum element of array:", getMax(arr, n)) 

print("-----------%s seconds"%(time.time()-start))