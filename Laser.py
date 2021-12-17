import Super_ad as ad
from PIL import Image, ImageTk

class Laser(ad.Super_ad):

    def __init__(self, x):
        self.anim = 0
        self.pox = 50
        self.poy = 80
        self.size = 10

        self.image_data = Image.open("media/img/laser.png")
        self.crop_image = self.image_data.crop((self.anim*682, 0, (self.anim+1)*682, 682))
        self.resize_image = self.crop_image
        self.imageL = ImageTk.PhotoImage(self.resize_image)

        ############################# Binding #############################
        ad.Super_ad.canvas.bind("<Configure>", self.resize)

    def resize(self, e):
        """
        fonction qui s'appelle a chaque modification de la  taille du canvas
        """
        self.resize_image = self.crop_image.resize((self.vw(self.size)+1, self.vw(self.size)+1), Image.ANTIALIAS)
        self.imageL = ImageTk.PhotoImage(self.resize_image)
        self.update()

    def update(self):
        ad.Super_ad.update(self)

        self.crop_image = self.image_data.crop((self.anim*512, 0, (self.anim+1)*512, 682))
        self.resize_image = self.crop_image.resize((self.vw(self.size)+1, self.vw(self.size)+1), Image.ANTIALIAS)
        self.imageL = ImageTk.PhotoImage(self.resize_image)
        ad.Super_ad.canvas.create_image(self.vw(self.pox), self.vh(self.poy), image = self.imageL)

    def tic(self):
        self.anim += 1
        if self.anim > 11:
            self.anim = 0

        self.update()