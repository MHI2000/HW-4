class Fan:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color
        self.speed = 0
        self.is_off = False
        self.is_on = True


        


    def __repr__(self):
        return repr (( self.radius,self.color, self.speed, self.is_off, self.is_on))


    def switch_on (self):
        self.is_on = True
        self.speed = 5
        fan.setColor ("yellow")
       


    





def switch_off (self):
            self.is_off = False
            self.speed = 0
            fan.setColor ("blue")



            
print(Fan(10,"yollow"))  



print(Fan(5,"blue"))  

