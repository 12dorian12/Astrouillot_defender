import tkinter as tk
import Jeu as j


root = tk.Tk()
root.title("Astrouillot Defender")
root.minsize(900,900)

partie = j.Jeu(root)
partie.run()

root.mainloop()