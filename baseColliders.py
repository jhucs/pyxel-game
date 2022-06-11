import pyxel

class Frame:
    def __init__(self,bank,px,py,pw,ph,colorKey):
        self.bank = bank
        self.px = px
        self.py = py
        self.pw = pw
        self.ph = ph
        self.colorKey = colorKey
        
    def PrintFrame(self,x,y):
        pyxel.blt(x,y,self.bank,self.px,self.py,self.pw,self.ph,self.colorKey)
        
class Animation:
    def __init__(self, frames, steps, loop):
        self.frames = frames
        self.steps = steps
        self.loop = loop
        self.current = 0
        self.time = 0
    
    def PrintAnimation(self,x,y):
        self.time += 1
        if (self.time >= self.steps):
            self.time = 0
            self.current += 1
            if (len(self.frames)<=self.current and self.loop):
                self.current = 0
        self.frames[self.current].PrintFrame(x,y)
        
class Collider:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

class ColliderManager:
    ColliderList = []
    PlayerObj = []
    
    def CheckCollider():
        