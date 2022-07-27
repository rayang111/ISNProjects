#!/usr/bin/env python
# -*- coding: utf-8 -*-

############################################################################################################################
#                                                                                                                          #GRIB Rayan
#                                           Space Invaders BAC - 16/05/2019                                                #REVILLARD Dany
#                                                                                                                          #MARLIN Anthony
############################################################################################################################

import pygame,sys
from pygame.locals import *
import random
import os
from constantes import *
############################################################################################################################
def fade(width, height):
    fade = pygame.Surface((width, height))
    fade.fill((0,0,0))
    for alpha in range(0, 50):
        fade.set_alpha(alpha)
        screen.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(5)

class Player(pygame.sprite.Sprite):
        def __init__(self, xpos, ypos, filename):
                pygame.sprite.Sprite.__init__(self)
                self.x = xpos
                self.y = ypos
                self.image = pygame.image.load(filename).convert_alpha()
                self.rect = self.image.get_rect()
                self.rect.centerx = (900/2)
                self.rect.bottom = (600 - 10)
                self.speedx = 0
        def update(self):
                self.speedx = 0
                keystate = pygame.key.get_pressed()
                if keystate[pygame.K_LEFT]:
                        self.speedx -= 10
                if keystate[pygame.K_RIGHT]:
                        self.speedx += 10
                self.rect.x += self.speedx
                if self.rect.right > 900:
                        self.rect.right = 900
                if self.rect.left < 0:
                        self.rect.left = 0
        def shoot(self, filename2):
                global ourmissile3 
                ourmissile3 = Bullet(self.rect.centerx, self.rect.top, filename2)
                all_sprites.add(ourmissile3)
                bullet.add(ourmissile3)

class Sprite(pygame.sprite.Sprite):
        def __init__(self, xpos, ypos, filename):
                pygame.sprite.Sprite.__init__(self)
                self.x = xpos
                self.y = ypos
                self.image = pygame.Surface((50, 40))
                self.image = pygame.image.load(filename).convert_alpha()
                self.image.set_colorkey((0,0,0))
                self.rect = self.image.get_rect()
                self.rect.center = (xpos, ypos)
        def set_position(self, xpos, ypos):
                self.x = xpos
                self.y = ypos
        def render(self):
                screen.blit(self.image, (self.x, self.y))

class Enemy(pygame.sprite.Sprite):
        def __init__(self, xpos, ypos, filename):
                pygame.sprite.Sprite.__init__(self)
                self.x = xpos
                self.y = ypos
                self.image = pygame.image.load(filename).convert_alpha()
                self.rect = self.image.get_rect()
                self.rect.center = (900/2, 600/2)
                self.rect.x = random.randrange(900 - self.rect.width)
                self.rect.y = random.randrange(-90,-40)
                self.speedy = random.randrange(1,5)
                self.speedx = random.randrange(-3,2)
        def update(self):
                self.rect.x += self.speedx
                self.rect.y += self.speedy
                if self.rect.top > 600 + 10 or self.rect.left < -25 or self.rect.right > 900 + 20:
                        self.rect.x = random.randrange(900 - self.rect.width)
                        self.rect.y = random.randrange(-90,-40)
                        self.speedy = random.randrange(1, 5)
                        
        def set_position(self, xpos, ypos):
                self.x = xpos
                self.y = ypos
        def render(self):
                screen.blit(self.image, (self.x, self.y))

class Bullet(pygame.sprite.Sprite):
        def __init__(self, x, y, filename):
                pygame.sprite.Sprite.__init__(self)
                self.image = pygame.image.load(filename).convert_alpha()
                self.rect = self.image.get_rect()
                self.rect.bottom = y
                self.rect.centerx = x
                self.speedy = -10
        def update(self):
                self.rect.y += self.speedy
                if self.rect.bottom < 0:
                        self.kill()
        def set_position(self, xpos, ypos):
                self.x = xpos
                self.y = ypos
        def render(self):
                screen.blit(self.image, (self.x, self.y))
                

def Intersect(s1_x, s1_y, s2_x, s2_y):
        if (s1_x > s2_x ) and (s1_x < s2_x + 50) and (s1_y > s2_y - 50) and (s1_y < s2_y ):
                return 1
        else:
                return 0

