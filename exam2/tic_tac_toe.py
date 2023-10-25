### Import ###

######
### Definitions ###

def afficher_grille(tab):
    print(tab[0])
    print(tab[1])
    print(tab[2])

def jouer(tab,tour):
    y = int(input("Entre la ligne que vous-voulez jouer : "))
    x = int(input("Entre la colonne que vous-voulez jouer : "))
    while (tab[y][x] == "X") or (tab[y][x] == "O"):
        print("Cette case est déjà joué !")
        y = int(input("Entre la ligne que vous-voulez jouer : "))
        x = int(input("Entre la colonne que vous-voulez jouer : "))
    if (tour // 2) == 0:
        tab[y][x] = "X"
    else:
        tab[y][x] = "O"


def verif_victoire(tab):
    for i in range(3):
        #vérifie les lignes horizontales
        if (tab[0][i] == tab[1][i] == tab[2][i] == "X") or (tab[0][i] == tab[1][i] == tab[2][i] == "O") :
            return True
        #verifier les lignes verticales
        if (tab[i][0] == tab[i][1] == tab[i][2] == "X") or (tab[i][0] == tab[i][1] == tab[i][2] == "O"):
            return True
    #vérifie les diagonales
    if (tab[0][0] == tab[1][1] == tab[2][2] == "X") or (tab[0][0] == tab[1][1] == tab[2][2] == "O"):
        return True
    if (tab[0][2] == tab[1][1] == tab[2][0] == "X") or (tab[0][2] == tab[1][1] == tab[2][0] == "O"):
        return True
    
    return False



def verif_grille_complete(tab):
    Flag = True
    for y in range(3):
        for x in range(3):
            if (tab[y][x] != "X") and (tab[y][x] != "O"):
                Flag = False
    return Flag
######

### Test ###

assert verif_victoire([["O","O","O"],[" "," "," "],[" "," "," "]]) == True
assert verif_victoire([[" "," ",""],[" "," "," "],[" "," "," "]]) == False
assert verif_victoire([["X"," ",""],[" ","X"," "],[" "," ","X"]]) == True
assert verif_victoire([["X"," ",""],["X"," "," "],["X"," "," "]]) == True


assert verif_grille_complete([[" "," ",""],[" "," "," "],[" "," "," "]]) == False
assert verif_grille_complete([[" ","X",""],["X"," "," "],["O"," "," "]]) == False
assert verif_grille_complete([["X","O","X"],["X","X","O"],["O","X","X"]]) == True

######

### MAIN ###
tableau = [[(0,0),(0,1),(0,2)],[(1,0),(1,1),(1,2)],[(2,0),(2,1),(2,2)]]
joue = True
tour = 2

while joue:

    afficher_grille(tableau)
    jouer(tableau, tour)
    
    if verif_victoire(tableau):
        afficher_grille(tableau)
        if (tour // 2) == 0 :
            print("Victoire des X !")
        else:
            print("Victoire des O !")
        joue = False
    
    elif verif_grille_complete(tableau):
        afficher_grille(tableau)
        print("Match nul ...")
        joue = False
    tour += 1
######

### question 6 ###
"""
Il faudrait augmenter la taille de la grille et lors des vérifications, 
vérifier seulement si 4 sont allignés et non pas si toute la ligne/colonne/diagonale
est alligné.
"""