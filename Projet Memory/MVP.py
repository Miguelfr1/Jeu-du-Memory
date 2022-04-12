from tkinter import *
from random import shuffle
'''dimensions des cartes'''

COTE = 120
PAD = 5
SIDE = COTE + PAD

NB_LIG = 4
NB_COL = 5

LARG = SIDE * NB_COL
HAUT = SIDE * NB_LIG
X0 = Y0 = SIDE // 2

NB_CARTES = NB_LIG * NB_COL // 2
'''Liste de toute mes photos choisies'''
LANG=['Sardoche', 'tomy', 'inoxtag', 'Rebeu-Deter', 'Kameto', 'michou meme',
      'amaru', 'AmineMatue', 'doigby', 'pfut']


def melanger_grille() : 
      ''' permet de faire une liste avec 2 fois chaque carte puis de les melanger'''
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
'''creation de l'interphace tkinter'''
fen = Tk()
cnv = Canvas(fen, width = LARG, height = HAUT, bg='gray')
cnv.pack()
cover = PhotoImage(file="./images/cover.gif")
plateau = melanger_grille()


''' la liste de tout les elements devient une liste de liste avec 5 liste de 4 elements'''
logos=[]

for lang in LANG:
    fichier = "./images/" + lang +  ".gif"
    logo = PhotoImage(file = fichier)
    logos.append(logo)
print()
print(plateau)


'''placement des listes par ligne et par colonne'''
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