def Intersect2(s1_x, s1_y, s2_x, s2_y):
        if (s1_x > s2_x ) and (s1_x < s2_x + 50) and (s1_y > s2_y - 50) and (s1_y < s2_y ):
                return 1
        else:
                return 0

def IntersectE(s1_x, s1_y, s2_x, s2_y):
        if (s1_x > s2_x - 50) and (s1_x < s2_x + 50) and (s1_y > s2_y - 50) and (s1_y < s2_y + 50):
                return 1
        else:
                return 0
        
def IntersectB(s1_x, s1_y, s2_x, s2_y):
        if (s1_x > s2_x - 50) and (s1_x < s2_x + 50) and (s1_y > s2_y - 50) and (s1_y < s2_y + 50):
                return 1
        else:
                return 0

def pause():
        startc.play()
        pause = True
        fade(900,600)
        global quitteres, Logo
        while pause:
                for event in pygame.event.get():
                        if event.type == KEYDOWN:
                                if event.key == K_r:
                                        fade(900,600)
                                        pause = False
                                if event.key == K_a:
                                        fade(900,600)
                                        pause = False
                                        quitteres = 1
                        if event.type == QUIT:
                                quitter = 1
                                pygame.quit()
                                sys.exit()

                backdrop2 = pygame.image.load('new-BG.bmp')
                Logo2 = pygame.image.load('SIB2.png')
                TextPause = Texty.render('JEU EN PAUSE', 0, (255,255,0))
                TextPauseQ = Texty5.render('Q : Quitter', 0, (255,255,0))
                TextPauseR = Texty5.render('R : Reprendre', 0, (255,255,0))
                text9=Texty5.render('Déplacez vous avec les touches \'droite\' et \'gauche\', tirez avec la touche \'espace\'', 0, (150,150,255))
                text10=Texty5.render('Protégez vos copies, et vous même !', 0, (100,100,100))
                Logo2 = pygame.transform.scale(Logo2, (187, 62))
                screen.blit(backdrop2, (0, 0))
                screen.blit(Logo2, (365,57))
                screen.blit(TextPause, (150,150))
                screen.blit(TextPauseQ, (150,275))
                screen.blit(TextPauseR, (600,275))
                screen.blit(text9, (25,500))
                screen.blit(text10, (250,350))

                pygame.display.update()
                mainclock.tick(15)

def perdu():
        "Si héros touché alors :"
        global enemies, enemies2, text, quitter, game, ns, enemy, aliens
        aliens.empty()
        text = Texty2.render('RECALÉ', 0, (255,0,0))
        textd = Texty3.render('A l\'année prochaine...', 0, (255,0,0))
        screen.blit(text, (200,150))
        screen.blit(textd, (225,350))
        gameover.play()
        pygame.display.update()
        pygame.time.delay(1000)
        pygame.time.delay(500)
        del text
        quitter=1
        pygame.mixer.music.stop()
        ns = 1
        enemy.empty()
        fade(900,600)
        nn = 0
        game = False
        pygame.mixer.music.load("01.wav")
        pygame.mixer.music.play(loops=10^99)
        
        
    


def win():
        "Si plus d'ennemis alors :"
        global enemies, enemies2, quitter, game, ns, enemy, aliens, score, ms, nn, nn1, nn2, nn3, nn4, nn5, nn6, choix, timeer, scorefinal
        aliens.empty()
        textx = Texty2.render('ADMIS !', 0, (0,255,0))
        scorefin = score + timeer + (len(bouclier1) + len(bouclier2) + len(bouclier3)*3)
        scorefinal.append(scorefin)
        if choix != 4:
            scoretext = Texty3.render('Votre score : {0}'.format(scorefin), 0, (255,255,255))
        elif choix == 4:
            scoretext = Texty3.render('Votre score : {0}'.format(scorefin), 0, (100,100,100))
        screen.blit(textx, (200,150))
        screen.blit(scoretext, (200,350))
        wins.play()
        pygame.display.update()
        pygame.time.delay(1000)
        pygame.time.delay(500)
        quitter = 1
        pygame.mixer.music.stop()
        ns = 1 
        enemy.empty()
        if choix != 7:
            nn += 1
        if choix == 1:
            nn1 = 1
        elif choix == 2:
            nn2 = 1
        elif choix == 3:
            nn3 = 1
        elif choix == 4:
            nn4 = 1
        elif choix == 5:
            nn5 = 1
        elif choix == 6:
            nn6 = 1
        fade(900,600)
        game = False
        pygame.mixer.music.load("01.wav")
        pygame.mixer.music.play(loops=10^99)

