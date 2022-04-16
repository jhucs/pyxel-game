from dataclasses import asdict
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

'''

te amito uwu uwuuuuuuuuuuuuuuuuuuuuuaczc
here was once a once owo. Hoy viernes santo, recuerdenlo como el dia en que Lian Ignacio encontró la paz interior al adentrarse 
en su espiritualidad. Todo esto surgió cuando vio que en TVN estaban dando la pasion de jesucristo, al ver como Jesús en vida era
una persona tan proactiva, artista, compositor, DJ, bailarín, programador, beta tester, y aun tenia tiempo para jugarse unas 10 
partidas de league of legends diarias, se decidió a ser como él cuando estaba con vida. Jesús desde el cielo veía conmovido como 
Lian Ignacio se adentraba en la misión de ser como él. Orgulloso, habló con su padre, Dios, que al escuchar lo que Jesús
de Nazareth contaba a él y a sus ángeles, decidió mandar unos dones especiales a Lian Ignacio, que sin saberlo, estaba a punto de 
experimentar como era recibir un don de Dios directamente sobre él.
Un día Sábado santo, a un día de que jesus resucitara, Dios se decidió a enviar los dones a Lian Ignacio, envió el don de la palabra, 
el don de dormir y además el don del enojo, que ayudarían a Lian en su camino por Chile, siendo el nuevo Mesías.
Esa mañana de sábado, Lian se despertó con los ojos bien abiertos, había recibido los dones de Dios en el cielo. Decidido, con la mirada 
fija sobre su objetivo, prendió el PC y se propuso encontrar una partida en el Lol
Ya en partida, eligió a su main, Gnar, pero, desgraciadamente, el pick de su rival era un counter muy marcado para su pequeño yordle. 
Sin embargo, a pesar de ese gran detalle, los dones que Dios le había enviado esa mañana, hicieron que, lian, en medio de la partida, 
se hiciera una pentakill doble cuando iba 1/7.XD

"Al fin he despertado a mi Jesus interior"- dijo Lian. 

Y así comenzó la gran aventura de Lian Jesus Ignacio (nuevo nombre en el registro civil)

'''