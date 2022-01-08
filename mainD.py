import tkinter as tk
import Super_ad as ad
import Vaisseau as v

import Laser as l
import Alien as a

root = tk.Tk()
root.title("Astrouillot Defender")
root.minsize(500,888)

#creation du canvas principal
main_canvas = tk.Canvas(root, bg="black")
main_canvas.pack(fill="both", expand="yes")

#permet d'initialiser notre super class
list_alien = []
super_class = ad.Super_ad(main_canvas)
joueur = v.Vaisseau(list_alien)


nb_alien = 10
for i in range(nb_alien):
    root.after(i*300, lambda : list_alien.append(a.Alien(joueur, list_alien)))


def tac():
    """
    Tac est une horloge globale, elle apelle la fonction tic de chaque objet 60 fois par seconde
    """
    joueur.tic()

    for alien in list_alien:
        alien.tic()

    for tir in ad.Super_ad.list_laser : 
        tir.tic()

    root.after(26, tac)
tac()

root.mainloop()