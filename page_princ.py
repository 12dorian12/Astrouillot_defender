import tkinter as tk
import Jeu as j
from PIL import Image, ImageTk



"""
///////////////////////////////////////////Fonctions//////////////////////////////////////////////
"""
def niveau1():
    frame_niveau.pack_forget()
    partie.run()
    frame_jeu.pack()

def jouer():
    frame_principale.pack_forget()
    frame_niveau.pack()



"""
///////////////////////////////////////////intitialisation//////////////////////////////////////////////
"""
groot = tk.Tk()
groot.title("Astrouillot Defender")
dimension = [1000]
groot.minsize(160, 90)



"""
///////////////////////////////////////////Page principale////////////////////////////////////////////
"""
frame_principale = tk.Frame(groot, width = dimension[0], height = dimension[0]*9/16)
frame_principale.grid_propagate(0)

img = Image.open("media/img/fond.jpg")
image_fond = ImageTk.PhotoImage(img)

frame_principale.grid_rowconfigure((0,1,2,3), weight=1)
frame_principale.grid_columnconfigure((0, 2), weight=1, minsize=groot.winfo_height()/3)

can = tk.Canvas(frame_principale, width=400, height=400)
can.create_image(0, 0, anchor=tk.NW, image=image_fond)
can.grid(row=0, rowspan= 4, column= 0, columnspan= 3)

tk.Label(frame_principale, text="ASTROUILLOT DEFENDER", font = ("Arial", 30)).grid(row=0,pady= 25, column= 0, columnspan= 3)
tk.Button(frame_principale, text="Jouer", command = jouer).grid(row=1, column= 1)
tk.Button(frame_principale, text="Parametres").grid(row=2, column=1)
tk.Button(frame_principale, text="Quit",  command= groot.destroy).grid(row=3, column=1)
tk.Button(frame_principale, text= "?").grid(row= 3, column= 0)
tk.Button(frame_principale, text="Credits").grid(row= 3, column= 2)



"""
///////////////////////////////////////////Page niveau////////////////////////////////////////////
"""
frame_niveau = tk.Frame(groot, width = dimension[0], height = dimension[0]*9/16)
frame_niveau.grid_propagate(0)

img = Image.open("media/img/fond.jpg")
image = ImageTk.PhotoImage(img)

frame_niveau.grid_columnconfigure((0), weight=1)
frame_niveau.grid_rowconfigure((0,1,2), weight=1)

tk.Button(frame_niveau, text="Niveau facile", command= niveau1).grid(row=0)
tk.Button(frame_niveau, text="Niveau moyen", command= niveau1).grid(row=1)
tk.Button(frame_niveau, text="Niveau difficile", command= niveau1).grid(row=2)



"""
///////////////////////////////////////////Page jouer////////////////////////////////////////////
"""

frame_jeu = tk.Frame(groot, width = dimension[0], height = dimension[0]*9/16)
frame_jeu.grid_propagate(0)

partie = j.Jeu(frame_jeu)




"""
////////////////////////////////////////trame du jeu/////////////////////////////////////////
"""

frame_principale.pack()

groot.mainloop()



