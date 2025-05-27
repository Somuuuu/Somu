a = (1,2,3,4,5,6,7,8,9,10)
for item in a:
    if item %3 == 0:
        continue
    else:
        b =item**2
        print(b)