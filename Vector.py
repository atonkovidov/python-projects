#Andre Tonkovidov
#atonkovi@ucsc.edu
#pa7
#A module of functions to perform standard vector operations with descriptions
#of module and each function accessible through the built-in help function.

"""
This module provides functions to perform standard vector operations.  Vectors
are represented as lists of numbers (floats or ints).  Functions that take two 
vector arguments may give arbitrary output if the vectors are not compatible,
i.e. of the same dimension.  
"""

import math
import random


#-- main program --------------------------------------------------------------


def add(u, v):
   """
   Return the vector sum u+v.
   """
   w = []
   for i in range(len(u)):
      w.append(u[i]+v[i])
   # end for
   return w
# end add()

def negate(u):
   """
   Rerurn the negative -u of the vector u.
   """
   return scalarMult(-1, u)
# end negate()

def sub(u, v):
   """
   Return the vector difference u-v.
   """
   return add(u, negate(v))
# end sub()

def scalarMult(c, u):
   """
   Return the scalar product cu of the number c by the vector u.
   """
   U = []
   for x in u:
      U.append(c*x)
   # end for
   return U
# end scalarMult()

def zip(u, v):
   """
   Return the component-wise product of u with v.
   """
   w = []
   for i in range(len(u)):
      w.append(u[i]*v[i])
   # end for
   return w
# end zip()

def dot(u, v):
   """
   Return the dot product of u with v.
   """
   return sum(zip(u, v))
# end dot()

def length(u):
   """
   Return the (geometric) length of the vector u.
   """
   return dot(u, u)**(1/2)
# end length()

def unit(v):
   """
   Return a unit (geometric length l) vector in the direction of v.
   """
   w = []
   for x in v:
      w.append(x/length(v))
   # end for
   return w
# end unit()

def angle(u, v):
   """
   Return the angle (in degrees) between vectors u and v.
   """
   return math.degrees(math.acos(dot(unit(u),unit(v))))
# end angle()

def randVector(n, a, b):
   """
   Return a vector of dimension n whose components are random floats
   in the range [a, b).
   """
   V = []
   for i in range(n):
      V.append(random.uniform(a, b))
   # end for
   return V
# end randomVector()