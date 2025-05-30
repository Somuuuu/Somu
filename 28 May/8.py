    
a = [1,2,3,4] 
rev = 0
for i in a: 
    digit = i % 10
    rev = rev * 10 + digit
    i //= 10