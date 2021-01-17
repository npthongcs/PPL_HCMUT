import math

class Rational:
    def __init__ (self, n=0, d=1):
        assert(d!=0)
        g = math.gcd(abs(n),abs(d))
        self.numer = int(n/g)
        self.denom = int(d/g)
    
    def __str__(self): 
        return str(self.numer) + "/" + str(self.denom)
        
    def __add__ (self, number):
        typeNumber = type(number).__name__
        if typeNumber == 'int':
            return self.addRational(Rational(number))
        elif typeNumber == 'Rational':
            return self.addRational(number)
        
    def addRational (self,num): 
        assert(type(num).__name__ == 'Rational')
        return Rational(self.numer*num.denom+self.denom*num.numer, self.denom*num.denom)
    
obj = Rational(2,3)
obj = obj+3
print(obj)
        