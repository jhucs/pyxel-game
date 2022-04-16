import pyxel
import colliders

GAME_DATA={"Title":"Oh no, its another pixel art game si queri cambialo!"}

class App:
  def __init__(self):
    pyxel.init(160, 120, title=GAME_DATA["Title"])
    pyxel.run(self.update, self.draw)

  def update(self):
    if pyxel.btnp(pyxel.KEY_Q):
      pyxel.quit()

  def draw(self): 
    pyxel.cls(0)
    pyxel.text(55, 41, "Hello uwu , Pyxel!", pyxel.frame_count % 16)


App()

#te amito uwu uwuuuuuuuuuuuuuuuuuuuuuaczc