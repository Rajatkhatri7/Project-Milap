#!/usr/bin/env python3 
#!/usr/bin/env python3 
# Check whether n is present in an array of size m or not.
import time

Number = int(input("enter the no to be searched in the array: "))
arr_size = int(input("enter the size of array: "))


arr = [int(input("enter the array elements: ")) for _ in range(arr_size)]

starttime = time.time()
if Number in arr:
    print("true")
    
else:
    print("false")    

print("----------%s seconds"%(time.time()-starttime))
