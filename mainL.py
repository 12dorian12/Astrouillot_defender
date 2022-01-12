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
pan = l.Laser(50)
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

import tkinter as tk
from tkinter.constants import CENTER
import Super_ad as ad
import Vaisseau as v

import Laser as l
import Alien as a

root = tk.Tk()
root.title("Astrouillot Defender")
root.minsize(400,400)
imge = tk.PhotoImage(file='media/img/mars.gif')

root.grid_rowconfigure((0,1,2,3), weight=1)
root.grid_columnconfigure((0, 2), weight=1, minsize=root.winfo_height()/3)

Canevas = tk.Canvas(root, width=400, height=400)
Canevas.create_image(0, 0, anchor=tk.NW, image=imge)
Canevas.grid(row=0, rowspan= 4, column= 0, columnspan= 3)

tk.Label( root, text="ASTROUILLOT DEFENDER", font = ("Arial", 30)).grid(row=0,pady= 25, column= 0, columnspan= 3)
tk.Button( root, text="Jouer").grid(row=1, column= 1)
tk.Button( root, text="Paramètres").grid(row=2, column=1)
tk.Button( root, text="Quit").grid(row=3, column=1)
tk.Button(root, text= "?").grid(row= 3, column= 0)
tk.Button(root, text="Credits").grid(row= 3, column= 2)

root.mainloop()


import tkinter as tk
import Super_ad as ad
import Vaisseau as v
import Ilots as il

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
mur = il.Ilots()
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