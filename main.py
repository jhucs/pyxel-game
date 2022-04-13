import pyxel
import colliders

class App:
  def __init__(self):
    colliders.uwu()
    pyxel.run(self.update, self.draw)

  def update(self):
    if pyxel.btnp(pyxel.KEY_Q):
      pyxel.quit()

  def draw(self):
    pyxel.cls(0)
    pyxel.text(55, 41, "Hello, Pyxel!", pyxel.frame_count % 16)


App()