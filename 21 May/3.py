loc = [(12.9716, 77.5946)]
a = float(input("Enter latitude: "))
b = float(input("Enter longitude: "))
new = (a, b)
if a == loc[0][0] and b == loc[0][1]:
    print("Location already exists.")
else:
    loc.append(new)
    print(loc)