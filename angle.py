#  Smaller Clock Angle

h=int(input("Hour: "))
m=int(input("Minute: "))
ha=(h%12)*30+m*0.5; ma=m*6
d=abs(ha-ma);
print("Smaller angle:",min(d,360-d))
