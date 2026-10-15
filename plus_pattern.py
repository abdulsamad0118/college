"""Pattern program: Plus (+) pattern."""

n = int(input("Enter an odd number for the plus pattern: "))
mid = n // 2
for i in range(n):
    for j in range(n):
        if i == mid or j == mid:
            print("*", end="")
        else:
            print(" ", end="")
    print()
