from types import DynamicClassAttribute
import Super_ad as ad
import tkinter as tk
from PIL import Image,ImageTk

class Alien(ad.Super_ad):
    def __init__(self):
        self.nb_vies = 1
        self.pox = 1
        self.poy = 5
        self.vitesse = 3
        self.gap = 3


        self.img_data = Image.open("media/img/alien.png")
        self.resize_img = self.img_data
        self.imageA = ImageTk.PhotoImage(self.resize_img)
        self.sprite = ad.Super_ad.canvas.create_image(self.vw(self.pox), self.vh(self.poy), image = self.imageA)

        self.resize(1)
        self.move()
        ############################# Binding #############################
        ad.Super_ad.canvas.bind("<Configure>", self.resize, add = "+")

    def resize(self, e):
        """
        fonction qui s'appelle a chaque modification de la  taille du canvas
        """
        self.resize_img = self.img_data.resize((self.vw(10)+1, self.vw(10)+1), Image.ANTIALIAS)
        self.imageA = ImageTk.PhotoImage(self.resize_img)
        self.update()

    def update(self):
        ad.Super_ad.update(self, self.imageA, self.pox, self.poy)
        
        
    
    def move(self):
        self.pox +=  self.vitesse
        if self.pox > 97:
            self.vitesse = -self.vitesse
            self.poy += self.gap
        if self.pox < 1:
            self.vitesse = -self.vitesse
            self.poy += self.gap

        
    def tic(self):
        self.move()
        self.update()




