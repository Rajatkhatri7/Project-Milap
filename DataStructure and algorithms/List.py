# delation and inseration takes O(n) time in array
# Behind the scenes a Python list is built as an array. 
# Even though you can do many operations on a Python list with just one line of code, there's a lot of code built in to the Python language running to make that operation possible.


#inserting into a list is easy (happens in constant time). 
# However, inserting into an array is O(n), 
# since you may need to shift elements to make space for the one you're inserting,
# or even copy everything to a new array if you run out of space. 
# Thus, inserting into a Python list is actually O(n), 
# while operations that search for an element at a particular spot are O(1)

# https://wiki.python.org/moin/TimeComplexity chk