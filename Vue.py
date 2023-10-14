from random import *
from Modele import *
from Jeu import *
import pygame
import random
import time
from pygame import mixer


#Constantes
#tailles de fenêtre
width=1280
height=720
#couleurs
black= (0,0,0)
white= (255,255,255)
light_green=(0,120,0)
red=(255,0,0)
pygame.init()

screen = pygame.display.set_mode((width,height))
#screen.fill(light_green)
screen.fill(black)


#nom et logo

pygame.display.set_caption("BlackJack")
pygame.display.set_icon(pygame.image.load("logo.png"))

def play():
    game=jeu()
    #police
    small_font = pygame.font.Font(None,32)
    large_font = pygame.font.Font(None,50)
    title_font = pygame.font.Font(None, 70)

    #BOUTTONS
    pygame.mixer.init()
    bg=mixer.Sound("background2.wav")
    draw=mixer.Sound("card_draw0.wav")
    victory=mixer.Sound("VICTORY.wav")
    pioche_bouton = large_font.render("TIRER", True, white, black)

    passe_bouton = large_font.render("RESTER", True, white, black)

    commencer_bouton=title_font.render("CLIQUEZ MOI POUR COMMENCER", True, white)

    perdu_bouton=title_font.render("VOUS AVEZ PERDU", True, white, black)
    gagne_bouton=title_font.render("VOUS AVEZ GAGNÉ", True, white, black)
    egalite_bouton=title_font.render("C'EST UNE ÉGALITÉ", True, white, black)
    recommencer_bouton=large_font.render("RECOMMENCER", True, white, black)
    quitter_bouton=large_font.render("QUITTER", True, white, black)
    #Rectangles

    pioche_bouton_rect=pioche_bouton.get_rect()
    passe_bouton_rect=passe_bouton.get_rect()
    commencer_bouton_rect=commencer_bouton.get_rect()

    perdu_bouton_rect=perdu_bouton.get_rect()
    gagne_bouton_rect=gagne_bouton.get_rect()
    egalite_bouton_rect=egalite_bouton.get_rect()
    recommencer_bouton_rect=recommencer_bouton.get_rect()
    quitter_bouton_rect=quitter_bouton.get_rect()

    pioche_bouton_rect.center=(450,620)
    passe_bouton_rect.center=(830,620)
    commencer_bouton_rect.center=(640,360)

    quitter_bouton_rect.center=(420,620)
    recommencer_bouton_rect.center=(830,620)
    perdu_bouton_rect.center=(640,360)
    gagne_bouton_rect.center=(640,360)
    egalite_bouton_rect.center=(640,360)
    #variables

    def do_main():
        game.distribution()
        j = game.joueur.calculer_main(game.joueur.main_joueur)
        c = game.croupier.calculer_main(game.croupier.main_joueur)
        return j,c

    clock = pygame.time.Clock()
    resultat=""
    temps = pygame.time.get_ticks()
    main,main_croupier = do_main()
    choix= 3
    fin = False
    game.joueur.main_joueur[0].image.get_rect()
    imagemain0=game.joueur.main_joueur[0].image
    imagemain1=game.joueur.main_joueur[1].image
    imagemain0_rect=imagemain0.get_rect()
    imagemain1_rect=imagemain1.get_rect()
    imagemain0_rect.center=(465,470)
    imagemain1_rect.center=(550,470)
    imagemaincroupier0=game.croupier.main_joueur[0].image
    imagemaincroupier1=game.croupier.main_joueur[1].image
    imagemaincroupier0_rect=imagemaincroupier0.get_rect()
    imagemaincroupier1_rect=imagemaincroupier1.get_rect()
    imagemaincroupier0_rect.center=(465,100)
    imagemaincroupier1_rect.center=(553,100)
    l=[i for i in range(-100,-1)]
    l2=[i for i in range(0,101)]
    #Boucle de game

    while True:
        mouse=pygame.mouse.get_pos()
        for event in pygame.event.get():

            #Quitting events
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            #CLIC GAUCHE EVENTS
            if not fin and event.type == pygame.MOUSEBUTTONDOWN:
                if 760 <= mouse[0] <= 900 and 600 <= mouse[1] <= 640 and choix in [-1, -2, -3]: #TEST POUR SAVOIR SI LE JOUEUR SE COUCHE
                    choix = 1
                    
                if 370 <= mouse[0] <= 530 and 600 <= mouse[1] <= 640 and choix not in l: #TEST POUR SAVOIR SI LE JOUEUR TIRE
                    choix = 0

                if 370 <= mouse[0] <= 530 and 600 <= mouse[1] <= 640 and choix==-2: #TEST POUR SAVOIR SI LE JOUEUR TIRER
                    choix = 4

                if 370 <= mouse[0] <= 530 and 600 <= mouse[1] <= 640 and choix==-3: #TEST POUR SAVOIR SI LE JOUEUR TIRER
                    choix = 5
                    
                if 0<=mouse[0]<=1280 and 0<=mouse[1]<=720: #lancement du game
                    if choix == 3:
                        choix=2

                #TEST DU QUITTAGE

                if 690 <= mouse[0] <= 965 and 600 <= mouse[1] <= 640 and choix==-100: #TEST POUR SAVOIR SI LE JOUEUR SE COUCHE
                    choix = 12
                    

                if 340 <= mouse[0] <= 490 and 600 <= mouse[1] <= 640 and choix==-100: #TEST POUR SAVOIR SI LE JOUEUR TIRE
                    choix = 404
                    
            if choix==0: #PREMIER TIRAGE
                game.tirer("j")
                main=game.joueur.calculer_main(game.joueur.main_joueur)
                imagemain0=game.joueur.main_joueur[2].image
                imagemain0_rect.center=(640,470)
                screen.blit(imagemain0, imagemain0_rect)
                valeur=large_font.render("Valeur de votre main: "+str(main), True, white, red)
                valeur_rect=valeur.get_rect()
                valeur_rect.center=(640,560)
                screen.blit(valeur, valeur_rect)
                draw.play(0)
                pygame.display.update()
                pygame.time.wait(2000)
                if main==21:
                    choix=14
                else:
                    if main==main_croupier:
                        choix=13
                    if main<=21:
                        choix = -2
                    else:
                        choix = 10
        
     
                    
            if choix==2: #initiation du game avant le premier choix
                screen.fill(light_green)
                screen.blit(pygame.image.load("Background.png").convert(), [0,0])
                screen.blit(pioche_bouton, pioche_bouton_rect)
                screen.blit(passe_bouton, passe_bouton_rect)
                screen.blit(imagemain0, imagemain0_rect)
                screen.blit(imagemain1, imagemain1_rect)
                valeur=large_font.render("Valeur de votre main: "+str(main), True, white, red)
                valeur_rect=valeur.get_rect()
                valeur_rect.center=(640,560)
                screen.blit(valeur, valeur_rect)
                backcard_rect=(520,50)
                screen.blit(backcard,backcard_rect)
                screen.blit(imagemaincroupier0, imagemaincroupier0_rect)
                bg.play(-1)
                choix=-1
                    

            if choix == 4: #deuxieme tirage
                game.tirer("j")
                main=game.joueur.calculer_main(game.joueur.main_joueur)
                imagemain0=game.joueur.main_joueur[3].image
                imagemain0_rect.center=(730,470)
                screen.blit(imagemain0, imagemain0_rect)
                valeur=large_font.render("Valeur de votre main: "+str(main), True, white, red)
                valeur_rect=valeur.get_rect()
                valeur_rect.center=(640,560)
                screen.blit(valeur, valeur_rect)
                draw.play(0)
                pygame.display.update()
                pygame.time.wait(2000)
                if main == 21:
                    choix=14
                else:
                    if main==main_croupier:
                        choix=13
                    if main<=21:
                        choix = -3
                    else:
                        choix=10
                
            if choix == 5: #troisieme tirage
                game.tirer("j")
                main=game.joueur.calculer_main(game.joueur.main_joueur)
                imagemain0=game.joueur.main_joueur[4].image
                imagemain0_rect.center=(820,470)
                screen.blit(imagemain0, imagemain0_rect)
                valeur=large_font.render("Valeur de votre main: "+str(main), True, white, red)
                valeur_rect=valeur.get_rect()
                valeur_rect.center=(640,560)
                screen.blit(valeur, valeur_rect)
                draw.play(0)
                pygame.display.update()
                pygame.time.wait(2000)
                if main == 21:
                    choix=14
                else:                   
                    if main==main_croupier:
                        choix=13
                    if main<=21:
                        choix = -4
                    else:
                        choix=10
                
            if choix ==1: #couchage
                screen.blit(imagemaincroupier1, imagemaincroupier1_rect)
                draw.play(0)
                pygame.display.update()
                time.sleep(2)
                if main_croupier<17 and main_croupier<=main:
                    game.tirer("c")
                    main_croupier=game.croupier.calculer_main(game.croupier.main_joueur)
                    imagecroupier2=game.croupier.main_joueur[2].image
                    imagecroupier2_rect=imagecroupier2.get_rect()
                    imagecroupier2_rect.center=(641,100)
                    screen.blit(imagecroupier2,imagecroupier2_rect)
                    draw.play(0)
                    if main_croupier<17 and main_croupier<=main:
                        pygame.display.update()
                        pygame.time.wait(2000)
                        game.tirer("c")
                        main=game.croupier.calculer_main(game.joueur.main_joueur)
                        imagecroupier3=game.croupier.main_joueur[3].image
                        imagecroupier3_rect=imagecroupier3.get_rect()
                        imagecroupier3_rect.center=(729,100)
                        screen.blit(imagecroupier3,imagecroupier3_rect)
                        draw.play(0)
                        if main_croupier<17 and main_croupier<=main:
                            pygame.display.update()
                            pygame.time.wait(2000)
                            game.tirer("c")
                            main=game.joueur.calculer_main(game.joueur.main_joueur)
                            imagecroupier4=game.croupier.main_joueur[4].image
                            imagecroupier4_rect=imagecroupier4.get_rect()
                            imagecroupier4_rect.center=(817,100)
                            screen.blit(imagecroupier4,imagecroupier4_rect)
                            draw.play(0)
                pygame.display.update()
                pygame.time.wait(3000)
                if main == 21:
                    choix=14
                else:
                    if main==main_croupier:
                        choix=13
                    if main<main_croupier and main_croupier<=21:
                        choix=10
                    else:
                        choix=11
                
            if choix==10: #perdu
                bg.stop()
                screen.fill(black)
                screen.blit(perdu_bouton, perdu_bouton_rect)
                screen.blit(recommencer_bouton, recommencer_bouton_rect)
                screen.blit(quitter_bouton, quitter_bouton_rect)
                choix = -100

            if choix==11: #gagné
                bg.stop()
                screen.fill(black)
                screen.blit(gagne_bouton, gagne_bouton_rect)
                screen.blit(recommencer_bouton, recommencer_bouton_rect)
                screen.blit(quitter_bouton, quitter_bouton_rect)
                choix = -100
                
            if choix==13:
                bg.stop()
                screen.fill(black)
                screen.blit(egalite_bouton, egalite_bouton_rect)
                screen.blit(recommencer_bouton, recommencer_bouton_rect)
                screen.blit(quitter_bouton, quitter_bouton_rect)
                choix = -100

            if choix==14:
                bg.stop()
                victory.play(0)
                screen.blit(pygame.image.load("Blackjackscreen.png"), [0,0])
                screen.blit(recommencer_bouton, recommencer_bouton_rect)
                screen.blit(quitter_bouton, quitter_bouton_rect)
                choix = -100
                
            if choix==12:
                victory.stop()
                screen.fill(black)
                return None
            
            if choix==404:
                pygame.quit()
                quit()

            
            if not fin and choix==3:
                screen.blit(commencer_bouton, commencer_bouton_rect)

        pygame.display.update()

while True:
    play()



