#!/usr/bin/env python3 

#reversse the array


def rev_array(arr):


    for i in range(len(arr)//2):
        temp = arr[i]
        arr[i] = arr[-(i+1)]
        arr[-(i+1)] = temp

      
    return arr
arr_size  = int(input("enter the size of array: "))
arr1 = [int(input("enter the arr element: ")) for _ in range(arr_size)]

print("reversed arr is: ", rev_array(arr1))


#Other Method 
#start = 0,end = len(arr)
#While Start<end:
#   arr[start],arr[end] = arr[end], arr[start]
#
#
#