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
        return (
            (self.x - self.w / 2) <= point.x <= (self.x + self.w / 2) and
            (self.y - self.h / 2) <= point.y <= (self.y + self.h / 2)
        )
  
    def intersects(self,range):
        return not(range.x - range.w/2 > self.x + self.w/2 or range.x + range.w/2 < self.x - self.w/2 or range.y - range.h/2 > self.y + self.h/2 or range.y + range.h/2 < self.y - self.h/2)

class Circle:
    def __init__(self,x,y,r):
        self.x = x
        self.y = y
        self.r = r
        self.rSqu = pow(r,2)
    
    def contains(self,point):
        return self.rSqu >= (pow(self.x-point.x,2) + pow(self.y-point.y,2))
    
    def intersects(self,range):  
        xDist = abs(self.x - range.x)
        yDist = abs(self.y - range.y)

        if (xDist > (self.r + range.w) or yDist>(self.r + range.h)):
            return False
        
        if (xDist <= range.w or yDist <= range.h):
            return True
        
        edges = pow((xDist-range.w),2) + pow(yDist-range.h,2)
        return edges <= self.rSqu


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
        self.divided = False

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

    def insert(self, point):
        if not self.boundary.contains(point):
            return False

        if self.divided:
            return (
                self.northeast.insert(point) or
                self.northwest.insert(point) or
                self.southeast.insert(point) or
                self.southwest.insert(point)
            )

        if len(self.points) < self.capacity:
            self.points.append(point)
            return True
        else:
            self.subdivide()
            return self.insert(point)

    
    def query(self,range,found):
        if not(range.intersects(self.boundary)):
            return found
            
        if self.divided:
            self.northwest.query(range,found)
            self.northeast.query(range,found)
            self.southeast.query(range,found)
            self.southwest.query(range,found)
            pass
        else:
            for p in self.points:
                if range.contains(p):
                    found += [p]
            
        return found

