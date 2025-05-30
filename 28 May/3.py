a = int(input("Enter even number: "))
new = []
new.append(a)
while a%2==0:
        a = int(input("Enter even number: "))
        if a%2!=0:
            break
        new.append(a)

print(f"All numbers: {new}")
    