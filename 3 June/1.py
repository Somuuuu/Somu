class light:
    def turn_on(self):
        print("Lights turned on")
    def turn_off(self):
        print("Lights turned off")


class AC:
    def __init__(self, brand):
        self.brand = brand
    def turn_on(self):
        print(f" {self.brand} Ac turned on")
    def turn_off(self):
        print("Ac turned off")
    def change_temp(self):
        pass
    
    
class Room:
    def __init__(self, ac, l):
        self.temp = 24
        self.ac = ac
        self.l = l
ac = AC("samsung")
l = light()
room = Room(ac, l)

room.l.turn_on()
 
room.ac.turn_on()
