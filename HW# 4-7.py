class QuadraticEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def discriminant(self):
        return ((self.b)**2) - (4 * self.a * self.c)

    def root1(self):
        if self.discriminant() < 0:
            return None
        else:
            return (-self.b + math.sqrt(self.discriminant())) / (2 * self.a)
    def root2(self):
        if self.discriminant() < 0:
            return None
        else:
            return (-self.b - math.sqrt(self.discriminant())) / (2 * self.a)

a = QuadraticEquation(1,2,3)
print (a.root1())
print (a.root2())
print (a.discriminant())
