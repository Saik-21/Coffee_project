class Line:
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def slope(self):
        return (self.coor2[1]-self.coor1[1])/(self.coor2[0] - self.coor1[0])

    def distance(self):
        

li = Line((3,2),(8,10))

print(li.slope())
    

