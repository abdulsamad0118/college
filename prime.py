n = int(input("enter a number : "))

count = 0 

for i in range(1,n+1):
    if n % i == 0:
        count=  count + 1 

# print(count)

if count == 2 :
    print("the given number is prime number which is ",n)
else :
    print("not a prime number") 