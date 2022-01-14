import tkinter as tk
from PIL import Image, ImageTk

class Super_ad():
    """
    On charge toute nos image et on cree le canvas a l'initialisation
    Tout les objets de notre jeu herite de cette super class
    contient la liste des laser
    contient la liste des alien
    contient le joueur
    """
    image_data_laser = Image.open("media/img/laser_fixe.png")
    image_data_vaisseau = Image.open("media/img/vaisseau.png")
    image_data_alien = Image.open("media/img/alien.png")
    image_data_fond1 = Image.open("media/img/niveau1.jpg")
    image_data_fond2 = Image.open("media/img/niveau2.jpg")
    image_data_fond3 = Image.open("media/img/niveau3.jpg")
    image_data_bloc = Image.open("media/img/pierre.jpg")

    canvas = None
    joueur = None
    list_laser = []
    list_alien = []
    list_bloc = []
    
    

    def __init__(self, window, w, fond):
        #creation du canvas principal
        Super_ad.canvas = tk.Canvas(window, bg="black", width=int(w), height=int(w*(16/9)))
        self.resize_bg = fond.resize((int(w*(16/9)**2), int(w*(16/9))), Image.ANTIALIAS)
        self.bg = ImageTk.PhotoImage(self.resize_bg)
        self.can_bg = Super_ad.canvas.create_image(-w/1.25,0, anchor= tk.NW, image = self.bg)

    def vw(self, x):
        #retourne la postion en px sur le canvas a partir d'un pourcentage sur la largeur
        return int(Super_ad.canvas.winfo_width()*x/100)
    def vh(self, y):
        #retourne la postion en px sur le canvas a partir d'un pourcentage sur la hauteur
        return int(Super_ad.canvas.winfo_height()*y/100)
    def distance_eclidienne(self, x1, y1, x2, y2):
        #retourne la distance selon la norme 2
        return ((x1-x2)**2 + (y1-y2)**2)**(1/2)



    def update(self, img, pox, poy):
        #update le canvas
        self.canvas.itemconfig(self.sprite, image = img)
        self.canvas.coords(self.sprite, self.vw(pox), self.vh(poy))
