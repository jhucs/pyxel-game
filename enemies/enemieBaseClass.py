

class enemie:
    def __init__(self,x,y,sprite,movement,speed):
        self.x = x
        self.y = y
        self.sprite = sprite
        self.movement = movement
        self.speed = speed
        
        
class enemieBunny(enemie):
    def __init__(self, x, y, sprite,speed):
        super().__init__(x, y, sprite, self.movement(),speed)
        
    def movement(self):
        self.y += self.speed