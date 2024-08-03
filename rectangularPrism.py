class RectangularPrism:
    def __init__(self, c, l, w):
        self.colour=c
        self.length=l
        self.width=w
    def perimeter(self):
        self.perimeter = 2*self.width + 2*self.length
        return self.perimeter
    def area(self):
        self.area = self.length * self.width
        return self.area
    def diagonal(self):
        self.diagonal = (self.width**2 + self.length**2)**(1/2)
        return self.diagonal
    def volume(self, h):
        self.height = h
        self.volume=self.length*self.width*self.height
        return(self.volume)
prism1=RectangularPrism('blue', 3, 6)
vol1 = prism1.volume(1)
prism2=RectangularPrism('yellow', 6, 9)
vol2 = prism2.volume(3)
print('prism1 length = ',prism1.length)
print('prism1 width = ', prism1.width)
print('prism1 area =', prism1.area())
print('prism1 perimeter = ',prism1.perimeter())
print('prism1 diagonal = ', prism1.diagonal())
print('prism1 colour = ',prism1.colour)
print('prism1 volume = ',vol1)

print('prism2 length = ', prism2.length)
print('prism2 width = ', prism2.width)
print('prism2 area = ', prism2.area())
print('prism2 perimeter = ',prism2.perimeter())
print('prism2 diagonal = ',prism2.diagonal())
print('prism2 colour = ', prism2.colour)
print('prism2 volume = ',vol2)