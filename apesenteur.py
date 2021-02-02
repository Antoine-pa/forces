from math import sqrt
"""
la vitesse de chute d'un objet dans le vide avec comme seule
force appliquée a cet objet, n'est pas influencée par la masse/poid/forme...
"""

g = 9.81
t = v = v0 = 0
z0 = float(input("hauteur en mètre(s) : "))

v_impact = sqrt(2*g*z0) #calcul de la vitesse d'impact en m/s
t_impact = sqrt(2*z0/g) #calcul de la durée de chute en s

while True:
    v = -g*t+v0 #calul de la vitesse de l'objet en m/s
    z = -1/2*g*t**2+z0+t*v0 #calcul de l'altitude de l'objet en m

    if t >= t_impact: #si impact
        print(f"impact à {round(t_impact, 4)}s à {round(v_impact, 4)}m/s")
        break
    print(f"{round(t, 3)}s : {round(z, 4)}m, {str(round(v, 4))[1:] if v != 0.0 else str(v)}m/s")
    t += 0.1