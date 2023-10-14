############################################
from random import *
from Modele import *
from Jeu import *
import pygame
import random
import time
from pygame import mixer
#import des différents modules utilisés (dont les fichiers contenat certaines fonctions très utiles)
############################################


############################################
width=1280
height=720
black= (0,0,0)
white= (255,255,255)
light_green=(0,120,0)
red=(255,0,0)
pygame.init()
#définition des variables de base les plus importante (couleurs, dimensions de la fenêtre...)
############################################


############################################
screen = pygame.display.set_mode((width,height))
screen.fill(black)

pygame.display.set_caption("BlackJack")
pygame.display.set_icon(pygame.image.load("logo.png"))
#initialisation de l'icone, du nom du jeu, aisni que de l'écran de base
############################################

############################################
#Fonction qui basiquement, fait fonctionner tout le jeu (sera éxécuté indéfiniment plus tard)
def play():
    ################################################################################################################################################################################
    #Longue définition des différentes variable utilisé dans jeu
    game=jeu() #initialisation d'une classe jeu qui servira tout au long du code
    ############################################
    small_font = pygame.font.Font(None,32)
    large_font = pygame.font.Font(None,50)
    title_font = pygame.font.Font(None, 70)
    #Définition des différentes polices de texte
    ############################################
    ############################################
    pygame.mixer.init()
    bg=mixer.Sound("background2.wav")
    draw=mixer.Sound("card_draw0.wav")
    victory=mixer.Sound("VICTORY.wav")
    #Définition des differents sons à l'aide de mixer
    ############################################
    ############################################
    pioche_bouton = large_font.render("TIRER", True, white, black) 
    passe_bouton = large_font.render("RESTER", True, white, black)
    commencer_bouton=title_font.render("CLIQUEZ MOI POUR COMMENCER", True, white)
    perdu_bouton=title_font.render("VOUS AVEZ PERDU", True, white, black)
    gagne_bouton=title_font.render("VOUS AVEZ GAGNÉ", True, white, black)
    egalite_bouton=title_font.render("C'EST UNE ÉGALITÉ", True, white, black)
    recommencer_bouton=large_font.render("RECOMMENCER", True, white, black)
    quitter_bouton=large_font.render("QUITTER", True, white, black)
    #Initialisation de tout ce qui servira à faire fonctionner les différents boutons (texte, couleur, couleur fond..)
    ############################################
    pioche_bouton_rect=pioche_bouton.get_rect()
    passe_bouton_rect=passe_bouton.get_rect()
    commencer_bouton_rect=commencer_bouton.get_rect()
    perdu_bouton_rect=perdu_bouton.get_rect()
    gagne_bouton_rect=gagne_bouton.get_rect()
    egalite_bouton_rect=egalite_bouton.get_rect()
    recommencer_bouton_rect=recommencer_bouton.get_rect()
    quitter_bouton_rect=quitter_bouton.get_rect()
    #rectangles qui serviront à placer les boutons
    ############################################
    pioche_bouton_rect.center=(450,620)
    passe_bouton_rect.center=(830,620)
    commencer_bouton_rect.center=(640,360)
    quitter_bouton_rect.center=(420,620)
    recommencer_bouton_rect.center=(830,620)
    perdu_bouton_rect.center=(640,360)
    gagne_bouton_rect.center=(640,360)
    egalite_bouton_rect.center=(640,360)
    #Définition des cordoonnées de placement des boutons
    ############################################
    ############################################
    def do_main():
        game.distribution()
        j = game.joueur.calculer_main(game.joueur.main_joueur)
        c = game.croupier.calculer_main(game.croupier.main_joueur)
        return j,c
    #Fonction qui servira à initialiser une main aléatoire de base pour le joueur et le croupier (utilisant les classes des fichiers controle et jeu)
    ############################################
    ############################################
    resultat="" 
    main,main_croupier = do_main()
    choix= 3 #Variable ESSENTIELLE: sert à faire fonctionner chaque choix lors des différents clics.
    fin = False 
    #Variables utiles (main du joueur et du croupier, et variable de fin)
    ############################################
    ############################################
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
    #Initialisation visuelle des première cartes de la main du joueur et du croupier
    ############################################
    ############################################
    l=[i for i in range(-100,-1)]
    l2=[i for i in range(0,101)]
    #définition de simples liste utiles pour plus tard contenant respectivement les nombre de -100 à -1 et de 0 à 101
    ################################################################################################################################################################################



    ################################################################################################################################################################################
    #Moment où le jeu démarre réllement, toutes les actions se feront ici à l'aide de tout ce qui a pu etre défini.
    while True:       
        mouse=pygame.mouse.get_pos()#obtention d'une variable souris qui est une liste avec les cordoonées du clic x et y
        ############################################
        for event in pygame.event.get(): #boucle gérant les différents évènements (ici en fait les clics du joueur)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        #simple event de quittage si le joueur souhaite fermer le jeu de lui même
        ############################################
