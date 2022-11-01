# this set of functions is to solve for kinematic values given most cases having 3 of the 5 variables.
#  a = Acceleration (Meters per second squared)
#  s = positional "space" (Meters)
#  t = time (seconds)
# v0 = initial velosity (Meters per second)
#  v = velosity at curent time (Meters per second)

# how to import:
#https://stackoverflow.com/questions/2349991/how-do-i-import-other-python-files
# use any of the methods from the link above 
# but this is the most reliable method in case you are working offline.
# import sys 
# import os
# sys.path.append(os.path.abspath("/path/to/this/file"))
# from UniformAccel_kinematics import *
# # or 
# # import UniformAccel_kinematics as kinematics 


# one dependant function: 
# sorry, I like my math functions and vector.array() in this namespace. when using python as a CLI
# sqrt is all these functions need
# if you are importing math into this namespace, then you can comment this out.
# sqrt needs to exist in this... otherwise you can change all lines "sqrt" to "math.sqrt" if you want.
from math import sqrt

# usage: 
# These functions take 3 arguments of 4.
# If you have all 4 available arguments for a problem, pick 3
# it will not try to compute with all 4 arguments, as it may create an inequality.
# it will just return the error string anyway
#
# example: 
# >>> a = solveFor_a(t=6,v0=3,v=45)
# >>> a
# 7.0

# how it works:
# valset is a list of your variables and which flags or bits they are assigned to. 
# valset assignments change per solver
# the sub-function 'listNotNone_to_intBits' convers the list 'valset' into an integer. 
# in binary, the 1's would corespond with the arguments provided to the function.
# technically an int; functionally , it's just 4 bits in inverted line priority. 
# 
# match select and below just selects which Kinematic equation to apply and returns the value.

def listNotNone_to_intBits(ArgL):
   i = 0
   intOut = 0
   for e in ArgL:
      intOut = intOut ^ ( (type(e) is not type(None)) << i )
      i = i+1
   return(intOut)
 

def solveFor_a(t=None,v=None,v0=None,s=None):
   valset = [t,v,v0,s] # [ 1s, 2s, 4s, 8s ] 
   select = listNotNone_to_intBits(valset)
   match select:
      case 7: #15-8: t,v0,v
         return( (v - v0)/t)
      case 11: #15-4:, t,v,s
         return( 'not implemented')
      case 13: #15-2: t,v0,s
         return( (2*(s-v0*t)/(t**2)))
      case 14: #15-1: v,v0,s
         return( (v**2 - v0**2)/(2*s) )
      case 15: 
         return('please do not provide all 4 arguments. pick 3')
   return('error: ' + str(valset) + ', ' + str(select))

def solveFor_s(t=None,v=None,v0=None,a=None):
   valset = [t,v,v0,a] # [ 1s, 2s, 4s, 8s ] 
   select = listNotNone_to_intBits(valset)
   match select:
      case 7: #15-8: t,v0,v
         return( (t*(v0+v)/2) )
      case 11: #15-4:, t,v,a
         return( 'not implemented')
      case 13: #15-2: t,v0,a
         return( (v0*t + (a*t**2)/2) )
      case 14: #15-1: v,v0,a
         return( (v**2 - v0**2)/(2*a) ) 
      case 15: 
         return('please do not provide all 4 arguments. pick 3')
   return('error: ' + str(valset) + ', ' + str(select))

def solveFor_t(s=None,v=None,v0=None,a=None):
   valset = [s,v,v0,a] # [ 1s, 2s, 4s, 8s ] 
   select = listNotNone_to_intBits(valset)
   match select:
      case 7: #15-8: s,v0,v
         return(  (2*s)/(v0+v) )
      case 11: #15-4:, s,v,a
         return( 'not implemented')
      case 13: #15-2: s,v0,a
         return( (sqrt(v0**2 + 2*a*s) -v0)/a )
      case 14: #15-1: v,v0,a
         return( (v - v0)/a )
      case 15: 
         return('please do not provide all 4 arguments. pick 3')
   return('error: ' + str(valset) + ', ' + str(select))


def solveFor_v0(s=None,v=None,t=None,a=None):
   valset = [s,v,t,a] # [ 1s, 2s, 4s, 8s ] 
   select = listNotNone_to_intBits(valset)
   match select:
      case 7: #15-8: s,t,v
         return( 'not implemented')
      case 11: #15-4:, s,v,a
         return( sqrt(v**2 - 2*a*s ) ) 
      case 13: #15-2: s,t,a
         return( (s/t) - (a*t)/(2) )
      case 14: #15-1: v,t,a
         return( v - a*t )
      case 15: 
         return('please do not provide all 4 arguments. pick 3')
   return('error: ' + str(valset) + ', ' + str(select))



def solveFor_v(s=None,v0=None,t=None,a=None):
   valset = [s,v0,t,a] # [ 1s, 2s, 4s, 8s ] 
   select = listNotNone_to_intBits(valset)
   match select:
      case 7: #15-8: s,t,v0
         return( 'not implemented')
      case 11: #15-4:, s,v0,a
         return( sqrt(v0**2 +2*a*s) )
      case 13: #15-2: s,t,a
         return( 'not implemented')
      case 14: #15-1: v0,t,a
         return( v0 + a*t )
      case 15: 
         return('please do not provide all 4 arguments. pick 3')
   return('error: ' + str(valset) + ', ' + str(select))


