class Rectangle:
    def __init__(self, c, l, w):
        self.colour=c
        self.length=l
        self.width=w

rect1=Rectangle('blue', 3, 6)
rect2=Rectangle('yellow', 6, 9)
print(rect1.colour)
print(rect2.colour)