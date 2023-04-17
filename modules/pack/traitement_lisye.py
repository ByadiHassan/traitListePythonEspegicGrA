import pickle
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


def getMax(liste):
    max=liste[0]
    for item in liste:
        if item>max:
            max=item
    return max      
def getMin(liste):
    min=liste[0]
    for item in liste:
        if item<max:
            min=item
    return min  
def getAdmis(liste) :
    admis=[]
    for item in liste:
        if item>=10:
            admis.append(item)
        
    return admis
def getMax(liste):
    m=liste[0]
    for i in range(1,len(liste)):
        if liste[i]>m:
            m=liste[i]
    return m
def getMin(liste):
    m=liste[0]
    for i in range(1,len(liste)):
        if liste[i]<m:
            m=liste[i]
    return m
def enregistrer(liste):
    fichier=open('notes.bin','wb')
    pickle.dump(liste,fichier)
    fichier.close()
def charger():
    fichier=open('notes.bin','rb')
    liste=pickle.load(fichier)
    fichier.close()
    return liste

'''
def afficher(liste):
    for i in range(len(liste)):
        print(liste[i])
'''
if __name__=="__main__":
    print("Je suis le module Traitement_Liste")
    print("Test de la fonction getMax")
    print("Max de [10,11,3,77,-4]est ",getMax([10,11,3,77,-4]))
    print("Test de la fonction getMin")
    print("Min de [10,11,3,77,-4]est ",getMin([10,11,3,77,-4]))