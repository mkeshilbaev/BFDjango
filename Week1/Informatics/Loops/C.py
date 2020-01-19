import math

a = int(input())
b = int(input())

if a <= b:
 for i in range(a, b):
     k = math.floor(math.sqrt(i))
     if (k*k==i):
      print(i)
