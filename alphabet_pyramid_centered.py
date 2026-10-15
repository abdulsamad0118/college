"""Pattern program: Alphabet pyramid (centered)."""

n = int(input("Enter number of rows (1-26): "))
for i in range(1, n + 1):
    left = [chr(64 + j) for j in range(1, i + 1)]
    right = [chr(64 + j) for j in range(i - 1, 0, -1)]
    print(" " * (n - i) + " ".join(left + right))
