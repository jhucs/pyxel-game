import random
import pyxel
import background, proyectRef
import player.playerMain as pm
import enemies.enemieBaseClass as em

class App:
  def __init__(self):
    pyxel.init(proyectRef.width, proyectRef.height, title=proyectRef.title, fps=60)
    pyxel.load("assets.pyxres")
    pyxel.run(self.update, self.draw)

  def update(self):
    pm.PlayerObj.InputController()

  def draw(self): 
    pyxel.cls(0)
    background.PrintAllStars()
    pm.PlayerObj.DrawPlayer()
    enemieCute.PrintEnemie()
    enemieCute.Movement()
    #pyxel.text(55, 41, "Hello uwu , Pyxel!", pyxel.frame_count % 16)

enemieCute = em.enemieBunny(random.randint(0,proyectRef.width),-10)

App()