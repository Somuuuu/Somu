a ={
    'apple': 2, 
    'banana': 3,
    'apricot': 4, 
    'berry': 5
}
b = 1
for item in a:
    if item[0]=='a': 
        b *= a[item]
print(f"product of values: {b}")