a = list(input("Enter five numbers: "))
print(a)
key = input()
for item in a:
    if item in key:
        print("Found")
        break
else:
    print("Not found")