def view():
    print(cart)
def cal_ttl():
    ttl=sum(cart.values())
    return ttl
items=int(input('enter the no.of items:'))
cart={input('enter item name:'):int(input('enter the price:'))for _ in range(items)}
view()
print(cal_ttl())