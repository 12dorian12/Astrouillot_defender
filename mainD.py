import tkinter as tk
import Super_ad as ad
import Vaisseau as v

import Laser as l
import Alien as a

root = tk.Tk()
root.title("Astrouillot Defender")
root.minsize(400,400)

#creation du canvas principal
main_canvas = tk.Canvas(root, bg="black")
main_canvas.pack(fill="both", expand="yes")

#permet d'initialiser notre super class
super_class = ad.Super_ad(main_canvas)

joueur = v.Vaisseau()
lst_alien = []

nb_alien = 10
for i in range(nb_alien):
    root.after(i*300, lambda : lst_alien.append(a.Alien()))


def tac():
    """
    Tac est une horloge globale, elle apelle la fonction tic de chaque objet 60 fois par seconde
    """
    joueur.tic()
    for alien in lst_alien:
        alien.tic()

    root.after(16, tac)
tac()

root.mainloop()