class vehicle:
    def sound(self):
        print("making sound")
        

class bike(vehicle):
    def __int__(self):
        print("This is bike")


class car(vehicle):
    def __int__(self):
        print("This is car")
        
a = car()
print(a.sound())
b = bike()
print(b.sound())