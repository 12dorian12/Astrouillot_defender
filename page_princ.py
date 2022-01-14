import tkinter as tk
import Jeu as j
from PIL import Image, ImageTk

def  jouer():
    groot.destroy()
    jroot = tk.Tk()
    jroot.title("Astrouillot Defender")
    jroot.minsize(400,400)
    img = Image.open("media/img/fond.jpg")
    image = ImageTk.PhotoImage(img)

    jroot.grid_columnconfigure((0), weight=1)
    jroot.grid_rowconfigure((0,1,2), weight=1)

    tk.Button( jroot, text="Niveau facile", command= niveau1).grid(row=0)
    tk.Button( jroot, text="Niveau moyen", command= niveau1).grid(row=1)
    tk.Button( jroot, text="Niveau difficile", command= niveau1).grid(row=2)

    jroot.mainloop()

def niveau1 ():
    root = tk.Tk()
    root.title("Astrouillot Defender")
    root.minsize(400,400)

    partie = j.Jeu(root)
    partie.run()

    root.mainloop()
        




groot = tk.Tk()
groot.title("Astrouillot Defender")
groot.minsize(400,400)
img = Image.open("media/img/fond.jpg")
image = ImageTk.PhotoImage(img)

groot.grid_rowconfigure((0,1,2,3), weight=1)
groot.grid_columnconfigure((0, 2), weight=1, minsize=groot.winfo_height()/3)

Canevas = tk.Canvas(groot, width=400, height=400)
Canevas.create_image(0, 0, anchor=tk.NW, image=image)
Canevas.grid(row=0, rowspan= 4, column= 0, columnspan= 3)

tk.Label( groot, text="ASTROUILLOT DEFENDER", font = ("Arial", 30)).grid(row=0,pady= 25, column= 0, columnspan= 3)
tk.Button( groot, text="Jouer", command= jouer).grid(row=1, column= 1)
tk.Button( groot, text="Paramètres").grid(row=2, column=1)
tk.Button( groot, text="Quit",  command= groot.destroy).grid(row=3, column=1)
tk.Button(groot, text= "?").grid(row= 3, column= 0)
tk.Button(groot, text="Credits").grid(row= 3, column= 2)


groot.mainloop()



