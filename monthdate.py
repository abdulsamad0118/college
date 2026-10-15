#  Month Number And Days

m=int(input("Month number: "))
if m in [1,3,5,7,8,10,12]:
     print("31 days")
elif m in [4,6,9,11]:
     print("30 days")
elif m==2:
     print("28 or 29 days")
else:
     print("Invalid month")
