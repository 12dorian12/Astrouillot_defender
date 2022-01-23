"""
objectif : cree la class Ilots.
Dates : 17 decembre
fait par : Lea Dorian
Todo : 
"""

import Super_ad as ad
import tkinter as tk
from PIL import Image,ImageTk

import Laser as l

class Ilots(ad.Super_ad):
    def __init__(self, x):
        """
        *** x : entier represente la position en pourcent
        """
        self.nb_vies = 1
        self.pox = x
        self.poy = 80

        self.image_data = ad.Super_ad.image_data_bloc
        self.resize(5, 5)  # definit self.image
        self.sprite = ad.Super_ad.canvas.create_image(self.vw(self.pox), self.vh(self.poy), image = self.image)
        self.update(self.image, self.pox, self.poy)


    def hit(self, damage):
        """
        fonction qui appeler lors d'une collision
        *** damage : un entier qui represente les point de vie a perdre
        """
        self.nb_vies -= damage
        if self.nb_vies <= 0:
            self.delete()

    def delete(self):
        """
        permet la supression sur le canvas est dans super_ad
        """
        ad.Super_ad.canvas.delete(self.sprite)
        ad.Super_ad.list_bloc.remove(self)


           


