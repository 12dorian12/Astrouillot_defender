"""
objectif : lancer le programe, cree la fenetre principale, cree les widget de ces fenetre, cree l'objet partie
Dates : 17 decembre
fait par : Lea Dorian
Todo : rajouter des image pour les bouton et pour les frames de victoire et defaite
"""

from distutils import command
import tkinter as tk
import Jeu as j
from PIL import Image, ImageTk



"""
///////////////////////////////////////////Fonctions//////////////////////////////////////////////
"""
def niveau1():
    partie = j.Jeu(frame_jeu, int(dimension[0]*3/4*9/16), fin_du_game, maj_vie, maj_score)
    frame_niveau.pack_forget()
    partie.run(0, 1, 1) 
    frame_jeu.pack()

def niveau2():
    partie = j.Jeu(frame_jeu, int(dimension[0]*3/4*9/16), fin_du_game, maj_vie, maj_score)
    frame_niveau.pack_forget()
    partie.run(0, 1, 2) 
    frame_jeu.pack()

def niveau3():
    partie = j.Jeu(frame_jeu, int(dimension[0]*3/4*9/16), fin_du_game, maj_vie, maj_score)
    frame_niveau.pack_forget()
    partie.run(0, 1, 3) 
    frame_jeu.pack()

def jouer():
    frame_principale.pack_forget()
    frame_defaite.pack_forget()
    frame_victoire.pack_forget()
    frame_niveau.pack()

def fin_du_game(victory):
    if victory:
        frame_jeu.pack_forget()
        frame_victoire.pack()
    else:
        frame_jeu.pack_forget()
        frame_defaite.pack()


def maj_score(point):
    label_score.configure(text = "score: {}".format(point))


def maj_vie(vie):
    label_vie.configure(text = "Vie restantes: {}".format(vie))


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
frame_principale.grid_columnconfigure((0, 2), weight=1, uniform="column")

can = tk.Canvas(frame_principale, width = dimension[0], height = dimension[0]*9/16)
can.create_image(0, 0, anchor=tk.NW, image=image_fond)
can.grid(row=0, rowspan= 4, column= 0, columnspan= 3)

tk.Label(frame_principale, text="ASTROUILLOT DEFENDER", font = ("Arial", 30)).grid(row=0, pady= 25, column= 0, columnspan= 3)
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

can_niv = tk.Canvas(frame_niveau, width = dimension[0], height = dimension[0]*9/16)
can_niv.create_image(0, 0, anchor=tk.NW, image=image_fond)
can_niv.pack()


frame_niveau.grid_columnconfigure((0), weight=1)
frame_niveau.grid_rowconfigure((0,1,2), weight=1)

tk.Button(frame_niveau, text="Niveau facile", command= niveau1).grid(row=0)
tk.Button(frame_niveau, text="Niveau moyen", command= niveau2).grid(row=1)
tk.Button(frame_niveau, text="Niveau difficile", command= niveau3).grid(row=2)



"""
///////////////////////////////////////////Page jouer////////////////////////////////////////////
"""
frame_jeu = tk.Frame(groot, bg = "black", width = dimension[0], height = dimension[0]*3/4)
frame_jeu.grid_propagate(0)

frame_jeu.grid_columnconfigure((1), weight=2, uniform="column")
frame_jeu.grid_columnconfigure((0, 2), weight=1, uniform="column")

label_score = tk.Label(frame_jeu, text="Score")
label_score.grid(row= 0, column=0)
label_vie = tk.Label(frame_jeu, text= "Vie restante")
label_vie.grid(row= 0, column=2)


"""
///////////////////////////////////////////Page Victoire////////////////////////////////////////////
"""
frame_victoire = tk.Frame(groot, bg="black", width=dimension[0], height=dimension[0]*3/4)
frame_victoire.grid_propagate(0)

frame_victoire.grid_columnconfigure((0, 1, 2), weight=2, uniform="column")
frame_victoire.grid_rowconfigure((0, 1, 2), weight=1)

tk.Label(frame_victoire, text="Tu as GAGNER", font=("Arial", 30)).grid(row=0, column=0, columnspan=3)
tk.Button(frame_victoire, text="Rejouer", command=jouer).grid(row=1, column=1)
tk.Button(frame_victoire, text="Quiter", command=groot.destroy).grid(row=3, column=1)

"""
///////////////////////////////////////////Page defaite////////////////////////////////////////////
"""
frame_defaite = tk.Frame(groot, bg="black", width=dimension[0], height=dimension[0]*3/4)
frame_defaite.grid_propagate(0)

frame_defaite.grid_columnconfigure((0, 1, 2), weight=2, uniform="column")
frame_defaite.grid_rowconfigure((0, 1, 2), weight=1)

tk.Label(frame_defaite, text="Tu as PERDU", font=("Arial", 30)).grid(row=0, column=0, columnspan=3)
tk.Button(frame_defaite, text="Rejouer", command=jouer).grid(row=1, column=1)
tk.Button(frame_defaite, text="Quiter", command=groot.destroy).grid(row=3, column=1)


"""
////////////////////////////////////////trame du jeu/////////////////////////////////////////
"""

frame_principale.pack()

groot.mainloop()



