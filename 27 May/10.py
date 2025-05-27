a =  {
     'name': 'Alice',
     'city': 'New York', 
     'hobby': 'coding'
}
new ={
    
}
for item in a:
    b = a[item]
    if len(b)>5:
        new[item]=b.upper()
        
    else:
        new[item]=b.lower()
print(new)
        
    
