def saisir(liste, nbr):
    for i in range(nbr):
        liste.append(float(input('Tapez la note num '+str(i+1)+ ' : ')))
    
def afficherV(items):
    for item in items:
        print(item)
def afficherH(items):
    # print(items)    
    for item in items:
        print(item ,end='  ')
    print()
def triCroissant(items):
    #for i in range(len(items)-1):
    isSorted=False
    while not isSorted:
        isSorted=True
        for j in range(len(items)-1):
            if items[j]>items[j+1]:
                #tmp=items[j]
                #items[j]=items[j+1]
                #items[j+1]=tmp
                items[j],items[j+1]=items[j+1],items[j]
                isSorted=False

def triCroissantV1(items):
    items.sort()



'''
def afficher(liste):
    for i in range(len(liste)):
        print(liste[i])
'''