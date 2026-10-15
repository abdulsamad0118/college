#  Calculator Using Match Case

a=float(input("First number: "))
b=float(input("Second number: "))
op=input("Operator: ")
match op:
    case "+": print(a+b)
    case "-": print(a-b)
    case "*": print(a*b)
    case "/": print("Cannot divide by zero" if b==0 else a/b)
    case _: print("Invalid operator")
