#  Time Greeting

h=int(input("Enter hour 0-23: "))
if 5<=h<12:
     print("Morning")
elif 12<=h<17:
     print("Afternoon")
elif 17<=h<21:
     print("Evening")
else: print("Night")
