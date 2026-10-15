"""Pattern program: Hollow diamond inside rectangle."""

n = int(input("Enter an odd number of columns (e.g. 7): "))
if n % 2 == 0:
    print("Please enter an odd number.")
else:
    mid = n // 2
    for i in range(n):
        distance = abs(mid - i)
        for j in range(n):
            if j == 0 or j == n - 1 or j == distance or j == n - 1 - distance:
                print("*", end="")
            else:
                print(" ", end="")
        print()
