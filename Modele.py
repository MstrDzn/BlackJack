from random import *
import pygame
class card :
    def __init__(self,valeur,couleur):
        self.valeur = valeur
        self.couleur = couleur
        self.noms_couleurs = ["coeur", "carreau", "pique", "trèfle"]
        self.noms_valeurs = [None, "as", "2", "3", "4", "5", "6", "7", "8", "9", "10", "valet", "dame", "roi"]
        self.image=pygame.image.load(r"./cards/"+str(valeur)+str(couleur)+".png")
        self.image=pygame.transform.scale(self.image, (69,105))
        
    def __str__(self) :
        return '%s_de_%s' % (self.noms_valeurs[self.valeur], self.noms_couleurs[self.couleur])


class paquet :
    def __init__(self) :
        self.cartes = []
        for couleur in range(0,4) :
            for valeur in range(1,14) :
                carte = card(valeur,couleur)
                self.cartes.append(carte)

    def __str__(self):
        liste = []
        for carte in self.cartes :
            liste.append(str(carte))
        return '\n'.join(liste)
    
    def melange(self) :
        shuffle(self.cartes)


class joueur :
    def __init__(self) :
        self.main_joueur = []

    def calculer_main(self,cartes):
        val = 0
        for carte in cartes :
            if 1 < carte.valeur <= 10 :
                val += carte.valeur
            elif carte.valeur > 10 :
                val += 10
            elif carte.valeur ==1:
                val +=11
        return val
backcard=pygame.image.load(r"./cards/backcard.png")
#backcard=pygame.transform.scale(backcard, (103,157))
backcard_rect=backcard.get_rect()

deck=paquet()
