a = ('sam', 'jhon', 'alex', 'bob')
for item in a:
    b = item.upper()
    if len(item)<=3:
        print(b)
    else:
        c = item.capitalize()
        print(c)