"""Pattern program: Number triangle (row-wise)."""

n = int(input("Enter number of rows: "))
for i in range(1, n + 1):
    print(" " * (n - i) + (str(i) + " ") * i)
