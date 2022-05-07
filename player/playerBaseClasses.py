import pyxel

class PlayerWings:
    def __init__(self,sx,sy):
        self.sx = sx
        self.sy = sy
        self.x = 12 #unused
        self.y = 4
        
    def DrawWings(self,px,py):
        pyxel.blt(12+px,self.y+py,0,self.sx,self.sy,8,8,0) #right
        pyxel.blt(-4+px,self.y+py,0,self.sx,self.sy,-8,8,0) #left
        
class PlayerRocket:
    def __init__(self):
        self.PParticles = []
        self.time = 0
        self.maxTimeParticle = 6
        
    def DrawParticles(self,x,y):
        self.time += 1
        if (self.time >= self.maxTimeParticle):
            self.PParticles.append(PlayerRocketParticle(self,x,y))
            self.time = 0
        
        for _pp in self.PParticles:
            _pp.DrawParticle()

class PlayerRocketParticle:
    def __init__(self,RocketCore, x, y):
        self.x = x + 3
        self.y = 0
        self.iniY = y + 10
        self.t = 0
        self.RocketCore = RocketCore
        
    def DrawParticle(self):
        self.y +=1
        self.t +=2
        self.aux = (self.t/10)
        
        if (self.t<40 ):
            pyxel.ellib(self.x+(self.aux/3), self.iniY + self.y, 10-self.aux,4-self.aux ,3)
        else:
            self.RocketCore.PParticles.remove(self)
        
            