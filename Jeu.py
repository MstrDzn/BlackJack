from random import * 
from Modele import *

class jeu :
    def __init__(self) :
        self.joueur = joueur()
        self.croupier = joueur()
        self.joueur.main_joueur = []
        self.croupier.main_joueur = []
        self.jeu_paquet = paquet()
        
    def distribution(self) :
        self.jeu_paquet.melange()
        for i in range(0,2) :
            self.joueur.main_joueur.append(self.jeu_paquet.cartes.pop())
            self.croupier.main_joueur.append(self.jeu_paquet.cartes.pop())


    def tirer(self, a):
        t = len(self.jeu_paquet.cartes)
        if t > 0:
            carte = self.jeu_paquet.cartes[0]
            del(self.jeu_paquet.cartes[0])
            if a=="j":
                self.joueur.main_joueur.append(carte)
            if a=="c":
                self.croupier.main_joueur.append(carte)
        else:
            return None
    
    def jouer (self) :
        self.distribution()
        j = self.joueur.calculer_main(self.joueur.main_joueur)
        c = self.croupier.calculer_main(self.croupier.main_joueur)
        print(self.joueur.main_joueur[0].valeur,self.joueur.main_joueur[1].valeur, self.croupier.main_joueur[0].valeur)
        print("\nVotre main de départ vaut :", j)
        while j < 21 :
            
            pioche = input("\nVoulez-vous piocher une carte ? Oui pour piocher\n")
            if pioche == "Oui" :
                self.joueur.tirer()
            j = self.joueur.calculer_main(self.joueur.main_joueur)
            print("Votre main vaut ", j)

            if j == 21 :
                return ("\nBlackjack !")
            if pioche == "Non" :
                
                while c < 17 :
                    self.croupier.tirer()
                    c = self.croupier.calculer_main(self.croupier.main_joueur)
                if c == 21 :
                    return("Blackjack ! Vous avez perdu")
                if c > 21 :
                    return("Le croupier a dépassé 21 ! Vous avez gagné !")
            
                j = self.joueur.calculer_main(self.joueur.main_joueur)
                print("La somme des cartes du croupier vaut ", c)
                if j > c :
                    return ("\nVous avez gagné !\n")
                elif j < c :
                    return ("\nVous avez perdu !\n")
                elif j == c :
                    return ("\nEgalité !\n")
        return ("Vous avez perdu")
            
if __name__ == "__main__" :
    jeu_test = jeu()