################################################################################################################################################################################
            if not fin and event.type == pygame.MOUSEBUTTONDOWN:
                if 760 <= mouse[0] <= 900 and 600 <= mouse[1] <= 640 and choix in [-1, -2, -3]: #test pour savoir si le joueur se couche
                    choix = 1
                    
                if 370 <= mouse[0] <= 530 and 600 <= mouse[1] <= 640 and choix not in l: #test du premier tirage
                    choix = 0

                if 370 <= mouse[0] <= 530 and 600 <= mouse[1] <= 640 and choix==-2: #test du deuxieme tirage
                    choix = 4

                if 370 <= mouse[0] <= 530 and 600 <= mouse[1] <= 640 and choix==-3: #test du troisieme tirage
                    choix = 5
                    
                if 0<=mouse[0]<=1280 and 0<=mouse[1]<=720: #Lancement du jeu (choix initialiement mit à 3 pour cela)
                    if choix == 3:
                        choix=2 #on renvoit au choix 2 (voir plus bas pour comprendre)

                if 690 <= mouse[0] <= 965 and 600 <= mouse[1] <= 640 and choix==-100: #test du recommencement
                    choix = 12
                    
                if 340 <= mouse[0] <= 490 and 600 <= mouse[1] <= 640 and choix==-100: #test pour quitter
                    choix = 404
#Tous les différents évènement liés aux clics (en fait, chaque clic change la valeur de la variable "choix" pour qu'ensuite, une action soit éffectuée
#De la même manière, chaque événement de clic est testé selon la valeur de choix pour permettre de reconnaître les différentes actions
################################################################################################################################################################################                   
            if choix==2: #initiation du jeu quand on clique pour commencer
                screen.fill(light_green) #on rempli l'écran de vert clair
                screen.blit(pygame.image.load("Background.png").convert(), [0,0]) #on fait apparait le fond qu'on charge directement dans le dossier
                screen.blit(pioche_bouton, pioche_bouton_rect) #on fait apparaitre le bouton pour tirer
                screen.blit(passe_bouton, passe_bouton_rect) #on fait apparaitre le bouton pour rester
                screen.blit(imagemain0, imagemain0_rect) #on fait apparaître la premiere carte de la main du joueur
                screen.blit(imagemain1, imagemain1_rect) #on fait apparaître la deuxieme carte de la main du joueur
                valeur=large_font.render("Valeur de votre main: "+str(main), True, white, red) #on initialise le compteur de la main
                valeur_rect=valeur.get_rect()
                valeur_rect.center=(640,560) #position du compteur
                screen.blit(valeur, valeur_rect)# on l'affiche
                backcard_rect=(520,50) 
                screen.blit(backcard,backcard_rect) #on fait apparaitre la seconde carte du croupier, face cachée.
                screen.blit(imagemaincroupier0, imagemaincroupier0_rect) # on fait apparaitre la premiere carte du croupier, face révélée.
                bg.play(-1)#on joue la musique de fond indéfiniment (enfin jusqu'à ce qu'on perde ou gagne)
                choix=-1 # on initie le choix à -1 pour permettre de choisir quel type d'évènement arrivera par la suite
                    
