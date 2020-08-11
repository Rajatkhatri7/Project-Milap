

# step-1 we grab the element from the index=no of rotation to performed
# upto the last element and put them in new array
# step-2 then grab the remaing element from 0 to index=no of rotation to performed and append them to new arr
# Ex- [1,2,3,4,5] operation =2 it will be [3,4,5,1,2]
def leftrotate(a,d):


    rotate_index = d
    i=0
    rotated_arr = [None]*len(a) #[None,None,NoneNone]



    '''

    Dont do rotated_arr = []
    while (rotate_index<len(a)): # step1
        rotated_arr[i] = a[rotate_index]
        i+=1
        rotate_index+=1
    

    #itgive  will give list index out of range error
    becoz we cant assign a value at index which doesnt exist
    ,we can only assign a value at index if there is already a value so
    we only can append 

    The thing to realise is that a list object will not allow you to assign a value to an index that doesn't exist.
    
    '''


    while (rotate_index<len(a)): # step1
        rotated_arr[i] = a[rotate_index]
        i+=1
        rotate_index+=1

    rotate_index=0   #step2
    while (rotate_index<d):
        rotated_arr[i] = a[rotate_index]
        i+=1
        rotate_index+=1


    return rotated_arr


if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))
    result = leftrotate(a,d)
    
    print(result)