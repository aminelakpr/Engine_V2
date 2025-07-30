import random as rd

class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def limit(self,s):
        if self.x > s:
            self.x = s
        elif self.x < -s:
            self.x = -s
        if self.y > s:
            self.y = s
        elif self.y < -s:
            self.y = -s

    def add(self,vect):
        self.x += vect.x
        self.y += vect.y
    def vadd(self,vect):
        return Vector(self.x + vect.x,self.y + vect.y)
    def vsub(self,vect):
        return Vector(self.x - vect.x,self.y - vect.y)
    def vscal(self,scl):
        return Vector(self.x * scl,self.y * scl)
    def vprod(self,vect):
        return (self.x * vect.x)+(self.y * vect.y)
    def vint(self):
        return Vector(int(self.x),int(self.y))
    def dist(self,vect):
        return pow(pow(self.x-vect.x,2)+pow(self.y-vect.y,2),1/2)
    def sdist(self):
        return pow(pow(self.x,2)+pow(self.y,2),1/2)
    def impactvect(self):
        return self.vscal(1/self.sdist())

class Particle:
    def __init__(self,x,y,mass,velocity=Vector(rd.randint(1,10),rd.randint(1,10))):
        self.position = Vector(x,y)
        self.velocity = velocity
        self.acceleration = Vector(0,0)
        self.mass = mass
        self.r = int(pow(mass,1/2)*20)
        self.width = 800
        self.height = 400
        self.lossPE = -0.6
    
    def tupl(self):
        return (self.position.x,self.position.y)
    
    def update(self,vect):
        self.acceleration = vect
        self.velocity.add(self.acceleration)
        self.velocity.limit(2.5)
        #self.velocity = self.velocity.vscal(0.995) #Frottem
        self.position.add(self.velocity)
        self.edge()                     #HHHDDII rassek hna

    def edge(self):
        if self.position.x > self.width - self.r :
            self.position.x = self.width - self.r
            self.velocity.x *= self.lossPE
        elif self.position.x < self.r :
            self.position.x = self.r
            self.velocity.x *= self.lossPE
        
        if self.position.y > self.height - self.r :
            self.position.y = self.height - self.r
            self.velocity.y *= self.lossPE
        elif self.position.y < self.r :
            self.position.y = self.r
            self.velocity.y *= self.lossPE
        
    def collide(self,other):
        if self.position.dist(other.position)<self.r + other.r:

            return True
    
    def resolution(self,other):
        m2 = self.mass + other.mass
        den = m2 * pow( self.r + other.r ,2)

        vdiff = other.velocity.vsub(self.velocity)
        pdiff = other.position.vsub(self.position)
        num = vdiff.vprod(pdiff)*2*other.mass #maybe heeeeerre
        res = num/den
        new_velocity = self.velocity.vadd(pdiff.vscal(res))
        #self.velocity = self.velocity.vint()
        #print(vdiff.vprod(pdiff))
        #print(vdiff.x,vdiff.y)
        #print(self.velocity.x,self.velocity.y)

        vdiff = self.velocity.vsub(other.velocity)
        pdiff = self.position.vsub(other.position)
        num = vdiff.vprod(pdiff)*2*self.mass #maybe heeeeerre
        res = num/den
        #print(vdiff.x,vdiff.y)
        #(other.velocity.x,other.velocity.y)

        overlap = self.position.dist(other.position) - (self.r + other.r)
        dirr = other.position.vsub(self.position).impactvect().vscal(overlap*0.49)
        self.position.vadd(dirr)
        #print(overlap)
        self.velocity = new_velocity
        return other.velocity.vadd(pdiff.vscal(res)) ,other.position.vsub(dirr)

        
        
        