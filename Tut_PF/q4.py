from functools import reduce

def square(x):
    return x*x

def increase(x): 
    return x+1

def double(x):
    return 2*x

def compose(*arg): 
    return reduce(lambda g,h: lambda x:g(h(x)),arg,lambda x:x)

def identity(x):
    return x

def compose2(*arg): 
    if arg:
        func = compose2(*arg[1:])
        return lambda x:arg[0](func(x)) 
    else: return identity

n = compose2(square,increase,double)
print(n(4))