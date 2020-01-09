def findAll(s,ch):
   L = []
   i = 0
   while i < len(s):
      if s[i] == ch:
         L.append(i)
      i += 1
   return L

print(findAll('ballarama', 'a'))