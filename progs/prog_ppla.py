#import traitement_lisye as t
from os import system
from sys import path
path.append("d:\\Espegic\\Tsdi1\\groupe_a\\gestion_notes\\modules")
import pack.traitement_lisye as t
'''
for p in path:
    print(p)
system("pause")
'''
notes=[]
choix=0

while choix!=9:
    system("cls")
    choix=int(input('1. Saisir\n2. Afficher\n3. Tri croissant\n4. Inverser le Tri\n5. Max\n6. Admis\n7. MAx\n8. Non Admis\n9. Quitter\nTapez votre choix ? '))
   
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
    elif choix==6:
        print("Liste des Admis :" )
        t.afficherV(t.getAdmis(notes))
        system("pause")
    elif choix==7:
        print("La plus grande note est :" )
        t.getMax(notes)
        
        system("pause")
    