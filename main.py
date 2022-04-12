
from tkinter import *
from random import shuffle

COTE = 120
PAD = 5
SIDE = COTE + PAD

NB_LIG = 4
NB_COL = 5

LARG = SIDE * NB_COL
HAUT = SIDE * NB_LIG
X0 = Y0 = SIDE // 2

NB_CARTES = NB_LIG * NB_COL // 2

LANG=['Sardoche', 'tomy', 'inoxtag', 'Rebeu-Deter', 'Kameto', 'michou meme',
      'amaru', 'AmineMatue', 'doigby', 'pfut']


def melanger_grille() :
    cartes = list(range(NB_CARTES)) * 2
    print(cartes)
    shuffle(cartes)
    print(cartes)



    P = []
    k = 0
    for lig in range(NB_LIG) :
        L = []
        for col in range(NB_COL):
            L.append(cartes[k])
            k += 1
        P.append(L)
        
    return P


fen = Tk()
cnv = Canvas(fen, width = LARG, height = HAUT, bg='gray')
cnv.pack()

cover = PhotoImage(file="./images/cover.gif")
plateau = melanger_grille()



logos=[]

for lang in LANG:
    fichier = "./images/" + lang +  ".gif"
    logo = PhotoImage(file = fichier)
    logos.append(logo)
print()
print(plateau)


# Placement des images
for lig in range(NB_LIG) :
    for col in range(NB_COL) :
        centre = (X0 + col * SIDE, Y0 + lig * SIDE)
        nro = plateau[lig][col]
        logo = logos[nro]
        cnv.create_image(centre, image = logo)
        print(logo, end= " ")
    
    print()

    print()
    
    



















fen.mainloop() 

