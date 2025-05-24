bill = 0
menu = {
    "idli":10,
    "samosa":15,
    "parota":25
}
a = input("Item: ")
b = int(input("count: "))
bill = menu[a]*b
print(f"{bill}")
