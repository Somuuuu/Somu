a = [10,25,36,40]
for item in a:
    b = item**0.5
    if b*b==item:
        break
print(f"{item} is a perfect square")