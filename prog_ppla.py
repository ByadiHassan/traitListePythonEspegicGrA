import traitement_lisye as t
from os import system
notes=[]
choix=0
system("cls")
while choix!=6:
    choix=int(input('1. Saisir\n2. Afficher\n3. Tri croissant\n4. Inverser le Tri\n5.Max\n6. Quitter\nTapez votre choix ? '))
    if choix==1:
        nbr= int(input('Combien de notes voulez vous traiter ?'))
        t.saisir(notes,nbr)
        #system('cls')
    elif choix==2:
        t.afficherH(notes)
        system("pause")
        #system('cls')

    elif choix==3:
        t.triCroissant(notes)
        t.afficherV(notes)
        system("pause")
        #system('cls')
    elif choix==4:
        notes=notes[::-1]
        t.afficherV(notes)
        system("pause")
        #system('cls')

    elif choix==5:
        print("La plus grande note de la liste est :",t.getMax(notes) )
        system("pause")
    system('cls')