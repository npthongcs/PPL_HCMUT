# a
def lessThan(n,lst): 
    return [x for x in lst if x<n]

# b
def lessThan1(n,lst): 
    if not lst: return []
    elif lst[0]<n: return [lst[0]] + lessThan1(n,lst[1:])
    else: return lessThan1(n,lst[1:])
    
# c
def lessThan2(n,lst): 
    return list(filter(lambda x:x<n,lst))

print(lessThan2(5,[1,2,3,4,5,6,7,8,9]))