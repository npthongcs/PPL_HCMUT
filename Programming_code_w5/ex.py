from functools import reduce
# List Comprehension
def lessThan1(list,n):
    return [x for x in list if x<n]

# HOF
def lessThan(n,alist):
    return list(filter(lambda x:x<n,alist))

#print(lessThan(4,[1,2,3,4,5,6]))

# recursive
def lstSquare1(n): 
    return [] if n<1 else lstSquare1(n-1) + [n*n]

#print(lstSquare1(4))

def lstSquare(n): 
    return [x*x for x in range(n+1) if x!=0]

#print(lstSquare(4))

def flatten1(lst): 
    return [] if not lst else lst[0]+flatten1(lst[1:])

#print(flatten1([[1,2,3],[4,5],[6]]))

def flatten(lst): 
    if not lst: return [] 
    else: return list(reduce(lambda x,y:x+y,lst))

#print(flatten([]))

def increase(a): return a+1
def square(b): return b*b
def compose(*arg): 
    return reduce(lambda g,h: lambda x:g(h(x)),arg,lambda x:x)

f=compose(increase,increase,square)
print(f(3))

    
