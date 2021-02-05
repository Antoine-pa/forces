from tkinter import *
tk = Tk()

#paramètrage fenetre
tk.title("interface des forces")
tk.minsize(600, 360)
largeur_ecran = tk.winfo_screenwidth()
hauteur_ecran = tk.winfo_screenheight()
largeur_fenetre = 1000
hauteur_fenetre = 600
X = largeur_ecran // 2 - largeur_fenetre // 2
Y = hauteur_ecran // 2 - hauteur_fenetre // 2
tk.geometry(f"{largeur_fenetre}x{hauteur_fenetre}+{X}+{Y}")

#observateurs

#var de controles...

#widgets...
name = LabelFrame(tk, text = "titre", height = 200, width = 500, borderwidth = 5)
name.pack()

#main boucle
tk.mainloop()
