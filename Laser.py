"""
objectif : cree la class Laser.
Dates : 17 decembre
fait par : Lea Dorian
Todo : 
"""

import Super_ad as ad
from PIL import Image, ImageTk
import  Vaisseau as v

class Laser(ad.Super_ad):
    """
    class qui cree des laser utiliser par les alien et le vaisseau
    la vitesse est soit positive si il vient d'un alien, ou vegative si il vient du vaisseau
    """
    def __init__(self, x, y, vitesse, force):
        """
        *** x : entier represente la position horizontale en pourcent
        *** y : entier represente la position verticale en pourcent
        *** vitesse : entier represente la vitesse de mouvement a chaque tic
        *** force : entier represente les degat a appliquer
        """
        self.pox = x
        self.poy = y
        self.size = 10
        self.vitesse = vitesse
        self.force = force

        self.image_data = ad.Super_ad.image_data_laser
        self.resize(10,10,2.62) #definit self.image
        self.sprite = ad.Super_ad.canvas.create_image(self.vw(self.pox), self.vh(self.poy), image = self.image)
        self.update(self.image, self.pox, self.poy)

    def move(self):
        """
        on modifie la position du laser selon ca vitesse et on update
        """
        self.poy += self.vitesse
        if self.poy <= 0 or self.pox >100:
            self.delete()

    def delete(self):
        """
        permet la supression sur le canvas est dans super_ad
        """
        ad.Super_ad.canvas.delete(self.sprite)
        ad.Super_ad.list_laser.remove(self)

    def tic(self):
        """
        fonction qui ce fait appeler par tac de jeu, elle fait evoluer l'objet dans le temps
        """
        self.move()
        self.update(self.image, self.pox, self.poy)
