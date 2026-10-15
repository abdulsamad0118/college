#  Salary With Overtime

hours=float(input("Hours worked: "))
rate=float(input("Rate: "))
salary=40*rate+(hours-40)*rate*1.5 if hours>40 else hours*rate
print("Salary:",salary)
