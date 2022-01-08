import Super_ad as ad
from PIL import Image, ImageTk

class Laser(ad.Super_ad):
    """
    class qui cree des laser
    le laser test les colision avec le joueur ou les alien
    """
    def __init__(self, x, vitesse, force):
        self.anim = 0
        self.pox = x
        self.poy = 90
        self.size = 10
        self.vitesse = vitesse
        self.force = force

        self.image_data = ad.Super_ad.image_data_laser
        self.sprite = ad.Super_ad.canvas.create_image(self.vw(self.pox), self.vh(self.poy), image = "") #on definit l'image avec update dans resize
        self.resize()

        ############################# Binding #############################
        ad.Super_ad.canvas.bind("<Configure>", self.resize, add = "+")

    def resize(self, *e):
        """
        fonction qui s'appelle a chaque modification de la  taille du canvas
        """
        self.resize_image = self.image_data.resize((int(self.vw(self.size)/2.62+1), self.vw(self.size)+1), Image.ANTIALIAS)
        self.imageL = ImageTk.PhotoImage(self.resize_image)
        self.update()

    def update(self):
        ad.Super_ad.update(self, self.imageL, self.pox, self.poy)

    def move(self):
        self.poy += self.vitesse

    def tic(self):
        self.move()
        self.update()