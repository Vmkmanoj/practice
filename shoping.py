order=[]
price=[]
total=0

while True:
    orders=input("enter the orders (q to quit): ")
    if orders.lower()=="q":
        break
    else:
        prices=float(input(f"enter the price {orders}:"))
        order.append(orders)
        price.append(prices)
for i in order:
    print(i,end="\n ")

for j in price:
    total=total+j
print(f"your total is {total}")