def choicen():
    global game, choice, choix, nn, nn1, nn2, nn3, nn4, nn5, nn6
    choice = True
    while choice == True and game == False:
        screen.blit(backdrop2, (0, 0))
        player=pygame.Rect(170,380,20,20)
        textnc =  Texty3.render('Pour confirmer apppuyez sur \'Espace\'...', 0, (255,0,0))
        textinfos =  Texty5.render('Passez les 6 épreuves ! Le niveau "Classic" est un entraînement.', 0, (100,100,0))
        screen.blit(textinfos, (100,525))
        for event in pygame.event.get():
                        if event.type == KEYDOWN:
                                if event.key == K_0:
                                    choix = 0
                                if event.key == K_1:
                                    choixs.play()
                                    choix = 1
                                if event.key == K_2:
                                    choixs.play()
                                    choix = 2
                                if event.key == K_3:
                                    choixs.play()
                                    choix = 3
                                if event.key == K_4:
                                    choixs.play()
                                    choix = 4
                                if event.key == K_5:
                                    choixs.play()
                                    choix = 5
                                if event.key == K_6:
                                    choixs.play()
                                    choix = 6
                                if event.key == K_7:
                                    choixs.play()
                                    choix = 7
                                if event.key == K_SPACE and choix:
                                    if nn1 and choix == 1 or nn2 and choix == 2 or nn3 and choix == 3 or nn4 and choix == 4 or nn5 and choix == 5 or nn6 and choix == 6:
                                        choix = 0
                                        break
                                    fade(900,600)
                                    choice = False
                                    game = True
                                if event.key == K_a:
                                    choix = 0
                                    fade(900,600)
                                    choice = False
                        if event.type == QUIT:
                                quitter = 1
                                pygame.quit()
                                sys.exit()

        if choix == 0:
            textn =  Texty3.render('Choisissez une épreuve...', 0, (255,255,0))
            choicei = Texty5.render('Appuyez sur un numéro sur votre clavier en partant de 0 à 7.', 0, (100,100,255))
            screen.blit(textn, (250,50))
            screen.blit(choicei, (125,250))
        if choix == 1:
            textn =  Texty2.render('Philosophie', 0, (255,255,255))
            screen.blit(textn, (50,150))
            if nn1 == 1:
                textnc =  Texty3.render('Vous avez déjà fait cette épreuve !', 0, (255,0,0))
                screen.blit(textnc, (50,350))
            else:
                screen.blit(textnc, (50,350))
                
        if choix == 2:
            textn =  Texty2.render('Histoire-Géo.', 0, (255,255,255))
            screen.blit(textn, (30,150))
            if nn2 == 1:
                textnc =  Texty3.render('Vous avez déjà fait cette épreuve !', 0, (255,0,0))
                screen.blit(textnc, (50,350))
            else:
                screen.blit(textnc, (50,350))
        if choix == 3:
            textn =  Texty2.render('Langues', 0, (255,255,255))
            screen.blit(textn, (30,150))
            if nn3 == 1:
                textnc =  Texty3.render('Vous avez déjà fait cette épreuve !', 0, (255,0,0))
                screen.blit(textnc, (50,350))
            else:
                screen.blit(textnc, (50,350))
        if choix == 4:
            textn =  Texty2.render('Physique Ch.', 0, (255,255,255))
            screen.blit(textn, (30,150))
            if nn4 == 1:
                textnc =  Texty3.render('Vous avez déjà fait cette épreuve !', 0, (255,0,0))
                screen.blit(textnc, (50,350))
            else:
                screen.blit(textnc, (50,350))
        if choix == 5:
            textn =  Texty2.render('Maths', 0, (255,255,255))
            screen.blit(textn, (30,150))
            if nn5 == 1:
                textnc =  Texty3.render('Vous avez déjà fait cette épreuve !', 0, (255,0,0))
                screen.blit(textnc, (50,350))
            else:
                screen.blit(textnc, (50,350))
        if choix == 6:
            textn =  Texty2.render('S.V.T.', 0, (255,255,255))
            screen.blit(textn, (30,150))
            if nn6 == 1:
                textnc =  Texty3.render('Vous avez déjà fait cette épreuve !', 0, (255,0,0))
                screen.blit(textnc, (50,350))
            else:
                screen.blit(textnc, (50,350))
        if choix == 7:
            textn =  Texty2.render('Classic', 0, (255,255,255))
            screen.blit(textn, (30,150))
            screen.blit(textnc, (50,350))
        pygame.display.update()

