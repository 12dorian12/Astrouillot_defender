"""
objectif : cree la class Vaisseau.
Dates : 17 decembre
fait par : Lea Dorian
Todo : 
"""

import Super_ad as ad
from PIL import Image, ImageTk
import Alien as a

import Laser as l

class Vaisseau(ad.Super_ad):
    def __init__(self):
        self.nb_vies = 3
        self.pox = 50
        self.poy = 94
        self.vitesse = 1

        self.vitesse_tire = 2
        self.temp_de_recharge = 500
        self.force = 1
        self.reload = True

        self.is_mooving = False

        self.image_data = ad.Super_ad.image_data_vaisseau
        self.resize(10, 10)  # definit self.image
        self.sprite = ad.Super_ad.canvas.create_image(self.vw(self.pox), self.vh(self.poy), image = self.image)
        self.update(self.image, self.pox, self.poy)


        ############################# Binding #############################
        ad.Super_ad.canvas.bind_all("<KeyPress>", self.key_down, add = "+")
        ad.Super_ad.canvas.bind_all("<KeyRelease>", self.key_up, add = "+")

    def key_down(self,e):
        """ 
        permet de definir la direction du vaisseau selon la touche appuier
        *** e : objet de type evenement fournit par les event de tkinter
        """
        if e.keysym == "Left" or e.keysym == "q":
            self.is_mooving = "Left"
        if e.keysym == "Right" or e.keysym == "d":
            self.is_mooving = "Right"
        if e.keysym == "Return" or e.keysym == "space":
            self.tire()
    
    def key_up(self,e):
        """
        permet de rendre le vaisseau statique quand il ne bouge les touche son relever
        *** e : objet de type evenement fournit par les event de tkinter
        """
        if e.keysym == "Left" or e.keysym == "q":
            if self.is_mooving == "Left":
                self.is_mooving = False
        if e.keysym == "Right" or e.keysym == "d":
            if self.is_mooving == "Right":
                self.is_mooving = False

    def tire(self):
        """ 
        permet de tirer un laser
        """
        if self.reload:
            self.reload = False
            ad.Super_ad.list_laser.append(l.Laser(self.pox, 90, -self.vitesse_tire, self.force))
            ad.Super_ad.canvas.after(self.temp_de_recharge, self.reloading)

    def reloading(self):
        """ 
        permet de recharger
        """
        self.reload = True

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
        permet de unbind les evenement liee au touche
        """
        ad.Super_ad.canvas.delete(self.sprite)
        ad.Super_ad.joueur = None
        ad.Super_ad.canvas.unbind_all("<KeyPress>")
        ad.Super_ad.canvas.unbind_all("<KeyRelease>")

    def tic(self):
        """
        fonction qui ce fait appeler par tac de jeu, elle fait evoluer l'objet dans le temps
        le deplacement est geree ici et selon la direction
        """
        if self.is_mooving == "Left":
            self.pox -= self.vitesse
            if self.pox < 3:
                self.pox = 3
        if self.is_mooving == "Right":
            self.pox += self.vitesse
            if self.pox > 97:
                self.pox = 97
        self.update(self.image, self.pox, self.poy)
