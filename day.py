# Select Day By Number

d=int(input("Enter day number 1-7: "))
days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
print(days[d-1] if 1<=d<=7 else "Invalid day")
