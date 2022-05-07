import pyxel 
from player.playerBaseClasses import *


class PlayerCore:
    def __init__(self,x,y,wings,rocket):
        self.x = x
        self.y = y
        self.maxTimeParticle = 5
        self.wings = wings
        self.rocket = rocket

    def DrawPlayer(self):
        pyxel.blt(self.x,self.y,0,0,0,16,16,0)
        self.wings.DrawWings(self.x,self.y)
        self.rocket.DrawParticles(self.x,self.y)

    def InputController(self):
        if pyxel.btn(pyxel.KEY_D):
            self.x = self.x + 1
        if pyxel.btn(pyxel.KEY_A):
            self.x = self.x - 1
        if pyxel.btn(pyxel.KEY_W):
            self.y = self.y - 1
        if pyxel.btn(pyxel.KEY_S):
            self.y = self.y + 1
            
        if pyxel.btnp(pyxel.KEY_J):
            pass
            
        

Player = PlayerCore(50,50,PlayerWings(16,0),PlayerRocket())
#16,0 to 23,7