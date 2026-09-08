#  Profit Loss Or No Profit

cost=float(input("Cost price: "))
sell=float(input("Selling price: "))
if sell>cost:
     print("Profit:",sell-cost)
elif sell<cost:
     print("Loss:",cost-sell)
else:
     print("No profit, no loss")
