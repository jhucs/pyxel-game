import pyxel
import random
import proyectRef

starsCollection=[]

def InitalizeStarCollection():
    for c in range(0,4):
        starsCollection.append(Star(random.randint(0,proyectRef.Width),random.randint(0,proyectRef.Height),1,3,1))
        
    for c in range(0,7):
        starsCollection.append(Star(random.randint(0,proyectRef.Width),random.randint(0,proyectRef.Height),0,2,0.5))
        

def PrintAllStars():
    for _star in starsCollection:
        _star.Update()

class Star:
    def __init__(self,x,y,radius,color,speed):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = speed
        
    def Update(self):
        pyxel.circ(self.x,self.y,self.radius,self.color)
        self.y = self.y + self.speed
        if self.y > proyectRef.Height : self.y = -5
            
InitalizeStarCollection()