import tkinter as tk
import Super_ad as ad
import Vaisseau as v

root = tk.Tk()
root.title("Astrouillot Defender")
root.minsize(400,400)

#creation du canvas principal
main_canvas = tk.Canvas(root, bg="black")
main_canvas.pack(fill="both", expand="yes")

#permet d'initialiser notre super class
super_class = ad.Super_ad(main_canvas)

joueur = v.Vaisseau()

def tac():
    """
    Tac est une horloge globale, elle apelle la fonction tic de chaque objet 60 fois par seconde
    """
    joueur.tic()

    root.after(16, tac)
tac()

root.mainloop()