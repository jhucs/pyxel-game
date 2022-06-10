import pyxel 
from player.playerUpdates import *


class Player:
    def __init__(self,x,y,core,wings,rocket,shooter):
        self.x = x
        self.y = y
        self.maxTimeParticle = 5
        self.core = core
        self.wings = wings
        self.rocket = rocket
        self.shooter = shooter

    def DrawPlayer(self):
        self.core.DrawCore(self.x,self.y)
        self.wings.DrawWings(self.x,self.y)
        self.rocket.DrawParticles(self.x,self.y)
        self.shooter.DrawBullets()

    def InputController(self):
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x = self.x + 1
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x = self.x - 1
        if pyxel.btn(pyxel.KEY_UP):
            self.y = self.y - 1
        if pyxel.btn(pyxel.KEY_DOWN):
            self.y = self.y + 1
            
        if pyxel.btnp(pyxel.KEY_Z):
            self.shooter.Shoot(self.x,self.y)
            
        

PlayerObj = Player(50,50,NormalCore(),NormalWings(),NormalRocket(),NormalShooter())
#16,0 to 23,7