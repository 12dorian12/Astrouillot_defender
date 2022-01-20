import tkinter as tk
from PIL import Image

import Super_ad as ad
import Vaisseau as v
import Alien as a
import Ilots as il


class Jeu():
    def __init__(self, window, ayer_finit, dimention):
        self.window = window
        self.ayer_finit = ayer_finit

        #initialisation de Super_ad
        self.heart = ad.Super_ad(self.window, dimention, ad.Super_ad.image_data_fond1)



    def make_alien(self, nb, dt):
    #permet de faire spawn des aliens
        for i in range(nb):
            self.window.after(i*dt, lambda : ad.Super_ad.list_alien.append(a.Alien()))


    def make_wall(self, nb, ec):
    #permet de creer les murs
        for i in range(nb):
            ad.Super_ad.list_bloc.append(il.Ilots((i+1)*ec))


    def run(self, ro, col):
    #permet de lancer le jeu
        ad.Super_ad.canvas.grid(row = ro, column=col)
        #creation du joueur
        ad.Super_ad.joueur = v.Vaisseau()
        #creation d'aliens
        self.make_alien(20, 300)
        #creation des blocs
        self.make_wall(10, 5)

        self.tac()


    def end_game(self, victory):
        if victory:
            print("victoiiiire")
            self.ayer_finit(True)
        else:
            print("tes nuuuul")
            self.ayer_finit(False)
        for i in ad.Super_ad.list_alien : 
            i.delete()
        for i in ad.Super_ad.list_bloc : 
            i.delete()
        for i in ad.Super_ad.list_laser : 
            i.delete()
        ad.Super_ad.joueur.delete()


    def distance_eclidienne(self, x1, y1, x2, y2):
        #retourne la distance selon la norme 2
        return ((x1-x2)**2 + (y1-y2)**2)**(1/2)

    def colision(self):
        for laser in ad.Super_ad.list_laser:
            for bloc in ad.Super_ad.list_bloc:
                if self.distance_eclidienne(laser.pox, laser.poy, bloc.pox, bloc.poy) <= 5:
                    bloc.hit(laser.force)
                    laser.delete()
            if laser.vitesse < 0:
                for alien in ad.Super_ad.list_alien:
                    if self.distance_eclidienne(laser.pox, laser.poy, alien.pox, alien.poy) <= 5:
                        alien.hit(laser.force)
                        laser.delete()
            if laser.vitesse > 0:
                if self.distance_eclidienne(laser.pox, laser.poy, ad.Super_ad.joueur.pox, ad.Super_ad.joueur.poy) <= 5:
                    ad.Super_ad.joueur.hit(laser.force)
                    laser.delete()

        for alien in ad.Super_ad.list_alien:
            for bloc in ad.Super_ad.list_bloc:
                if self.distance_eclidienne(alien.pox, alien.poy, bloc.pox, bloc.poy) <= 5:
                    tmp = bloc.nb_vies #sinon le nb de point de vie diminue une fois le hit effectuer
                    bloc.hit(alien.nb_vies)
                    alien.hit(tmp)


    def tac(self):
    #Tac est une horloge globale, elle apelle la fonction tic de chaque objet 60 fois par seconde
        ad.Super_ad.joueur.tic()

        for alien in ad.Super_ad.list_alien:
            alien.tic()

        for tir in ad.Super_ad.list_laser : 
            tir.tic()
        
        """ if len(ad.Super_ad.list_alien) == 0:
            self.end_game(True) """

        self.colision()
        self.window.after(26, self.tac)