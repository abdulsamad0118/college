def fun(n):
    if n == 0 :
        return 1
    lastdigit = n % 10 
    return lastdigit*fun(n//10)


x = fun(234)
print(x)
