#  Scholarship Eligibility

marks=float(input("Marks: "))
attendance=float(input("Attendance: "))
income=float(input("Family income: "))
print("Eligible" if marks>=80 and attendance>=75 and income<=300000 else "Not eligible")
