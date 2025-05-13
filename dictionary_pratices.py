#Test 1 :Shopping Cart
cart = {}

# add the item 
def add_to_cart(item, price, quantity):
    if item in cart:
        cart[item]["quantity"]+=quantity    
    else:
        cart[item]={"price":price,"quantity":quantity}
    

add_to_cart("水果茶",60,5)
add_to_cart("水果茶",60,5)
print(cart)

# 計算總價
def calculate_total():
    total = 0
    for item in cart:
        total += cart[item]["price"] * cart[item]["quantity"]
    return total
print(calculate_total())

#檢視清單
def show_cart():
    for item, info in cart.items():
        print(f"{item} x{info['quantity']} @ ${info['price']} = ${info['price'] * info['quantity']}")
    print(f"總價：${calculate_total()}")
