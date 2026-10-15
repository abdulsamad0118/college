#  Electricity Bill Slabs

units = int(input("Enter electricity units: "))

if units <= 100:
    bill = units * 1
elif units <= 200:
    bill = 100 * 1 + (units - 100) * 2
elif units <= 300:
    bill = 100 * 1 + 100 * 2 + (units - 200) * 3
else:
    bill = 100 * 1 + 100 * 2 + 100 * 3 + (units - 300) * 4

print("Electricity bill:", bill)
