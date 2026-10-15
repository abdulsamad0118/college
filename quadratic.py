# 32. Quadratic Equation

import math
a=float(input("a: "))
b=float(input("b: "))
c=float(input("c: "))
d=b*b-4*a*c
if a==0:
     print("Not quadratic")
elif d>=0:
     print((-b+math.sqrt(d))/(2*a),(-b-math.sqrt(d))/(2*a))
else:
     print("Complex roots")
