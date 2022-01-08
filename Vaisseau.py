import Super_ad as ad
from PIL import Image,ImageTk

import Laser as l

class Vaisseau(ad.Super_ad):
    def __init__(self, list_alien):
        self.list_alien = list_alien

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
        self.sprite = ad.Super_ad.canvas.create_image(self.vw(self.pox), self.vh(self.poy), image = "") #on definit l'image avec update dans resize
        self.resize()


        ############################# Binding #############################
        ad.Super_ad.canvas.bind("<Configure>", self.resize, add = "+")
        ad.Super_ad.canvas.bind_all("<KeyPress>", self.key_down, add = "+")
        ad.Super_ad.canvas.bind_all("<KeyRelease>", self.key_up, add = "+")

    def resize(self, *e):
        """
        fonction qui s'appelle a chaque modification de la  taille du canvas
        """
        self.resize_img = self.image_data.resize((self.vw(10)+1, self.vw(10)+1), Image.ANTIALIAS)
        self.imageV = ImageTk.PhotoImage(self.resize_img)
        self.update()

    def update(self):
        ad.Super_ad.update(self, self.imageV, self.pox, self.poy)
        
    def key_down(self,e):
        if e.keysym == "Left" or e.keysym == "q":
            self.is_mooving = "Left"
        if e.keysym == "Right" or e.keysym == "d":
            self.is_mooving = "Right"
        if e.keysym == "Return" or e.keysym == "space":
            self.tire()
    
    def key_up(self,e):
        """
        c pou le peti bug mesie
        """
        if e.keysym == "Left" or e.keysym == "q":
            if self.is_mooving == "Left":
                self.is_mooving = False
        if e.keysym == "Right" or e.keysym == "d":
            if self.is_mooving == "Right":
                self.is_mooving = False

    def tire(self):
        if self.reload:
            self.reload = False
            ad.Super_ad.list_laser.append(l.Laser(self.pox, -self.vitesse_tire, self.force, self.list_alien))
            ad.Super_ad.canvas.after(self.temp_de_recharge, self.reloading)

    def hit(self):
        print("pan")

    def reloading(self):
        self.reload = True

    def tic(self):
        if self.is_mooving == "Left":
            self.pox -= self.vitesse
            if self.pox < 3:
                self.pox = 3
        if self.is_mooving == "Right":
            self.pox += self.vitesse
            if self.pox > 97:
                self.pox = 97
        self.update()
        
        




        
        
    
    