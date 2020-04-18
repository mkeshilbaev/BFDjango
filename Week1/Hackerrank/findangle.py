import math
a = int(input())
b = int(input())
c = math.sqrt( a**2 + b**2)
med = math.sqrt((2*a**2 + 2*b**2 - c**2)/4)
c /= 2
cosx = -(c**2 - med**2 - b**2)/(2*med*b)
print(round(math.degrees(math.acos(cosx))), end='°')