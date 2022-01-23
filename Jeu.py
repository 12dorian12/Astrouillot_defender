"""
objectif : cree la class Jeu.
Dates : 17 decembre
fait par : Lea Dorian
Todo : augmenter l'influence du niveau de dificulter sur les attribut d'alien
"""

import tkinter as tk
from PIL import Image, ImageTk

import Super_ad as ad
import Vaisseau as v
import Alien as a
import Ilots as il


class Jeu():
    def __init__(self, window, dimention, fin_du_game, maj_vie, maj_score):
        self.window = window
        self.dimention = dimention
        self.fin_du_game = fin_du_game
        self.maj_vie = maj_vie
        self.maj_score = maj_score

        #on load les immages une seul fois
        ad.Super_ad()

        #creation du canvas principal
        ad.Super_ad.canvas = tk.Canvas(window, bg="black", width=int(dimention), height=int(dimention*(16/9)))

        self.running = False
        self.score = 0


    def make_alien(self, nb, dt):
    #permet de faire spawn des aliens
        self.nb_alien = nb
        self.nb_alien_tuer = 0
        for i in range(nb):
            self.window.after(i*dt, lambda : ad.Super_ad.list_alien.append(a.Alien()))


    def make_wall(self, nb):
    #permet de creer les murs
        for i in range(nb):
            ad.Super_ad.list_bloc.append(il.Ilots((i+1)*100/(nb+1)))

    def make_joueur(self):
        #permet de creer le joueur
        ad.Super_ad.joueur = v.Vaisseau()


    def run(self, ro, col, lvl):
        """permet de lancer le jeu"""
        self.running = True

        ad.Super_ad.canvas.grid(row=ro, column=col)

        if lvl == 1:
            #on definit le bg
            self.resize_bg = ad.Super_ad.image_data_fond1.resize((int(self.dimention*(16/9)**2), int(self.dimention*(16/9))), Image.ANTIALIAS)
            #creation d'aliens
            self.make_alien(20, 300)
        elif lvl == 2:
            #on definit le bg
            self.resize_bg = ad.Super_ad.image_data_fond2.resize((int(self.dimention*(16/9)**2), int(self.dimention*(16/9))), Image.ANTIALIAS)
            #creation d'aliens
            self.make_alien(50, 300)
        elif lvl == 3:
            #on definit le bg
            self.resize_bg = ad.Super_ad.image_data_fond3.resize((int(self.dimention*(16/9)**2), int(self.dimention*(16/9))), Image.ANTIALIAS)
            #creation d'aliens
            self.make_alien(100, 300)

        #creation des blocs
        self.window.after(100, lambda :self.make_wall(10))
        #creation du joueur
        self.window.after(100, self.make_joueur)
        #on affiche le bg
        self.bg = ImageTk.PhotoImage(self.resize_bg)
        self.can_bg = ad.Super_ad.canvas.create_image(-self.dimention/1.25,0, anchor= tk.NW, image = self.bg)
        #on met a jour les infos a l'ecrant une premiere fois
        self.maj_score(self.score)
        self.maj_vie(3)
        #on lance l'horloge
        self.tac()


    def end_game(self, victory):
        if victory:
            self.fin_du_game(True)
        else:
            self.fin_du_game(False)
        
        self.videur(ad.Super_ad.list_alien)
        self.videur(ad.Super_ad.list_bloc)
        self.videur(ad.Super_ad.list_laser)
        if ad.Super_ad.joueur != None :
            ad.Super_ad.joueur.delete()

    def videur(self, liste):
        if len(liste) > 0:
            liste[-1].delete()
            self.videur(liste)


    def distance_eclidienne(self, x1, y1, x2, y2):
        #retourne la distance selon la norme 2
        return ((x1-x2)**2 + (y1-y2)**2)**(1/2)

    def colision(self):
        for laser in ad.Super_ad.list_laser:
            for bloc in ad.Super_ad.list_bloc:
                if self.distance_eclidienne(laser.pox, laser.poy, bloc.pox, bloc.poy) <= 5:
                    bloc.hit(laser.force)
                    if laser in ad.Super_ad.list_laser:
                        laser.delete()
            if laser.vitesse < 0:
                for alien in ad.Super_ad.list_alien:
                    if self.distance_eclidienne(laser.pox, laser.poy, alien.pox, alien.poy) <= 5:
                        if laser in ad.Super_ad.list_laser:
                            laser.delete()
                        if alien.hit(laser.force):
                            self.nb_alien_tuer += 1
                            self.score += 100
                            self.maj_score(self.score)
            if laser.vitesse > 0:
                if self.distance_eclidienne(laser.pox, laser.poy, ad.Super_ad.joueur.pox, ad.Super_ad.joueur.poy) <= 5:
                    if laser in ad.Super_ad.list_laser:
                        laser.delete()
                    if ad.Super_ad.joueur.hit(laser.force):
                        self.running = False
                        self.end_game(False)
                        return 0 #on arrette les colision
                    else :
                        self.maj_vie(ad.Super_ad.joueur.nb_vies)

        for alien in ad.Super_ad.list_alien:
            for bloc in ad.Super_ad.list_bloc:
                if self.distance_eclidienne(alien.pox, alien.poy, bloc.pox, bloc.poy) <= 5:
                    tmp = bloc.nb_vies #sinon le nb de point de vie diminue une fois le hit effectuer
                    bloc.hit(alien.nb_vies)
                    if alien.hit(tmp):
                        self.nb_alien_tuer +=1
                        self.score -= 100
                        self.maj_score(self.score)

            if self.distance_eclidienne(alien.pox, alien.poy, ad.Super_ad.joueur.pox, ad.Super_ad.joueur.poy) <= 5:
                # sinon le nb de point de vie diminue une fois le hit effectuer
                tmp = ad.Super_ad.joueur.nb_vies
                if ad.Super_ad.joueur.hit(alien.nb_vies):
                    self.running = False
                    self.end_game(False)
                    return 0  # on arrette les colision
                else:
                    self.maj_vie(ad.Super_ad.joueur.nb_vies)

                if alien.hit(tmp):
                    self.nb_alien_tuer += 1
                    self.score += 1000
                    self.maj_score(self.score)


    def tac(self):
        """
        fonction qui appel tout les tic de nos objet toutes les 26 millisecondes
        """
        #le joueuer n'est pas cree tout de suite
        if ad.Super_ad.joueur != None:
            ad.Super_ad.joueur.tic()

            for alien in ad.Super_ad.list_alien:
                alien.tic()

            for tir in ad.Super_ad.list_laser : 
                tir.tic()

            self.colision()

            if self.nb_alien == self.nb_alien_tuer:
                self.running = False
                self.end_game(True)

        if self.running:
            self.window.after(26, self.tac)