def resuslts():
    global score, scorefinal, scorefin
    resusltats = True
    aa = 0
    cnx = 0
    aaa = -1
    blocked = 0
    newscore = scorefinal[0] + scorefinal[1] + scorefinal[2] + scorefinal[3] + scorefinal[4] + scorefinal[5]
    if newscore < 152:
        cnx = 1
    if newscore > 152:
        cnx = 0
    while resusltats == True:
        if aa == 0 and aaa == -1:
            screen.blit(backdrop2, (0, 0))
            textres =  Texty3.render('Vous avez fini les épreuves du BAC !', 0, (50,150,50))
            screen.blit(textres, (90,225))
            textres2 =  Texty7.render('L\'avez vous eu ?', 0, (255,255,0))
            screen.blit(textres2, (90,275))
            textres3 =  Texty3.render('Pour le savoir, appuyez sur \'espace\'...', 0, (90,100,100))
            screen.blit(textres3, (90,475))
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    aa = 1
                    if aa == 1:
                        if blocked == 1:
                            pass
                        elif blocked == 0:
                            aaa = 1
                            chrono1 = pygame.time.get_ticks()/1000
                            blocked = 1
            if event.type == QUIT:
                quitter = 1
                pygame.quit()
                sys.exit()            
                        
        if aaa == 1:
            screen.blit(backdrop2, (0, 0))
            chrono2 = pygame.time.get_ticks()/1000 - chrono1
            CT = 5
            chrono3 = CT - chrono2
            textres4 =  Textya.render('{0}'.format(int(chrono3)), 0, (255,255,255))
            screen.blit(textres4, (350,0))
            if int(chrono3) < 0:
                aaa = 0
        if aaa == 0:
             screen.blit(backdrop2, (0, 0))
             if cnx == 1:
                 textres5 =  Textya.render('NON', 0, (255,0,0))
                 screen.blit(textres5, (150,0))
                 textres6 =  Texty3.render('Vous avez échoué...', 0, (255,0,0))
                 textresq =  Texty3.render('Appuyez sur espace pour quitter...', 0, (255,255,255))
                 textres7 =  Texty3.render('{0} / 304 points'.format(newscore), 0, (100,100,100))
                 moy =  Texty5.render('(Moyenne = 152)'.format(newscore), 0, (255,0,0))
                 pygame.time.delay(1500)
                 screen.blit(textres6, (475,500))
                 screen.blit(textres7, (50,500))
                 screen.blit(textresq, (100,10))
                 screen.blit(moy, (215,480))
             elif cnx == 0:
                 textres5 =  Textya.render('OUI', 0, (0,255,0))
                 screen.blit(textres5, (150,0))
                 textres6 =  Texty3.render('Vous l\'avez eu !', 0, (0,255,0))
                 textresq =  Texty3.render('Appuyez sur espace pour quitter...', 0, (255,255,255))                 
                 textres7 =  Texty3.render('{0} / 304 points'.format(newscore), 0, (0,255,0))
                 moy =  Texty5.render('(Moyenne = 152)'.format(newscore), 0, (0,255,0))
                 pygame.time.delay(1500)
                 screen.blit(textres6, (475,500))
                 screen.blit(textres7, (50,500))
                 screen.blit(textresq, (100,10))
                 screen.blit(moy, (215,480))
             for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        fade(900,600)
                        resusltats = False
                        game = False
                        nn = 0
                        nn1 = 0
                        nn2 = 0
                        nn3 = 0
                        nn4 = 0
                        nn5 = 0
                        nn6 = 0
                        if cnx == 0:
                            pygame.quit()
                            sys.exit()
                    if event.type == QUIT:
                        quitter = 1
                        pygame.quit()
                        sys.exit()            
                            
        pygame.display.update()
    

   
