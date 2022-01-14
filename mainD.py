import tkinter as tk
import Jeu as j


root = tk.Tk()
root.title("Astrouillot Defender")
root.minsize(400,400)

partie = j.Jeu(root)
partie.run()

root.mainloop()