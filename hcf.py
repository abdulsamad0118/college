n = int(input("enter a number :"))
result = []
for i in range(1,n+1):
    if n % i == 0 : 
        result.append(i)
print("highest common factor is ",result[-1])