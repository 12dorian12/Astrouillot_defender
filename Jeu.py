import tkinter as tk
from PIL import Image

import Super_ad as ad
import Vaisseau as v
import Alien as a
import Ilots as il


class Jeu():
    def __init__(self, window):
        self.window = window

        #initialisation de Super_ad
        self.heart = ad.Super_ad(self.window, 500)



    def make_alien(self, nb, dt):
    #permet de faire spawn des aliens
        for i in range(nb):
            self.window.after(i*dt, lambda : ad.Super_ad.list_alien.append(a.Alien()))


    def make_wall(self, nb, ec):
        #permet de creer les murs
        for i in range(nb):
            il.Ilots().pox += ec
            self.window(ad.Super_ad.list_bloc.append(il.Ilots()))


    def run(self):
    #permet de lancer le jeu
        ad.Super_ad.canvas.pack()#fill="both", expand="yes"
        #creation du joueur
        ad.Super_ad.joueur = v.Vaisseau()
        #creation d'aliens
        self.make_alien(20, 300)
        self.tac()
        #creation des blocs
        ad.Super_ad.mur = il.Ilots()
        #self.make_wall(3, 10)





    def tac(self):
    #Tac est une horloge globale, elle apelle la fonction tic de chaque objet 60 fois par seconde
        ad.Super_ad.joueur.tic()

        for alien in ad.Super_ad.list_alien:
            alien.tic()

        for tir in ad.Super_ad.list_laser : 
            tir.tic()

        self.window.after(26, self.tac)