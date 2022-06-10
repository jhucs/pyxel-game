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