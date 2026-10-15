"""Pattern program: Alphabet triangle (row repeat)."""

n = int(input("Enter number of rows (1-26): "))
for i in range(1, n + 1):
    letter = chr(64 + i)
    print(letter * i)
