
# list comprehension approach
def double_1(lst):
    return [2*x for x in lst]

# recursive approach
def double_2(lst): 
    return [] if not lst else [2*lst[0]]+double_2(lst[1:])

# HOF
def double_3(lst): 
    return list(map(lambda x:2*x,lst))

print(double_3([1,2,3])) 

    