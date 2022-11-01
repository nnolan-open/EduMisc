# These two functions make life easier when trying to find the zero of a quadratic.

# I remember making two variants, but not entirely sure why I formatted this the way that I did. 
# Python handles i as j natively, like `1j`, but fractions.Fraction doesn't handle j. I may rework some of this later with sympy.simplify or something

# what's here now?
# Quadratic is better if you know your numbers are all real
# iQuadratic returns two strings in a list for the + and the -.

#bonus Factors function, but doesn't produce primes or count. 

from fractions import Fraction as frac
from fractions import Decimal as dec

import math

sin = math.sin
pi = math.pi
sqrt = math.sqrt

def Quadratic(a,b,c):
   n1 = (-b)+sqrt((b**2)-4*a*c)
   n2 = (-b)-sqrt((b**2)-4*a*c)
   d = 2 * a
   print(str(n1) +  '/' + str(d) + ' or ' +  str(n2) + '/' + str(d))
   try:
      return(frac(dec(n1),d),frac(dec(n2),d)) 
   except:
      return(frac(str((n1/d))),frac(str((n2/d))))


def iQuadratic(a,b,c):
   real = (-b)
   unreal_inside = (b**2) - 4*a*c
   denom = 2*a
   if unreal_inside < 0:
      is_i = 'i'
      real_inside = unreal_inside * -1
   else:
      is_i = ''
      real_inside = unreal_inside
   rooted = sqrt(real_inside)
   return([str( '(' + str(real) + ' + ' + str(rooted) + is_i + ')/' + str(denom)  ),
   str( '(' + str(real) + ' - ' + str(rooted) + is_i + ')/' + str(denom)  )])



#### not really useful. need prime factors, and count. 
def factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)
 












