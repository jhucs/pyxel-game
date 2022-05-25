import pyxel 
from player.playerBaseClasses import *


class PlayerCore:
    def __init__(self,x,y,wings,rocket,shooter):
        self.x = x
        self.y = y
        self.maxTimeParticle = 5
        self.wings = wings
        self.rocket = rocket
        self.shooter = shooter

    def DrawPlayer(self):
        pyxel.blt(self.x,self.y,0,0,0,16,16,0)
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
            
        

Player = PlayerCore(50,50,PlayerWings(16,0),PlayerRocket(),PlayerShooter(7,1,5,1))
#16,0 to 23,7