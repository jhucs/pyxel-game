from colliders import *
import math

class enemie:
    def __init__(self, x, y, movement, speed, animation):
        self.x = x
        self.y = y
        self.movement = movement
        self.speed = speed
        self.animation = animation
        
    def PrintEnemie(self):
        self.animation.PrintAnimation(self.x,self.y)
        
    def Movement(self):
        self.movement()
        
        
class enemieBunny(enemie):
    def __init__(self, x, y):
        animAux = Animation([Frame(0,0,120,16,16,0),Frame(0,16,120,16,16,0)],10,True)
        super().__init__(x, y, self.BunnyMovement,1,animAux)
        
    def BunnyMovement(self):
        self.y += self.speed
        self.x = (self.x + math.cos(self.y/20))