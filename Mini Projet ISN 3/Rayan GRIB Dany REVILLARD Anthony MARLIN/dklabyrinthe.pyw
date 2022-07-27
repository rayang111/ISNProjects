#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
Jeu Donkey Kong Labyrinthe
Jeu dans lequel on doit déplacer DK jusqu'aux bananes à travers un labyrinthe.

Script Python
Fichiers : dklabyrinthe.py, classes.py, constantes.py, n1, n2 + images
"""

import pygame
from pygame.locals import *

from classes import *
from constantes import *
import time
import datetime
import os

pygame.init()

#Ouverture de la fenêtre Pygame (carré : largeur = hauteur)
fenetre = pygame.display.set_mode((cote_fenetre, cote_fenetre))
#Icone
icone = pygame.image.load(image_icone)
pygame.display.set_icon(icone)
#Titre
pygame.display.set_caption(titre_fenetre)


#BOUCLE PRINCIPALE
continuer = 1
while continuer:
  #Chargement et affichage de l'écran d'accueil
  accueil = pygame.image.load(image_accueil).convert()
  pygame.mixer.music.load(musique_menu)
  pygame.mixer.music.play(loops=10^999)
  quitterimg = pygame.image.load(quitter_img).convert()
  MSTTI = pygame.image.load(image_ms).convert_alpha()
  niveau1d = pygame.image.load(niveau1_img).convert()
  niveau2d = pygame.image.load(niveau2_img).convert()
  niveau3d = pygame.image.load(niveau3_img).convert()
  niveau4d = pygame.image.load(niveau4_img).convert()
  niveau5d = pygame.image.load(niveau5_img).convert()  
  fenetre.blit(accueil, (0,0))
    #Ouverture du fichier meilleurs scores
  ms = open("ms", "r+")
  MST = ms.read().split()
  MSTL = [int(i) for i in MST]
  MSTL.sort()
  font=pygame.font.Font(None, 24)
  try:
    MSTTT = font.render("1 : {0} points".format(MSTL[-1]),1,(255,255,255))
  except IndexError:
    pass
  try:
    MSTTTS = font.render("1 : {0} points".format(MSTL[-1]),True,pygame.Color('black'))
  except IndexError:
    pass
  try:
    MSTTT1 = font.render("2 : {0} points".format(MSTL[-2]),1,(255,255,255))
  except IndexError:
    pass
  try:
    MSTTTS1 = font.render("2 : {0} points".format(MSTL[-2]),True,pygame.Color('black'))
  except IndexError:
    pass
  try:
    MSTTT2 = font.render("3 : {0} points".format(MSTL[-3]),1,(255,255,255))
  except IndexError:
    pass
  try:
    MSTTTS2 = font.render("3 : {0} points".format(MSTL[-3]),True,pygame.Color('black'))
  except IndexError:
    pass
  #Rafraichissement
  pygame.display.flip()

  #On remet ces variables à 1 à chaque tour de boucle
  continuer_jeu = 1
  continuer_accueil = 1

  #BOUCLE D'ACCUEIL
  while continuer_accueil:
  
    #Limitation de vitesse de la boucle
    pygame.time.Clock().tick(30)
  
    for event in pygame.event.get():
    
      #Si l'utilisateur quitte, on met les variables 
      #de boucle à 0 pour n'en parcourir aucune et fermer
      if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
        continuer_accueil = 0
        continuer_jeu = 0
        continuer = 0
        #Variable de choix du niveau
        choix = 0
        pygame.mixer.music.stop()
        fenetre.blit(quitterimg,(0,0))
        font2=pygame.font.Font(None, 45)
        textquit = font2.render('Fermeture du jeu...', True, pygame.Color('gray'))
        fenetre.blit(textquit, (90,200))
        pygame.display.flip()
        time.sleep(2)
        pygame.quit()
        print("\nDK LABYRINTHE ENHANCED\n version 1.0\n")
        
        
      elif event.type == KEYDOWN:       
        #Lancement du niveau 1
        if event.key == K_F1:
          pygame.mixer.music.stop()
          fenetre.blit(niveau1d,(0,0))
          pygame.display.flip()
          time.sleep(2)
          continuer_accueil = 0 #On quitte l'accueil
          choix = 'n1'#On définit le niveau à charger
          P = 0
          TP = 0
          ms.truncate()
          
        #Lancement du niveau 2
        elif event.key == K_F2:
          pygame.mixer.music.stop()
          fenetre.blit(niveau2d,(0,0))
          pygame.display.flip()
          time.sleep(2)
          continuer_accueil = 0
          choix = 'n2'
          P = 0
          ms.truncate()

        #Lancement du niveau 3
        elif event.key == K_F3:
          pygame.mixer.music.stop()
          fenetre.blit(niveau3d,(0,0))
          pygame.display.flip()
          time.sleep(2)
          continuer_accueil = 0
          choix = 'n3'
          P = 0
          ms.truncate()

        #Lancement du niveau 4
        elif event.key == K_F4:
          pygame.mixer.music.stop()
          fenetre.blit(niveau4d,(0,0))
          pygame.display.flip()
          time.sleep(2)
          continuer_accueil = 0
          choix = 'n4'
          P = 0
          ms.truncate()

        #Lancement du niveau 5
        elif event.key == K_F5:
          pygame.mixer.music.stop()
          fenetre.blit(niveau5d,(0,0))
          pygame.display.flip()
          time.sleep(2)
          continuer_accueil = 0
          choix = 'n5'
          P = 0
          ms.truncate()
          
        #Affichage des meilleurs scores
        elif event.key == K_m:
          fenetre.blit(MSTTI, (0,0))
          try:
            fenetre.blit(MSTTTS, (102, 178))
          except NameError:
            aucun_scoreS = font.render("Il y a aucun score...",True,pygame.Color('black'))
            fenetre.blit(aucun_scoreS, (102,178))
          try:
            fenetre.blit(MSTTT, (100,175))
          except NameError:
            aucun_score = font.render("Il y a aucun score...",1,(255,255,255))
            fenetre.blit(aucun_score, (100,175))
          try:
            fenetre.blit(MSTTTS1, (102, 203))
          except NameError:
            pass
          try:
            fenetre.blit(MSTTT1, (100,200))
          except NameError:
            pass
          try:
            fenetre.blit(MSTTTS2, (102, 228))
          except NameError:
            pass
          try:
            fenetre.blit(MSTTT2, (100,225))
          except NameError:
            pass
          pygame.display.flip()
          time.sleep(4)
          fenetre.blit(accueil, (0,0))
          pygame.display.flip()


    
    

  #on vérifie que le joueur a bien fait un choix de niveau
  #pour ne pas charger s'il quitte
  if choix != 0:
    #Chargement du fond
    if choix == 'n1':
      fond = pygame.image.load(image_fond1).convert()
    if choix == 'n2':
      fond = pygame.image.load(image_fond2).convert()
    if choix == 'n3':
      fond = pygame.image.load(image_fond3).convert()
    if choix == 'n4':
      fond = pygame.image.load(image_fond4).convert()
    if choix == 'n5':
      fond = pygame.image.load(image_fond5).convert()
      

    #Génération d'un niveau à partir d'un fichier
    niveau = Niveau(choix)
    choixperso = pygame.image.load(image_choixperso).convert()
    choixpersot = 1
      #Demmende au joueur son choix de personnage
    while choixpersot:
      fenetre.blit(choixperso, (0,0))
      pygame.display.flip()
      for event in pygame.event.get():
        if event.type == KEYDOWN:
          if event.key == K_d:
            choixdk = Perso("images/dk_droite.png", "images/dk_gauche.png", 
            "images/dk_haut.png", "images/dk_bas.png", niveau)
            choixpersot = 0
          elif event.key == K_o:
            choixdk = Perso("images/Orque_droite.png", "images/Orque_gauche.png", "images/Orque_Avant.png",
            "images/Orque_bas.png", niveau)
            choixpersot = 0
          elif event.key == K_g:
            choixdk = Perso("images/Golden_Skeleton_droite.png", "images/Golden_Skeleton_gauche.png", "images/Golden_Skeleton_haut.png",
            "images/Golden_Skeleton_bas.png", niveau)
            choixpersot = 0
          elif event.key == K_v:
            choixdk = Perso("images/Voleuse_droite.png", "images/Voleuse_gauche.png", "images/Voleuse_haut.png",
            "images/Voleuse_bas.png", niveau)
            choixpersot = 0
          
    niveau.generer()
    niveau.afficher(fenetre)
    #Création de la variable permetant de savoir le temps système, utile pour le calcul du temps écoulé et donc aussi pour celui du temps restant
    S = datetime.datetime.now()
    #Capture du temps à cette instant pour pouvoir soutraire le temps système par cette valeur
    T=S.second
    #On définit le temps dans le quel le niveau doit être réussi
    if choix == 'n1':
      CT = 55
    if choix == 'n2':
      CT = 50
    if choix == 'n3':
      CT = 45
    if choix == 'n4':
      CT = 40
    if choix == 'n5':
      CT = 40

    #Création de Donkey Kong ou autre personnage choisi
    dk = choixdk
    
    #Lancement de la musique du jeu
    pygame.mixer.music.load(musique_jeu)
    pygame.mixer.music.play(loops=10^99)
    #Initialisation du score
    score = 0
    #Initialisation de la variable permetant l'effet 'critique' du temps restant lorsqu'il est en dessous de 10 secondes
    TRS = 1

    M = 0
    TRR = 0
    


        
  #BOUCLE DE JEU
  while continuer_jeu:
    #Limitation de vitesse de la boucle
    pygame.time.Clock().tick(30)

    perduson = pygame.mixer.Sound(son_perdu)
    victson = pygame.mixer.Sound(son_victoire)
    coinS = pygame.mixer.Sound(son_piece)
    mvt = pygame.mixer.Sound(son_mouv)
    tempscritique = pygame.mixer.Sound(son_tempscritique)
    perdu1 = pygame.image.load(perdu_img).convert()
    victoireimg = pygame.image.load(victoire_img).convert()
    S1=datetime.datetime.now()
    #Calcul du temps écoulé
    TR = S1.second-(T)
    if S1.second == 59:
      TB = TR
    if TR < 0:
      TRR = TR
      TR = TR-TR+TB+S1.second
      M = 1
    if TRR < 0 and M == 1:
      TR = TR-TR+TB+S1.second      

    #Calcul du temps restant
    if choix == 'n1':
      TT = CT - TR
    if choix == 'n2':
      TT = CT - TR
    if choix == 'n3':
      TT = CT - TR
    if choix == 'n4':
      TT = CT - TR
    if choix == 'n5':
      TT = CT - TR
    font=pygame.font.Font(None, 24)
    fonts=pygame.font.Font(None, 32)
    texte = font.render("Temps restant : {0}".format(TT),1,(255,255,255))
    tshadow = font.render("Temps restant : {0}".format(TT),True,pygame.Color('black'))
    texte1 = font.render("Temps écoulé : {0}".format(TR),1,(255,255,255))
    tshadow1 = font.render("Temps écoulé : {0}".format(TR),True,pygame.Color('black'))
    texteS = font.render("Score : {0}".format(score),1,(255,255,255))
    tshadowS = font.render("Score : {0}".format(score),True,pygame.Color('black'))
    plusscoreT = fonts.render("+20",True,pygame.Color('white'))
    plusscoreTS = fonts.render("+20",True,pygame.Color('green'))

    #Si le joueur a perdu -> message perdu -> retour à l'acceuil 
    if TR == CT :
      pygame.mixer.music.stop()
      perduson.play()
      mvt.stop()
      fenetre.blit(perdu1, (0,0))
      pygame.display.flip()
      time.sleep(2)
      perduson.stop()
      continuer_jeu = 0

    #Effet critique du temps restant dès qu'il reste moins de 10 secondes
    if TT <= 10:
      if int(((TR)/2))*2 != TR :
        texte = font.render("Temps restant : {0}".format(TT),True,pygame.Color('red'))
        tshadow = font.render("Temps restant : {0}".format(TT),True,pygame.Color('white'))
        pygame.display.flip()
        while TRS:
          tempscritique.play()
          TRS = 0        
      else:
        texte = font.render("Temps restant : {0}".format(TT),True,pygame.Color('white'))
        tshadow = font.render("Temps restant : {0}".format(TT),True,pygame.Color('black'))
        pygame.display.flip()
        tempscritique.stop()
        TRS = 1
      if TT == 0:
        TRS = 1
        tempscritique.stop()
        

      
              
    for event in pygame.event.get():
         
      #Si l'utilisateur quitte, on met la variable qui continue le jeu
      #ET la variable générale à 0 pour fermer la fenêtre
      if event.type == QUIT:
        pygame.mixer.music.stop()
        continuer_jeu = 0
        continuer = 0
      
      elif event.type == KEYDOWN:
        #Si l'utilisateur presse Echap ici, on revient seulement au menu
        if event.key == K_ESCAPE:
          pygame.mixer.music.stop()
          continuer_jeu = 0
          
        #Touches de déplacement de Donkey Kong
        elif event.key == K_RIGHT:
          dk.deplacer('droite')
          mvt.play()
        elif event.key == K_LEFT:
          dk.deplacer('gauche')
          mvt.play()
        elif event.key == K_UP:
          dk.deplacer('haut')
          mvt.play()
        elif event.key == K_DOWN:
          dk.deplacer('bas')
          mvt.play()

          
    #Affichages aux nouvelles positions       

    fenetre.blit(fond, (0,0))
    niveau.afficher(fenetre)  
    fenetre.blit(dk.direction, (dk.x, dk.y)) #dk.direction = l'image dans la bonne direction
    fenetre.blit(tshadow1, (302, 202))  
    fenetre.blit(texte1, (300, 200))
    fenetre.blit(tshadow, (302, 302))  
    fenetre.blit(texte, (300, 300))
    fenetre.blit(tshadowS, (12,302))
    fenetre.blit(texteS, (10,300))
    pygame.display.flip()
    
    #Si le joueur récupère une pièce    
    if niveau.structure[dk.case_y][dk.case_x] == 'p':
      coinS.play()
      score += 20
      niveau.structure[dk.case_y][dk.case_x] = '0'
      fenetre.blit(plusscoreTS, (dk.x+2,dk.y+2))
      fenetre.blit(plusscoreT, (dk.x,dk.y))
      pygame.display.flip()
      
    #Victoire -> Retour à l'accueil
    if niveau.structure[dk.case_y][dk.case_x] == 'a':
      pygame.mixer.music.stop()
      victson.play()
      if choix == 'n1':
        if TT >= 25:
          score += 100
        elif 25 > TT >= 15:
          score += 50
        elif 15 > TT >= 10:
          score += 25
        elif 10 > TT >= 7:
          score += 5
        elif 7 > TT >= 4:
          score += 2
        elif 4 > TT >= 1:
          score += 1
      if choix == 'n2':
        if TT >= 15:
          score += 100
        elif 15 > TT >= 12:
          score += 50
        elif 12 > TT >= 10:
          score += 25
        elif 10 > TT >= 7:
          score += 5
        elif 7 > TT >= 4:
          score += 2
        elif 4 > TT >= 1:
          score += 1
      if choix == 'n3':
        if TT >= 15:
          score += 100
        elif 15 > TT >= 12:
          score += 50
        elif 12 > TT >= 10:
          score += 25
        elif 10 > TT >= 7:
          score += 5
        elif 7 > TT >= 4:
          score += 2
        elif 4 > TT >= 1:
          score += 1
      if choix == 'n4':
        if TT >= 15:
          score += 100
        elif 15 > TT >= 12:
          score += 50
        elif 12 > TT >= 10:
          score += 25
        elif 10 > TT >= 7:
          score += 5
        elif 7 > TT >= 4:
          score += 2
        elif 4 > TT >= 1:
          score += 1
      if choix == 'n5':
        if TT >= 15:
          score += 100
        elif 15 > TT >= 12:
          score += 50
        elif 12 > TT >= 10:
          score += 25
        elif 10 > TT >= 7:
          score += 5
        elif 7 > TT >= 4:
          score += 2
        elif 4 > TT >= 1:
          score += 1        
      mvt.stop()
      victoirescore = font.render("Votre score final : {0}  points !".format(score),1,(255,255,255))
      victoirescore0 = font.render("Votre score final : {0}  points ...".format(score),1,(255,255,255))
      meilleurscoretxt = font.render("MEILLEUR SCORE !!!".format(score),True,pygame.Color('orange'))
      fenetre.blit(victoireimg,(0,0))
      if score > 5:
        fenetre.blit(victoirescore, (100,100))
      else:
        fenetre.blit(victoirescore0, (100,100))
      try:
        if score > MSTL[-1]:
          fenetre.blit(meilleurscoretxt, (140,250))
      except IndexError:
        pass
      pygame.display.flip()
      score = int(score)
      msl = ms.write("{0} \n".format(score))
      int(msl)
      time.sleep(2)
      continuer_jeu = 0
