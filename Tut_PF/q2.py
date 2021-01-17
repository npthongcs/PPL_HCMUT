from functools import reduce
# a
def flatten(lst): 
    return [i for x in lst for i in x]

# re
def flatten1(lst): 
    return [] if not lst else lst[0]+flatten1(lst[1:])

# HOF
def flatten2(lst):
    return list(reduce(lambda x,y: x+y,lst))

print(flatten([[1,2,3],[4,5,6],[7,8]]))