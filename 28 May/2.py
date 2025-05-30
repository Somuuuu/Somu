a = int(input("Enter number: "))
count=1
while a <= 100:
    a += int(input("Enter number: "))
    count+=1
    if a>100:
        break
print(count)