class Point:
    def __init__(self,x,y,data = False):
        self.x = x
        self.y = y
        self.data = data

class Rectangle:
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def contains(self, point):
        return point.x >= (self.x - self.w/2) and point.x < (self.x + self.w/2) and point.y >= (self.y - self.h/2) and point.y < (self.y + self.h/2)

class QuadTree:
    def __init__(self, boundary, n, id=0):
        self.boundary = boundary
        self.capacity = n
        self.points = []
        self.divided = False
        self.id = id

        self.northeast = None
        self.northwest = None
        self.southeast = None
        self.southwest = None

    def clear(self):
        self.points = []
        self.northeast = None
        self.northwest = None
        self.southeast = None
        self.southwest = None

    def subdivide(self):

        ne = Rectangle(self.boundary.x + (self.boundary.w/4),self.boundary.y - (self.boundary.h/4), self.boundary.w/2, self.boundary.h/2)
        self.northeast = QuadTree(ne,self.capacity,self.id+1)
        nw = Rectangle(self.boundary.x - (self.boundary.w/4),self.boundary.y - (self.boundary.h/4), self.boundary.w/2, self.boundary.h/2)
        self.northwest = QuadTree(nw,self.capacity,self.id+1)
        se = Rectangle(self.boundary.x + (self.boundary.w/4),self.boundary.y + (self.boundary.h/4), self.boundary.w/2, self.boundary.h/2)
        self.southeast = QuadTree(se,self.capacity,self.id+1)
        sw = Rectangle(self.boundary.x - (self.boundary.w/4),self.boundary.y + (self.boundary.h/4), self.boundary.w/2, self.boundary.h/2)
        self.southwest = QuadTree(sw,self.capacity,self.id+1)
        self.divided = True

        for p in self.points:
            if self.northeast.boundary.contains(p):
                self.northeast.insert(p)
            elif self.northwest.boundary.contains(p):
                self.northwest.insert(p)
            elif self.southeast.boundary.contains(p):
                self.southeast.insert(p)
            elif self.southwest.boundary.contains(p):
                self.southwest.insert(p)
        self.points = []

    def insert(self,point):
        if not(self.boundary.contains(point)):
            return

        if not self.divided:
            if len(self.points) < self.capacity:
                self.points.append(point)
            else:
                self.subdivide()

                if self.northeast.boundary.contains(point):
                    self.northeast.insert(point)
                elif self.northwest.boundary.contains(point):
                    self.northwest.insert(point)
                elif self.southeast.boundary.contains(point):
                    self.southeast.insert(point)
                elif self.southwest.boundary.contains(point):
                    self.southwest.insert(point)
        else:
            if self.northeast.boundary.contains(point):
                self.northeast.insert(point)
            elif self.northwest.boundary.contains(point):
                self.northwest.insert(point)
            elif self.southeast.boundary.contains(point):
                self.southeast.insert(point)
            elif self.southwest.boundary.contains(point):
                self.southwest.insert(point)