import Super_ad as ad
import tkinter as tk
from PIL import Image,ImageTk

class Vaisseau(ad.Super_ad):
    def __init__(self):
        self.nb_vies = 3
        self.pox = 50
        self.poy = 94
        self.vitesse = 1

        self.is_mooving = False

        self.img_data = Image.open("media/img/vaisseau.png")
        self.resize_img = self.img_data
        self.imageV = ImageTk.PhotoImage(self.resize_img)


        ############################# Binding #############################
        ad.Super_ad.canvas.bind("<Configure>", self.resize)
        ad.Super_ad.canvas.bind_all("<KeyPress>", self.key_down)
        ad.Super_ad.canvas.bind_all("<KeyRelease>", self.key_up)

    def resize(self, e):
        """
        fonction qui s'appelle a chaque modification de la  taille du canvas
        """
        self.resize_img = self.img_data.resize((self.vw(10)+1, self.vw(10)+1), Image.ANTIALIAS)
        self.imageV = ImageTk.PhotoImage(self.resize_img)
        self.update()

    def update(self):
        ad.Super_ad.update(self)
        ad.Super_ad.canvas.create_image(self.vw(self.pox), self.vh(self.poy), image = self.imageV)
        
    def key_down(self,e):
        if e.keysym == "Left":
            self.is_mooving = "Left"
        if e.keysym == "Right":
            self.is_mooving = "Right"
    
    def key_up(self,e):
        """
        c pou le peti bug mesie
        """
        if e.keysym == "Left" and self.is_mooving == "Left":
            self.is_mooving = False
        if e.keysym == "Right" and self.is_mooving == "Right":
            self.is_mooving = False

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
        




        
        
    
    