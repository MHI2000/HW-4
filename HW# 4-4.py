class Rectangle1:
    def __init__(self,L,W):
        self.L=L
        self.W=W

        
    def findarea(self):
        return self.L*self.W
    def findperimeter(self):
        return 2*(self.L + self.W)

    
class Rectangle2:
    def __init__(self,L2,W2):
        self.L2=L2
        self.W2=W2

    def findarea(self):
        return self.L2*self.W2

    
    def findperimeter(self):
        return 2*(self.L2 + self.W2)












r1=Rectangle1(4,40)
r2=Rectangle2(3.5,35.7)
print("Area : " , r1.findarea())
print("Perimeter : " , r1.findperimeter())


print("Area : " , r2.findarea())
print("Perimeter : " , r2.findperimeter()) 
