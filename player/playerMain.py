import pyxel

class PlayerCore:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def DrawPlayer(self):
        pyxel.blt(self.x,self.y,0,0,0,16,16,0)
        PWings.DrawWings(self.x,self.y)

    def InputController(self):
        if pyxel.btn(pyxel.KEY_D):
            self.x = self.x + 1
        if pyxel.btn(pyxel.KEY_A):
            self.x = self.x - 1
        if pyxel.btn(pyxel.KEY_W):
            self.y = self.y - 1
        if pyxel.btn(pyxel.KEY_S):
            self.y = self.y + 1

class PlayerWings:
    def __init__(self,sx,sy):
        self.sx = sx
        self.sy = sy
        self.x = 12 #unused
        self.y = 5
        
    def DrawWings(self,px,py):
        pyxel.blt(12+px,self.y+py,0,self.sx,self.sy,8,8,0) #right
        pyxel.blt(-4+px,self.y+py,0,self.sx,self.sy,-8,8,0) #left
        
class PlayerRocket:
    def __init__(self):
        pass

Player = PlayerCore(50,50)
PWings = PlayerWings(16,0)

#16,0 to 23,7