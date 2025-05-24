order = {
   "item1": {"name": "Laptop", "price": 700},
   "item2": {"name": "Mouse", "price": 20}
}
a = input("Enter item1 or item2: ")
if a == "item1":
    print("Name: ",order["item1"]["name"])
    print("Price: ",order["item1"]["price"])
elif a == "item2":
    print("Name: ",order["item2"]["name"])
    print("Price: ",order["item2"]["price"])
else:
    print("Item not found")