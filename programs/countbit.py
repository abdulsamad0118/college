#  Count Number Of Bits


n = int(input("Enter a number: "))

count = 0

while n > 0:
    count += 1
    n = n >> 1

print("Number of bits:", count)