################################################ Définition des variables ##################################################
###################### et des images ainsi que de tout ce qui sera utilisé dans le reste du programme (voir le fichier constances.py) ######################

pygame.init()

mainclock= pygame.time.Clock()

buga = Sprite(20, 550, 'bug.bmp')
pygame.mixer.music.load("01.wav")
pygame.mixer.music.play(loops=10^99)

quitter = 0

x = 0
ns = 0
buga.x = 50
buga.y = 510
nn = 0
nn1 = 0
nn2 = 0
nn3 = 0
nn4 = 0
nn5 = 0
nn6 = 0

scorefinal=[]



menu = True
game = False
choice = False
option=0
debug=0


###################################### Boucle du menu (en attente d'évènements) ############################################
while True:
        if nn == 6:
            resuslts()
        pygame.display.update()
        while game == False:
                screen.blit(backdrop2, (0, 0))
                screen.blit(Logo, (285,40))
                texts=Texty3.render('Sauvez votre BAC...', 0, (255,255,0))
                screen.blit(texts, (270,350))
                text2=Texty3.render('JOUER', 0, (0,255,0))
                screen.blit(text2, (410,200))
                text3=Texty3.render('QUITTER', 0, (0,255,0))
                screen.blit(text3, (410,300))
                text33=Texty3.render('Version Finale', 0, (255,0,0))
                screen.blit(text33, (300,500))
                text4=Texty4.render('Musique sous licence Creative Commons, SmallRadio : LSF 7th Gear Remix (dans le jeu), Pornophotonique : Sad robot (menu principal)', 0, (255,255,0))
                screen.blit(text4, (0,580))
                text5=Texty4.render('AMÉLIORÉ PAR RAYAN GRIB ET DANY REVILLARD & ANTHONY MARLIN', 0, (255,255,0))
                screen.blit(text5, (216,550))
                text6=Texty4.render("Visitez notre site web situé dans le dossier racine du jeu !", 0, (50,226,103))
                screen.blit(text6, (190,565))
                text88=Texty4.render("Appuyez sur D pour activer le débuggage (puis voir le Shell)", 0, (50,226,103))
                screen.blit(text88, (250,540))
                text8=Texty5.render('Choisiez une option, puis appuyez sur \'Entrée\'...', 0, (255,255,255))
                screen.blit(text8, (200,400))
                player=pygame.Rect(170,380,20,20)
                quitter = 0
                choix = 0
                enemyspeed = 2
                enemyspeed2 = 2
                for event in pygame.event.get():
                        if event.type==QUIT:
                                pygame.quit()
                                sys.exit()
                        if event.type== KEYDOWN:
                                if event.key== K_DOWN and option==0:
                                        option=option+1
                                        choixs.play()
                                if event.key==K_UP and option==1:
                                        option=option-1
                                        choixs.play()
                                if event.key==K_RETURN and option==1:
                                        pygame.mixer.music.stop()
                                        exits.play()
                                        fade(900,600)
                                        pygame.quit()
                                        sys.exit()
                                if event.key==K_RETURN and option==0:
                                        pygame.mixer.music.stop()
                                        tin.play()
                                        fade(900,600)
                                        choicen()                                      
                                if event.key==K_d:
                                        debug=1
                                        print('Mode Débogage activé !')
                                        win95.play()

                if option==0:
                    screen.blit(shipx,(player.left+180,player.top-172))
                    screen.blit(shipy,(350,308))
                if option==1:
                    screen.blit(shipx,(player.left+180,player.top-72))
                    screen.blit(shipy, (350,208))
                if ns == 1:
                        pygame.mixer.music.stop()
                        tin2.play()
                        ns = 0
                        pygame.display.update()
                        pygame.time.delay(1500)
                        pygame.mixer.music.play(loops=10^99)
                pygame.display.update()

