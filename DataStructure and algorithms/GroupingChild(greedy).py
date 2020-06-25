""""
Problem is to group the childreans 
such that nay group doesn't contain 
the children with atmost 1 year age difference

"""

# brute force solution 
# 
# m= len(C) 
# for each partition into group
# C=g1 U g2 U ......gk:    # this takes 2^n times because n is total no of children and each group can either contain a chhildern or not 
#
#   good=true
#   for i from 1 to k:
#       if max(gi)-min(gi)>1:
#           good = flase
#   if good:
#       m=min(m,k)


# optial solution

""" 
Always make a mathmaticacl intuation while making a solution

for this probleam 

consider that x1,x2.......xn are the point of ages of children lying on a line 
and we need
to cover the each point with min segements of unit length such that each point will be 
covered.

        ---------.-.---------------..---------.-------------..-----------
"""


# sort the points with merge or quick sort O(nlogn) time and store it in list A

PointsCoverSorted(A):
    R = {},i=1
    while i<=n:
        l,r=x[i],x[i+1]    # starting the segement from the leftmost point on the line 
        R= R U{l,r}
        i=i+1                   # assuming that there will be optimal solution
        while i<=n and x[i]<=r: # checking point is covered or not 
            i=i+1
    return R
"""

i from 1 to n O(n)
 sorting running time O(nlogn)

 overall O(nlogn)
"""


