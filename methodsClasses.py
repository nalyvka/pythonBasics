class Rectangle:
    def __init__(self, c, l, w):
        self.colour=c
        self.length=l
        self.width=w
    def area(self):
        self.area = self.length*self.width
        return self.area
rect1=Rectangle('blue', 3, 6)
rect2=Rectangle('yellow', 6, 9)
print('rect1 length = ',rect1.length)
print('rect1 width = ', rect1.width)
print('rect1 colour = ',rect1.colour)
print('rect2 length = ', rect2.length)
print('rect2 width = ', rect2.width)
print('rect2 colour = ', rect2.colour)