############################################# "Si on lance le jeu alors" ###################################################

        while game == True:
                chrono1 = pygame.time.get_ticks()/1000
                score = 0
                all_sprites = pygame.sprite.Group()
                bullet = pygame.sprite.Group()
                enemy = pygame.sprite.Group()
                aliens = pygame.sprite.Group()
                bouclier1 = pygame.sprite.Group()
                bouclier2 = pygame.sprite.Group()
                bouclier3 = pygame.sprite.Group()
                bouclierall = pygame.sprite.Group()
                ourmissile3 = Bullet(20, 550, 'Missile 3.bmp')
                if choix == 1:
                    hero = Player(420,550, 'kant.png')
                    CT = 30
                elif choix == 2:
                    hero = Player(420,550, 'vaisseau2.png')
                    CT = 30
                elif choix == 3:
                    hero = Player(420,550, 'langvaiss.png')
                    CT = 20
                elif choix == 4:
                    hero = Player(420,550, 'acide.png')
                    CT = 30
                elif choix == 5:
                    hero = Player(420,550, 'calc.png')
                    CT = 35
                elif choix == 6:
                    hero = Player(420,550, 'itc.png')
                    CT = 40
                elif choix == 7:
                    hero = Player(420,550, 'si_vaisseaufinal.bmp')
                    CT = 20
                all_sprites.add(hero)
                if choix != 7:
                    shield2 = Sprite(100, 510, 'copie.png')
                    shield3 = Sprite(410, 510, 'copie.png')
                    shield4 = Sprite(700, 510, 'copie.png')
                elif choix == 7:
                    shield2 = Sprite(100, 510, 'si_shield3.bmp')
                    shield3 = Sprite(410, 510, 'si_shield3.bmp')
                    shield4 = Sprite(700, 510, 'si_shield3.bmp')                    
                bouclier1.add(shield2)
                bouclier2.add(shield3)
                bouclier3.add(shield4)
                bouclierall.add(bouclier1)
                bouclierall.add(bouclier2)
                bouclierall.add(bouclier3)
                all_sprites.add(shield2)
                all_sprites.add(shield3)
                all_sprites.add(shield4)
                all_sprites.add(bullet)
                all_sprites.add(bouclierall)
                
                if choix == 1:
                    for i in range(13):
                                bug = Enemy(20, 550, 'livre.png')
                                all_sprites.add(bug)
                                aliens.add(bug)
                elif choix == 2:
                    for i in range(18):
                                bug = Enemy(20, 550, 'nuke.png')
                                all_sprites.add(bug)
                                aliens.add(bug)
                elif choix == 3:
                            for i in range(10):
                                bug = Enemy(20, 550, 'iss.png')
                                all_sprites.add(bug)
                                aliens.add(bug)
                elif choix == 4:
                            for i in range(22):
                                bug = Enemy(20, 550, 'base.png')
                                all_sprites.add(bug)
                                aliens.add(bug)
                elif choix == 5:
                            for i in range(30):
                                bug = Enemy(20, 550, 'lnx.png')
                                all_sprites.add(bug)
                                aliens.add(bug)
                elif choix == 6:
                            for i in range(22):
                                bug = Enemy(20, 550, 'cell.png')
                                all_sprites.add(bug)
                                aliens.add(bug)
                elif choix == 7:
                            for i in range(10):
                                bug = Enemy(20, 550, 'si_perso2.bmp')
                                all_sprites.add(bug)
                                aliens.add(bug)
                all_sprites.remove(bug)        
                pygame.mixer.music.load("si_music.wav")
                pygame.mixer.music.play()
                n = 0
                hn1 = 0
                hn2 = 0
                hn3 = 0
                nei = 0
                ne = 0
                llo = 0
                missn = 0
                quitteres = 0
                x=0
                hero.x=420
                shield2.x = 100
                shield2.y = 510
                shield3.x = 410
                shield3.y = 510
                shield4.x = 700
                shield4.y = 510



                while quitter == 0:
                        if choix == 1:
                            backdrop = pygame.image.load('philoback.png')
                        elif choix == 2:
                            backdrop = pygame.image.load('histoire.png')
                        elif choix == 3:
                            backdrop = pygame.image.load('langues.png')
                        elif choix == 4:
                            backdrop = pygame.image.load('chimie.png')
                        elif choix == 5:
                            backdrop = pygame.image.load('maths.png')
                        elif choix == 6:
                            backdrop = pygame.image.load('svt.png')
                        elif choix == 7:
                            backdrop = pygame.image.load('si_fond2.bmp')
                                  
                        screen.blit(backdrop, (0, 0))
                        


