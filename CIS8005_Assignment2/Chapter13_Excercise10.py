''' Chapter 13 Excercise 10 '''

class Rational:
    def __init__(self, numerator = 1, denominator = 0):
        divisor = gcd(numerator, denominator)       
        self.__numerator = (1 if denominator > 0 else -1) \
            * int(numerator / divisor)
        self.__denominator = int(abs(denominator) / divisor)
        if self.__denominator == 0:
            raise ZeroDivisionError("Divided by 0")

    # Add a rational number to this rational 
    def __add__(self, secondRational):
        n = self.__numerator * secondRational[1] + \
            self.__denominator * secondRational[0]
        d = self.__denominator * secondRational[1]
        if d == 0:
            raise ZeroDivisionError("Divided by 0")
        return Rational(n, d)

    # Subtract a rational number from this rational 
    def __sub__(self, secondRational):
        n = self.__numerator * secondRational[1] - \
            self.__denominator * secondRational[0]
        d = self.__denominator * secondRational[1]
        if d == 0:
           raise ZeroDivisionError("Divided by 0")
        return Rational(n, d)

    # Multiply a rational number to this rational 
    def __mul__(self, secondRational):
        n = self.__numerator * secondRational[0]
        d = self.__denominator * secondRational[1]
        if d == 0:
           raise ZeroDivisionError("Divided by 0")
        return Rational(n, d)

    # Divide a rational number from this rational */
    def __div__(self, secondRational):
        n = self.__numerator * secondRational[1]
        d = self.__denominator * secondRational[0]
        if d == 0:
           raise ZeroDivisionError("Divided by 0")
        return Rational(n, d)

    def __truediv__(self, secondRational):
        return self.__div__(secondRational)
    
    # Return a float for the rational number
    def __float__(self):
        return self.__numerator / self.__denominator 

    # Return a integer for the rational number
    def __int__(self):
        return int(self.__float__())

    # Return a string representation  
    def __str__(self):
        if self.__denominator == 1:
            return str(self.__numerator)
        else:
            return str(self.__numerator) + "/" + str(self.__denominator)

    def __lt__(self, secondRational): 
        return self.__cmp__(secondRational) < 0

    def __le__(self, secondRational): 
        return self.__cmp__(secondRational) <= 0

    def __gt__(self, secondRational): 
        return self.__cmp__(secondRational) > 0

    def __ge__(self, secondRational): 
        return self.__cmp__(secondRational) >= 0
   
    # Compare two numbers
    def __cmp__(self, secondRational): 
        temp = self.__sub__(secondRational)
        if temp[0] > 0:
            return 1
        elif temp[0] < 0:
            return -1
        else:
            return 0        

    # Return numerator and denominator via indexer
    def __getitem__(self, index): 
        if index == 0:
            return self.__numerator
        else:
            return self.__denominator

def gcd(n, d):
    n1 = abs(n);
    n2 = abs(d)
    gcd = 1
    
    k = 1
    while k <= n1 and k <= n2:
        if n1 % k == 0 and n2 % k == 0:
            gcd = k
        k += 1

    return gcd

#Test the exception
c1 = Rational(1,0)
print(c1)


