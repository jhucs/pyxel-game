import pyxel

class PlayerCore:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def DrawPlayer(self):
        pyxel.blt(self.x,self.y,0,0,0,16,16,0)

    def InputController(self):
        if pyxel.btn(pyxel.KEY_D):
            self.x = self.x + 1
        if pyxel.btn(pyxel.KEY_A):
            self.x = self.x - 1
        if pyxel.btn(pyxel.KEY_W):
            self.y = self.y - 1
        if pyxel.btn(pyxel.KEY_S):
            self.y = self.y + 1

Player = PlayerCore(50,50)