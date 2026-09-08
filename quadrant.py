#  Quadrant From X And Y

x=float(input("x: ")); y=float(input("y: "))
if x==0 and y==0: print("Origin")
elif x==0:
     print("Y-axis")
elif y==0:
     print("X-axis")
elif x>0 and y>0:
     print("First quadrant")
elif x<0 and y>0:
     print("Second quadrant")
elif x<0 and y<0:
     print("Third quadrant")
else:
     print("Fourth quadrant")
