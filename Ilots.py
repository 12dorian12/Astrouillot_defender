import Super_ad as ad
import tkinter as tk
from PIL import Image,ImageTk

import Laser as l

class Ilots(ad.Super_ad):
    def __init__(self, x):
        self.nb_vies = 1
        self.pox = x
        self.poy = 80

        self.img_data = ad.Super_ad.image_data_bloc
        self.sprite = ad.Super_ad.canvas.create_image(self.vw(self.pox), self.vh(self.poy), image = "") #on definit l'image avec update dans resize

        self.resize()


        ############################# Binding #############################
        ad.Super_ad.canvas.bind("<Configure>", self.resize, add = "+")
        

    def resize(self, *e):
        """
        fonction qui s'appelle a chaque modification de la  taille du canvas
        """
        self.resize_img = self.img_data.resize((self.vw(5)+1, self.vw(5)+1), Image.ANTIALIAS)
        self.imageV = ImageTk.PhotoImage(self.resize_img)
        self.update()

    def update(self):
        ad.Super_ad.update(self, self.imageV, self.pox, self.poy)


    def hit(self, damage):
        self.nb_vies -= damage
        if self.nb_vies <= 0:
            self.delete()

    def delete(self):
        ad.Super_ad.canvas.delete(self.sprite)
        ad.Super_ad.list_bloc.remove(self)


           


