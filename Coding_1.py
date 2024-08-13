class Line:
    sqrt = lambda x:x**0.5
    sqr = lambda x:x**2

    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return (y2-y1)/(x2-x1)

    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return Line.sqrt(Line.sqr(y2-y1)+(Line.sqr(x2-x1)))



li = Line((3,2),(8,10))


class Cylinder:
    def __init__(self,height=1,radius=1):
        self.height =height
        self.radius = radius
    def volume(self):
        return 3.14*Line.sqr(self.radius)*self.height
    def surface_area(self):
        return 2*3.14*self.radius*self.height + 2*3.14*Line.sqr(self.radius)

c = Cylinder(2,3)


print(li.__dict__)