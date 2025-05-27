a = ['python', 'code', 'loop', 'if', 'python', 'else', 'if']
c = a[3],a[5],a[6]
for item in a:
    if item in c:
        continue
    else:
        print(set(item))
        