################################################################################################################################################################################
################################################################################################################################################################################                    
            if choix==0: #PREMIER TIRAGE (variable donc mise à 0)
                game.tirer("j") #on tire une carte pour le joueur grace à la classe jeu
                main=game.joueur.calculer_main(game.joueur.main_joueur) # on recalcule la main pour actualiser la valeur affichée
                imagemain0=game.joueur.main_joueur[2].image # on rédefini une variable avec l'image de la nouvelle carte tirée
                imagemain0_rect.center=(640,470) # on positionne la carte au bon emplacement
                screen.blit(imagemain0, imagemain0_rect) # on affiche la carte (la fonction .blit servira toujours à afficher un élément visuellement)
                valeur=large_font.render("Valeur de votre main: "+str(main), True, white, red) #on redéfini la valeur de la main avec la nouvelle valeur
                valeur_rect=valeur.get_rect() 
                valeur_rect.center=(640,560) #on change la position
                screen.blit(valeur, valeur_rect) #ré-affichage de la valeure de la main
                draw.play(0) # on lance le bruit du tirage d'une carte initialisé plus tôt
                pygame.display.update()# on actualise l'écran ici pour pouvoir pauser le programme une fois que les cartes sont affichées
                pygame.time.wait(2000) # fonction servant à pauser le programme 2000 millisecondes (peut créer des lags mais le choix a été fait parce que le jeu est beaucoup
                                       # plus clair avec ces pauses éffectuées
                ############################################
                if main==21:
                    choix=14
                else:
                    if main==main_croupier:
                        choix=13
                    if main<=21:
                        choix = -2
                    else:
                        choix = 10
                #Série de test définissant si létat du jeu est une victoire du joueur, une défaite, une égalité ou bien un BlackJack
                ############################################
#L'explication de ce tirage est la même pour chaque tirage, je ne la ré-écrirait donc pas pour chaque tirage mais ce sont les mêmes choses avec quelques différences
################################################################################################################################################################################     
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
#deuxième tirage aux mêmes explications que le premier
################################################################################################################################################################################                
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
#troisième tirage aux mêmes explications que le premier et le deuxième.
################################################################################################################################################################################
################################################################################################################################################################################
            if choix ==1: #le joueur a décidé de rester
                screen.blit(imagemaincroupier1, imagemaincroupier1_rect) # on affiche la carte face cachée du croupier
                draw.play(0)# bruit du tirage d'une carte
                pygame.display.update() # on actualise pour pauser le code
                time.sleep(2) # on pause le code
                if main_croupier<17 and main_croupier<=main: #test pour savoir si le croupier doit tirer une carte (il tire si sa main est inférieure à 17 et inférieure à la main du joueur)
                    game.tirer("c") #il doit tirer, on tire donc une carte pour le croupier
                    main_croupier=game.croupier.calculer_main(game.croupier.main_joueur)#on recalcule la main du croupier
                    imagecroupier2=game.croupier.main_joueur[2].image #on défini l'image de la carte tirée
                    imagecroupier2_rect=imagecroupier2.get_rect()
                    imagecroupier2_rect.center=(641,100) #on la positionne
                    screen.blit(imagecroupier2,imagecroupier2_rect) # on l'affiche
                    draw.play(0) # bruit du tirage d'une carte
                    #Les explications se répètent donc plusieurs fois de la même façon pour chaque cas possible, je ne les détaillerais donc pas étant très fortement similaires
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
                pygame.display.update()#on actualise l'écran
                pygame.time.wait(3000)#on pause 3 secondes le temps que le joueur comprenne ce qui se passe à l'écran
                ############################################
                if main == 21:
                    choix=14
                else:
                    if main==main_croupier:
                        choix=13
                    if main<main_croupier and main_croupier<=21:
                        choix=10
                    else:
                        choix=11
                #Série de test définissant si létat du jeu est une victoire du joueur, une défaite, une égalité ou bien un BlackJack
                ############################################
