"""Pattern program: Binary number triangle."""

n = int(input("Enter number of rows: "))
for i in range(n):
    for j in range(i + 1):
        print((i + j) % 2, end="")
    print()
