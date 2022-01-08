import Super_ad as ad
from PIL import Image, ImageTk

class Laser(ad.Super_ad):
    image_data = Image.open("media/img/laser.png")
    image_lst = []
    for i in range(12):
        image_lst.append(image_data.crop((i*512, 0, (i+1)*512, 682)))

    def __init__(self, x, vitesse, force):
        self.anim = 0
        self.pox = x
        self.poy = 90
        self.size = 10
        self.vitesse = vitesse
        self.force = force

        self.image_data = Laser.image_data
        self.image_lst = Laser.image_lst
        self.resize_image = self.image_lst[self.anim].resize((self.vw(self.size)+1, self.vw(self.size)+1), Image.ANTIALIAS)
        self.imageL = ImageTk.PhotoImage(self.resize_image)
        self.sprite = ad.Super_ad.canvas.create_image(self.vw(self.pox), self.vh(self.poy), image = self.imageL)

        ############################# Binding #############################
        ad.Super_ad.canvas.bind("<Configure>", self.resize, add = "+")

    def resize(self, e):
        """
        fonction qui s'appelle a chaque modification de la  taille du canvas
        """
        self.resize_image = self.image_lst[self.anim].resize((self.vw(self.size)+1, self.vw(self.size)+1), Image.ANTIALIAS)
        self.imageL = ImageTk.PhotoImage(self.resize_image)
        self.update()

    def update(self):
        self.imageL = ImageTk.PhotoImage(self.resize_image)
        ad.Super_ad.update(self, self.imageL, self.pox, self.poy)

    def animate(self):
        self.anim += 1
        if self.anim > 11:
            self.anim = 0
        self.resize_image = self.image_lst[self.anim].resize((self.vw(self.size)+1, self.vw(self.size)+1), Image.ANTIALIAS)

    def move(self):
        self.poy += self.vitesse

    def tic(self):
        self.move()
        
        self.animate()

        self.update()