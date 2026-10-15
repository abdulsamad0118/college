"""Pattern program: Zigzag pattern."""

n = int(input("Enter a number of columns (at least 3): "))
for row in range(3):
    for col in range(n):
        if (row == 0 and col % 4 == 0) or (row == 1 and col % 2 == 1) or (row == 2 and col % 4 == 2):
            print("*", end="")
        else:
            print(" ", end="")
    print()
