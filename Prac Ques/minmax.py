#!/usr/bin/env python3 
import time

start = time.time()
def getmin(arr,n):
    return min(arr)

def getmax(arr,n):
    return max(arr)

arr = [10,88,1,9,846,496,79,3,53545,45,542,454,54,5,4,5,454,254,254,25,456,546562,0]
arr_len = len(arr)
print("min of arr is : ",getmin(arr,arr_len))
print("max of arr is : ",getmax(arr,arr_len))



print("-----------%s seconds"%(time.time()-start))

#its much better version than minmax2