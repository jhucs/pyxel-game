import pyxel
from colliders import *

class PlayerCore:
    def __init__(self,frame,health, defence):
        self.frame = frame
        self.health = health
        self.defence = defence
    
    def DrawCore(self,x,y):
        self.frame.PrintFrame(x,y)

class PlayerWings:
    def __init__(self,frameLeft,frameRight):
        self.x = 12 #unused
        self.y = 4
        self.LeftWing = frameLeft
        self.RightWing = frameRight
        
    def DrawWings(self,px,py):
        self.LeftWing.PrintFrame(-4+px,self.y+py)
        self.RightWing.PrintFrame(12+px,self.y+py)

class PlayerRocket:
    def __init__(self,speed,playerRocketParticle):
        self.PParticles = []
        self.time = 0
        self.maxTimeParticle = 6
        self.speed = speed
        self.playerRocketParticle = playerRocketParticle
        
    def DrawParticles(self,x,y):
        self.time += 1
        if (self.time >= self.maxTimeParticle):
            self.PParticles.append(self.playerRocketParticle(self,x,y))
            self.time = 0
        
        for _pp in self.PParticles:
            _pp.DrawParticle()

class PlayerRocketParticle:
    def __init__(self,RocketCore, x, y,DrawParticleFn):
        self.x = x + 3
        self.y = 0
        self.iniY = y + 10
        self.t = 0
        self.RocketCore = RocketCore
        self.DrawParticleFn = DrawParticleFn
        
    def DrawParticleBase(self):
        self.DrawParticleFn(self)
        
class PlayerShooter:
    def __init__(self,color,damage,speed,rate):
        self.color = color
        self.damage = damage
        self.speed = speed
        self.rate = rate
        self.bullets = []
    
    def Shoot(self,x,y):
        self.bullets.append(PlayerBullet(self,self.damage,self.speed,x,y,self.color))
        
    def DrawBullets(self):
        for blt in self.bullets:
            blt.UpdateBullet()
        
class PlayerBullet:
    def __init__(self,PSB,damage,speed,x,y,color):
        self.PSB = PSB
        self.damage = damage
        self.speed = speed
        self.x = x
        self.y = y
        self.color = color
        
    def UpdateBullet(self):
        pyxel.rect(self.x,self.y,2,5,self.color)
        pyxel.rect(self.x+12,self.y,2,5,self.color)
        self.y -= self.speed