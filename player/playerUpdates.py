from player.playerBaseClasses import *
import math

class NormalWings(PlayerWings):
    def __init__(self):
        super().__init__(Frame(0,16,0,-8,8,0),Frame(0,16,0,8,8,0)) 
        
class NormalCore(PlayerCore):
    def __init__(self):
        super().__init__(Frame(0,0,0,16,16,0),3,1)
        
class NormalRocket(PlayerRocket):
    def __init__(self):
        super().__init__(1, NormalRocketParticle)
        
class NormalRocketParticle(PlayerRocketParticle):
    def __init__(self, RocketCore, x, y):
        super().__init__(RocketCore, x, y, self.DrawParticle)
        
    def DrawParticle(self):
        self.y +=1
        self.t +=2
        self.aux = (self.t/10)
        
        if (self.t<40 ):
            pyxel.ellib(self.x+(self.aux/3), self.iniY + self.y, 10-self.aux,4-self.aux ,3)
        else:
            self.RocketCore.PParticles.remove(self)

class NormalShooter(PlayerShooter):
    def __init__(self):
        super().__init__(1, NormalBullet)

class NormalBullet(PlayerBullet):
    def __init__(self,x,y):
        super().__init__(1, 5, x, y, 7, self.DrawBullet, self.MovementBullet)
    
    def DrawBullet(self):
        pyxel.rect(self.x,self.y,2,5,self.color)
        pyxel.rect(self.x+12,self.y,2,5,self.color)
    
    def MovementBullet(self):
        self.y -= self.speed