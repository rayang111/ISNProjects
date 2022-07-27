#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame,sys
from pygame.locals import *
import random
import os


pygame.init()

screen = pygame.display.set_mode((900,600))
pygame.key.set_repeat(0, 1)
pygame.display.set_caption('Space Invaders BAC')
backdrop = pygame.image.load('si_fond2.bmp')
backdrop2 = pygame.image.load('new-BG.bmp')
Logo = pygame.image.load('SIB.png')
Logo = pygame.transform.scale(Logo, (375, 125))
Texty = pygame.font.Font('si.ttf', 125)
Textya = pygame.font.Font('si.ttf', 500)
Texty2 = pygame.font.Font('si.ttf', 200)
Texty7 = pygame.font.Font('si.ttf', 90)
Texty3 = pygame.font.Font('si.ttf', 60)
Texty4 = pygame.font.Font('si.ttf', 20)
Texty5 = pygame.font.Font('si.ttf', 30)
Texty6 = pygame.font.Font('si.ttf', 40)
TextyT = pygame.font.Font('si.ttf', 18)



shipx=pygame.image.load('si_perso2.bmp')
shipy=pygame.image.load('si_perso3.bmp')


pygame.mixer.init()


pew = pygame.mixer.Sound("si_pew.wav")
win95 = pygame.mixer.Sound("egg.wav")
wins = pygame.mixer.Sound("win.wav")
exits = pygame.mixer.Sound("exit.wav")
startc = pygame.mixer.Sound("start.wav")
choixs = pygame.mixer.Sound("choix.wav")
gameover = pygame.mixer.Sound("si_gameover.wav")
tin = pygame.mixer.Sound("tin.wav")
tin2 = pygame.mixer.Sound("tin2.wav")
