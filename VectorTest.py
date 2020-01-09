#------------------------------------------------------------------------------
#  VectorTest.py
#------------------------------------------------------------------------------

import Vector

A = [-3, -4, 7]
B = [6, -2, 2]

print(A)
print(B)

print(Vector.add(A,B))
print(Vector.negate(B))
print(Vector.sub(A,B))
print(Vector.scalarMult(2.5,A))
print(Vector.scalarMult(-3.5,B))
print(Vector.zip(A,B))
print(Vector.dot(A,B))
print(Vector.length(A))
print(Vector.length(B))
print(Vector.unit(A))
print(Vector.unit(B))
print(Vector.angle(A,B))

C = Vector.randVector(3,-10,10)
print(Vector.sub(C,C))
