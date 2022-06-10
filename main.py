import pyxel
import background, proyectRef
import player.playerMain

class App:
  def __init__(self):
    pyxel.init(proyectRef.width, proyectRef.height, title=proyectRef.title, fps=60)
    pyxel.load("assets.pyxres")
    pyxel.run(self.update, self.draw)

  def update(self):
    player.PlayerMain.Player.InputController()

  def draw(self): 
    pyxel.cls(0)
    background.PrintAllStars()
    player.PlayerMain.Player.DrawPlayer()
    #pyxel.text(55, 41, "Hello uwu , Pyxel!", pyxel.frame_count % 16)


App()