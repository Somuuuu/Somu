cart = [{
    "id": 1, 
    "name": "shirt", 
    "qty": 1
}]
a = int(input("Enter product id: "))
b = input("Enter product: ")
new= {
    "id":a,
    "name":b
}
if a == cart[0]["id"] :
    print("available ")
else:
    cart.append(new)
    print(cart)


