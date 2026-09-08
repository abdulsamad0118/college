#  Atm Withdrawal And Minimum Balance

balance=float(input("Balance: "))
amount=float(input("Withdraw: "))
minimum=1000
if amount>balance:
    print("Insufficient balance")
elif balance-amount<minimum:
     print("Minimum balance rule violated")
else:
     print("New balance:",balance-amount)
