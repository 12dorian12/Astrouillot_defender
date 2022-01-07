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
ad.Super_ad.canvas = main_canvas

joueur = v.Vaisseau()

def tac():
    joueur.tic()

    root.after(16, tac)
tac()
root.mainloop()