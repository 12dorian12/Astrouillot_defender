import Super_ad as ad
from PIL import Image, ImageTk

class Alien(ad.Super_ad):
    def __init__(self):
        self.nb_vies = 1
        self.pox = 1
        self.poy = 5
        self.vitesse = 1
        self.gap = 5

        self.image_data = ad.Super_ad.image_data_alien
        self.sprite = ad.Super_ad.canvas.create_image(self.vw(self.pox), self.vh(self.poy), image = "") #on definit l'image avec update dans resize

        self.resize()
        self.move()

        ############################# Binding #############################
        ad.Super_ad.canvas.bind("<Configure>", self.resize, add = "+")

    def resize(self, *e):
        """
        fonction qui s'appelle a chaque modification de la  taille du canvas
        """
        self.resize_img = self.image_data.resize((self.vw(10)+1, self.vw(10)+1), Image.ANTIALIAS)
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

    def hit(self, damage):
        print("pan")
        self.nb_vies -= damage
        if self.nb_vies <= 0:
            self.delete()

    def delete(self):
        ad.Super_ad.canvas.delete(self.sprite)
        ad.Super_ad.list_alien.remove(self)
        
    def tic(self):
        self.move()
        self.update()




