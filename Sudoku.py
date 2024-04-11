# Travail réalisé par Gaspard Cotte et Guillaume Bouton
grille = [[3, 1, 0, 0, 0, 2, 0, 0, 0], \
          [0, 0, 0, 0, 0, 0, 4, 0, 3], \
          [0, 4, 5, 0, 7, 0, 1, 0, 0], \
          [0, 0, 0, 0, 0, 0, 0, 4, 0], \
          [7, 0, 0, 6, 1, 3, 0, 0, 2], \
          [0, 8, 0, 0, 0, 0, 0, 0, 0], \
          [0, 0, 2, 0, 3, 0, 8, 6, 0], \
          [5, 0, 8, 0, 0, 0, 0, 0, 0], \
          [0, 0, 0, 5, 0, 0, 0, 7, 1]]

def afficheGrille(g):
    for ii in range(3):
        print()
        for i in range(3):
            print(end = "\t")
            for jj in range(3):
                for j in range(3):
                    if g[3*ii+i][3*jj+j] != 0:
                        print(g[3*ii+i][3*jj+j], end=" ")
                    else:
                        print(".", end=" ")
                print(end = "\t")
            print()

def caseVide(g):
    for i in range(len(g)): # On prend l'indice de ligne
        for j in range(len(g[i])):# On prend l'indice de colone
            if g[i][j]==0 :
                return (i,j) # La valeur à (i,j) est donc la première valeur égale à 0 du tableau
    return (-1,-1) # Aucune valeur n'est égale à 0 

def verifDansLigne(g, i, num):
    for j in range(len(g)): # i est fixe puisqu'on regarde la ligne et j varie pour pouvoir tester toute la ligne
        if g[i][j]==num:
            return False # Puisque la valeur a (i,j) est égale à num, la valeur num est déjà présente dans la ligne 
    return True # La valeur num est donc pas présente dans la ligne

def verifDansColonne(g, j, num):
    for i in range(len(g)):# j est fixe puisqu'on regarde la colonne et i varie pour pouvoir tester toute la colonne
        if g[i][j]==num:
            return False # Puisque la valeur a (i,j) est égale à num, la valeur num est déjà présente dans la colonne
    return True # La valeur num est donc pas présente dans la colonne

def verifDansCarre(g, i, j, num):
    for k in range(3):          # k prend les valeurs de 0 à 2
        if num in g[i//3*3+k][j//3*3:(j//3+1)*3]:
            # je prend i que je divise et multiplie par 3
            # pour trouver la première ligne de carré.
            # j'ajoute k à cette première ligne
            # pour parcourir toutes les lignes du carré
            
            # je prend j que je divise et multiplie par 3
            # pour trouver la première case de carré.
            # ensuite je reprend j que je redivise par 3 
            # mais cette fois je lui ajoute puis je multiplie par 3
            # pour avoir la dernière case du carré.
            
            # Je vérifie ensuite entre la première et la dernière case
            # du carré, dans la première ligne+k du carré si il y a num.
            return False
    return True

def verifValeurPossible(g, i, j, num):
    if verifDansLigne(g, i, num) and verifDansColonne(g, j, num) and verifDansCarre(g, i, j, num):
        # je vérifie si toute les fonctions sont True et si oui je revoie True
        return True
    return False    # si non je renvoie False
 

def resoudre(g):
    i, j = caseVide(g)
    if (i,j) == (-1,-1):
        return True
    else:
        for num in range(1,10):
            if verifValeurPossible(g, i, j, num):
                g[i][j] = num
                if resoudre(g):
                    return True
                else :
                    g[i][j] = 0
        return False


#tests
afficheGrille(grille)
assert caseVide(grille) == (0,2), "erreur0"
assert verifDansLigne(grille, 4, 3) == False, "erreur1"
assert verifDansLigne(grille, 7, 3) == True, "erreur1"
assert verifDansColonne(grille, 4, 3) == False, "erreur2"
assert verifDansColonne(grille, 7, 3) == True, "erreur2"
assert verifDansCarre(grille, 7, 5, 3) == False, "erreur3"
assert verifDansCarre(grille, 7, 5, 2) == True, "erreur3"
assert verifValeurPossible(grille, 7, 5, 3) == False, "erreur4"
assert verifValeurPossible(grille, 7, 5, 4) == True, "erreur4"


# programme : résolution du soduku
resoudre(grille)
afficheGrille(grille)