################################################################################################################################################################################                
            if choix==10: # le joueur a perdu
                bg.stop() # on arrête la musique de fond
                screen.fill(black) # on rempli l'écran de la couleur noire
                screen.blit(perdu_bouton, perdu_bouton_rect) # on affiche "vous avez perdu"
                screen.blit(recommencer_bouton, recommencer_bouton_rect) # on affiche le bouton pour recommencer
                screen.blit(quitter_bouton, quitter_bouton_rect) #on affiche le bouton pour quitter
                choix = -100 #on met le choix à -100 pour que le programme comprenne qu'il s'agit du choix pour recommencer ou quitter et non un autre

            if choix==11: # le joueur a gagné
                bg.stop() # on arrête la musique de fond
                screen.fill(black) # on rempli l'écran de la couleur noire
                screen.blit(gagne_bouton, gagne_bouton_rect) # on affiche "vous avez gagné"
                screen.blit(recommencer_bouton, recommencer_bouton_rect) # on affiche le bouton pour recommencer
                screen.blit(quitter_bouton, quitter_bouton_rect) #on affiche le bouton pour quitter
                choix = -100 #on met le choix à -100 pour que le programme comprenne qu'il s'agit du choix pour recommencer ou quitter et non un autre
                
            if choix==13:
                bg.stop() # on arrête la musique de fond
                screen.fill(black) # on rempli l'écran de la couleur noire
                screen.blit(egalite_bouton, egalite_bouton_rect) # on affiche "égalité"
                screen.blit(recommencer_bouton, recommencer_bouton_rect) # on affiche le bouton pour recommencer
                screen.blit(quitter_bouton, quitter_bouton_rect) #on affiche le bouton pour quitter
                choix = -100 #on met le choix à -100 pour que le programme comprenne qu'il s'agit du choix pour recommencer ou quitter et non un autre

            if choix==14:
                bg.stop() # on arrête la musique de fond
                victory.play(0) # on lance la musique de victoire
                screen.blit(pygame.image.load("Blackjackscreen.png"), [0,0]) # on charge et fait apparaître le fond d'écran dédiacé au moment ou le joueur obtient un Blackjack
                screen.blit(recommencer_bouton, recommencer_bouton_rect) # on affiche le bouton pour recommencer
                screen.blit(quitter_bouton, quitter_bouton_rect) #on affiche le bouton pour quitter
                choix = -100 #on met le choix à -100 pour que le programme comprenne qu'il s'agit du choix pour recommencer ou quitter et non un autre
################################################################################################################################################################################                  
            if choix==12: #le joueur a choisi de recommencer
                victory.stop() # on arrête la musique de victoire
                screen.fill(black) #on rempli l'écran de noir
                return None #et ce return nous permet de sortir de la fonction en cours (c'est à dire la fonction play()) ce qui nous permet de relancer la boucle
            
            if choix==404: #le joueur à choisi de quitter
                pygame.quit() #on quitte le jeu
                quit()

            
            if not fin and choix==3: #tout premier écran, la où le joueur clique pour commencer l'intialisation du jeu
                screen.blit(commencer_bouton, commencer_bouton_rect)

        pygame.display.update() #ligne TRES importante étant donné que l'actualisation de ce qu'on voit se fait grâce à cette ligne indéfiniment (chaque élément à besoin d'être mis à jour pour s'afficher.)

################################################################################################################################################################################
while True:
    play()
#Boucle qui va permettre au jeu de se répéter indéfiniment, nottament lorsque
#on souhaitera recommencer une partie, on sera renvoyé ici pour tout réinitialiser
############################################

