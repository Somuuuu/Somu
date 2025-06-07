# class AC:
#     temp = 24
#     brand = "Samsung"
    



class light:
    watts = 10
    color = "white"
    brand = "philips"
    shape = "round"
    
    def turn_on(self):
        print("Turned on")
    def turn_off(self):
        print("Turned off")
    def intensity(self):
        pass

a = light()
print(a.turn_on)
a.turn_on()


class desk:
    height = 2 #meters
    color = "wodden"
    is_wheeled = True
    
    
    def change_height(self):
        print("Adjusted height as user needed")
    
    
a = desk()
print(a.is_wheeled)
a.change_height()    



class fan:
    color = "cream"
    brand = "crompton"
    speed = 10 #RPM
    
    
    def trun_on(self):
        print("Fan turned on")
    def turn_off(self):
        print("Fan turned off")
    def adjust_speed(self):
        print("adjusted to 15")

a = fan()
print(a.speed)
a.adjust_speed()    



class curtain:
    length = 10 #meters
    width = 6 #meters
    color = "red"
    design = "floral"
    
    
    def open(self):
        print("Opened")
    def close(self):
        print("Closed")

a = curtain()
print(a.design)
a.close()