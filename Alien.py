"""
objectif : cree la class Alien.
Dates : 17 decembre
fait par : Lea Dorian
Todo : 
"""

import Super_ad as ad
from PIL import Image, ImageTk
import random as rnd
import Laser as l

class Alien(ad.Super_ad):
    def __init__(self):
        self.nb_vies = 1
        self.pox = 1
        self.poy = 5
        self.vitesse = 1
        self.gap = 5

        self.vitesse_tire = 1
        self.force = 1

        self.image_data = ad.Super_ad.image_data_alien
        self.resize(10, 10)  # definit self.image
        self.sprite = ad.Super_ad.canvas.create_image(self.vw(self.pox), self.vh(self.poy), image = self.image)       
        self.update(self.image, self.pox, self.poy)
    
    def move(self):
        """
        on modifie la position du laser selon ca vitesse et on update
        """
        self.pox +=  self.vitesse
        if self.pox > 97:
            self.vitesse = -self.vitesse
            self.poy += self.gap
        if self.pox < 1:
            self.vitesse = -self.vitesse
            self.poy += self.gap
        if rnd.random() > 0.99:
            self.tire()
    
    def tire(self):
        """ 
        permet de tirer sur le joueur
        """
        ad.Super_ad.list_laser.append(l.Laser(self.pox, self.poy, self.vitesse_tire, self.force))

    def hit(self, damage):
        """
        fonction qui appeler lors d'une collision
        *** damage : un entier qui represente les point de vie a perdre
        """
        self.nb_vies -= damage
        if self.nb_vies <= 0:
            self.delete()
            return True
        return False

    def delete(self):
        """
        permet la supression sur le canvas est dans super_ad
        """
        ad.Super_ad.canvas.delete(self.sprite)
        ad.Super_ad.list_alien.remove(self)
        
    def tic(self):
        """
        fonction qui ce fait appeler par tac de jeu, elle fait evoluer l'objet dans le temps
        """
        self.move()        
        self.update(self.image, self.pox, self.poy)





