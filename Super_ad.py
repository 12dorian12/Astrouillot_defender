from tkinter import Canvas


class Super_ad():

    canvas = None

    def __init__(self):
        pass

    """
    les deux fonctions suivantes permettent d'avoir la postion 
    en px sur le canvas a partir d'un pourcentage
    """
    def vw(self, x):
        return int(Super_ad.canvas.winfo_width()*x/100)
    def vh(self, y):
        return int(Super_ad.canvas.winfo_height()*y/100)

    def update(self):
        #Super_ad.canvas.delete("all")
        a = 0