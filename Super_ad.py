from tkinter import Canvas
from PIL import Image, ImageTk


class Super_ad():
    """
    On charge toute nos image lors de la creation de la premiere initialisation de la super class
    Tout les objet de notre jeu herite de cette super class
    """
    image_data_laser = Image.open("media/img/laser_fixe.png")
    image_data_vaisseau = Image.open("media/img/vaisseau.png")

    canvas = None

    def __init__(self, canvas):
        Super_ad.canvas = canvas

    """
    les deux fonctions suivantes permettent d'avoir la postion 
    en px sur le canvas a partir d'un pourcentage
    """
    def vw(self, x):
        return int(Super_ad.canvas.winfo_width()*x/100)
    def vh(self, y):
        return int(Super_ad.canvas.winfo_height()*y/100)

    def update(self, img, pox, poy):
        self.canvas.itemconfig(self.sprite, image = img)
        self.canvas.coords(self.sprite, self.vw(pox), self.vh(poy))