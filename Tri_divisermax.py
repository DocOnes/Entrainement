from random import randint

liste=[]
longueurliste=int(input("combien de valeur dans la liste ?:"))
for i in range(longueurliste):
    liste.append(randint(1,10000))

print(liste)

def sort(liste):
    max=0
    listesort=[]
    lenliste=len(liste)
    for k in range(lenliste):
        listesort.append([])
    for i in liste:
        if i>max:
            max=i
    for i in range(lenliste):
        liste[i]=(liste[i]//max)*(lenliste-1)
        listesort[liste[i]]=liste[i]
        print(listesort)