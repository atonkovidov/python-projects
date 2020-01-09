# Andre Tonkovidov
# atonkovi@ucsc.edu
# pa4
# Prints a user indicated number of prime numbers starting from 2.
# The number 1 is excluded as a prime.

def isPrime(m, L):
   for i in range(0,len(L)):
      if m % L[i] == 0:
         return False 
      elif m < L[i]**2:
         return True

def PrimeList(primes):
   L = [2]
   m = 2
   while len(L) < primes:
      if isPrime(m, L) == True:
         L.append(m)
      m += 1
      isPrime(m, L)
   return L   

print()
primes = int(input("Enter the number of Primes to compute: "))
print()
print("The first", primes, "primes are:")
j = 0

for entry in PrimeList(primes):
   print(entry, end=" ")
   j += 1
   if j % 10 == 0:
      print(end="\n")
if j % 10 != 0:
   print(end="\n")