########################################### Condition d'apparition d'un missile du vaisseau #####################################
                        
                        if ourmissile3.speedy > 900 and ourmissile3.speedy < 0:
                                ourmissile3.speedy = 100000
                                
#################### Chronomètre ########################
                        chrono2 = pygame.time.get_ticks()/1000 - chrono1
                        chrono3 = CT - chrono2
                        timee = int(chrono2)
                        timeer = int(chrono3)
                        timeet = TextyT.render('Temps écoulé : {0}'.format(timee), 0, (150,255,0))
                        timeetS = TextyT.render('Temps écoulé : {0}'.format(timee), 0, (0,0,0))
                        timeert = TextyT.render('Temps restant : {0}'.format(timeer), 0, (150,255,0))
                        timeertS = TextyT.render('Temps restant : {0}'.format(timeer), 0, (0,0,0))
                        screen.blit(timeetS,(21,21))
                        screen.blit(timeet,(20,20))
                        screen.blit(timeertS,(21,41))
                        screen.blit(timeert,(20,40))
                                
################# Condition de "si plus d'ennemis alors", alors que le jeu n'est pas arreté #################################

                        if game == True:
                                if len(aliens) == 0:
                                        win()
                                if len(bouclier1) == 0 and len(bouclier2) == 0 and len(bouclier3) == 0 or timeer < 0:
                                        perdu()                                     
############################# Boucle principale du jeu (en attente d'évènements définis précédemment) ######################


                        for event in pygame.event.get():
                                if event.type == QUIT:
                                        quitter = 1
                                        pygame.quit()
                                        sys.exit()
                                if event.type == KEYDOWN:

                                        if event.key == K_SPACE:
                                                if choix == 1:
                                                    hero.shoot('pensee.png')
                                                pew.play()
                                                if choix == 2:
                                                    hero.shoot('mssilehis.png')
                                                pew.play()
                                                if choix == 3:
                                                    hero.shoot('voc.png')
                                                pew.play()
                                                if choix == 4:
                                                    hero.shoot('h.png')
                                                pew.play()
                                                if choix == 5:
                                                    hero.shoot('ex.png')
                                                pew.play()
                                                if choix == 6:
                                                    hero.shoot('perf.gif')
                                                pew.play()
                                                if choix == 7:
                                                    hero.shoot('Missile 3.bmp')
                                                pew.play() 
                                        if event.key == K_ESCAPE:
                                                pause()
                        if quitteres == 1:
                                quitter = 1
                                x=0
                                hero.x=420
                                shield2.x = 100
                                shield2.y = 510
                                shield3.x = 410
                                shield3.y = 510
                                shield4.x = 700
                                shield4.y = 510
                                enemy.empty()
                                pygame.mixer.music.stop()
                                game = False
                                ns =1
                                pygame.mixer.music.load("01.wav")
                                pygame.mixer.music.play(loops=10^99)

############################################# Affichage des éléments du jeu ################################################


                        hits = pygame.sprite.spritecollide(hero, aliens, False)
                        if hits:
                                perdu()
                        hitenemy = pygame.sprite.groupcollide(bullet, aliens, True, True)
                        if hitenemy:
                                score += 1
                                aliens.remove(bug)
                        hitb1 = pygame.sprite.groupcollide(bouclier1, aliens, True, True)
                        hitb2 = pygame.sprite.groupcollide(bouclier2, aliens, True, True)
                        hitb3 = pygame.sprite.groupcollide(bouclier3, aliens, True, True)
                        hita = pygame.sprite.collide_rect(bug, bug)
                        hit20 = pygame.sprite.groupcollide(bullet, bouclier1, True, False)
                        hit21 = pygame.sprite.groupcollide(bullet, bouclier2, True, False)
                        hit22 = pygame.sprite.groupcollide(bullet, bouclier3, True, False)

                        if debug == 1:
                            print(mainclock.get_fps())
                        all_sprites.draw(screen)
                        all_sprites.update()        
                        pygame.display.update()
                        pygame.time.delay(5)
                        mainclock.tick(60)
