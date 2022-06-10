from player.playerBaseClasses import *

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