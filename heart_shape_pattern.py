"""Pattern program: Heart shape pattern."""

n = int(input("Enter an even number (e.g. 6): "))
for i in range(n // 2, n + 1, 2):
    print(" " * ((n - i) // 2) + "*" * i + " " * (n - i) + "*" * i)
for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))
