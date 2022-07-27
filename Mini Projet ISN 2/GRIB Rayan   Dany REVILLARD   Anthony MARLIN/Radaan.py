#-*- coding utf-8 -*-
######## R A D A A N ##########################################

from tkinter import *
from PIL import ImageTk , Image
import tkinter , tkinter.filedialog, tkinter.ttk
from tkinter.messagebox import *
import os
import winsound
from random import randrange

############### Chargement de L'image et récupération de ses  données#################


def loadf():
   "Affiche une image choisie par L'utilisateur et mémorise les informations de L'image"
   winsound.PlaySound('data\Audio\clic.wav',winsound.SND_FILENAME)
   try:
      global PHOTO,PHOTOTK,L,H,M,DATA,DATAOUT,PIXELS,IMOUT,REFRESH
      c1.delete(tkinter.ALL)
      src=tkinter.filedialog.askopenfilename()
      PHOTO=Image.open(src)
      PHOTO.save('data\EFFET.png')
      PHOTO.save('data\EFFET2.png')
      PHOTOTK=ImageTk.PhotoImage(PHOTO)
      L,H,M=PHOTO.size[0],PHOTO.size[1],PHOTO.mode
      DATA=list(PHOTO.getdata())
      DATAOUT=[]
      PIXELS=PHOTO.load()
      IMOUT=Image.new(M ,(L,H))
      c1.config(width=L,height=H)
      REFRESH=c1.create_image(L/2,H/2,image=PHOTOTK)
   except OSError:
      showerror('Erreur','Vous avez ouvert un fichier incompatible avec R A D A A N. Le logiciel supporte uniquement les images.')
   except AttributeError:
      c1.create_image(L/2,H/2,image=DEBU2T)
   
################## Crée un négatif d'une image en niveau de gris######################


def negatif():
   "Crée un négatif de L'image en niveau de gris"
   for i in range(len(DATA)):          
       DATAOUT.append(255-DATA[i]) 
   IMOUT.putdata(DATAOUT)  
   affiche()

################## Modifie une luminosité (additive)######################


def lumino():
   try:
      PHOTO=Image.open('data\EFFET.png')
      PIXELS=PHOTO.load()
      m=PHOTO.mode
      l=PHOTO.size[0]
      h=PHOTO.size[1]
      showinfo("Allez sur la console.","Veuillez aller sur la console, cet effet a besoin d'un paramètre que vous entrerez.")
      k=int(input("Entrez une valeur pour modifier la luminosité :"))
      for i in range(l):
          for j in range(h):
              IMOUT.putpixel((i,j),(PIXELS[i,j][0]+k,PIXELS[i,j][1]+k,PIXELS[i,j][2]+k))
      affiche()
      IMOUT.save('data\EFFET.png')      
   except NameError:
      showerror('Erreur','Vous n\'avez ouvert aucune image. Ouvrez une image avant d\'appliquer un effet')
   except TypeError:
      showerror('Erreur','Effet incompatible sur cette image.')
   except ValueError:
      showerror('Erreur','Vous n\'avez pas rentré un nombre. Réessayez en entrant seulement un nombre.')
   

################## Crée un flou gaussien######################


def flou_gaussien():
   try:
      PHOTO=Image.open('data\EFFET.png')
      PIXELS=PHOTO.load()
      m=PHOTO.mode
      l=PHOTO.size[0]
      h=PHOTO.size[1]
      f1,f2,f3,f4,f5,f6,f7,f8,f9=1,2,1,2,4,2,1,2,1
      f0=1/16
      for i in range(1,l-1):
         for j in range(1,h-1):
            p1=PIXELS[i-1,j-1]
            p2=PIXELS[i,j-1]
            p3=PIXELS[i+1,j-1]
            p4=PIXELS[i-1,j]
            p5=PIXELS[i,j]
            p6=PIXELS[i+1,j]
            p7=PIXELS[i-1,j+1]
            p8=PIXELS[i,j+1]
            p9=PIXELS[i+1,j+1]
            r=int(f0*(f1*p1[0]+f2*p2[0]+f3*p3[0]+f4*p4[0]+f5*p5[0]+f6*p6[0]+f7*p7[0]+f8*p8[0]+f9*p9[0]))
            g=int(f0*(f1*p1[1]+f2*p2[1]+f3*p3[1]+f4*p4[1]+f5*p5[1]+f6*p6[1]+f7*p7[1]+f8*p8[1]+f9*p9[1]))
            b=int(f0*(f1*p1[2]+f2*p2[2]+f3*p3[2]+f4*p4[2]+f5*p5[2]+f6*p6[2]+f7*p7[2]+f8*p8[2]+f9*p9[2]))
            IMOUT.putpixel((i,j),(r,g,b))
      affiche()
      IMOUT.save('data\EFFET.png')
   except NameError:
      showerror('Erreur','Vous n\'avez ouvert aucune image. Ouvrez une image avant d\'appliquer un effet')
   except TypeError:
      showerror('Erreur','Effet incompatible sur cette image.')

################## Crée un effet sépia######################


def sepia():
   try:
      PHOTO=Image.open('data\EFFET.png')
      PIXELS=PHOTO.load()
      m=PHOTO.mode
      l=PHOTO.size[0]
      h=PHOTO.size[1]
      for i in range(l):
         for j in range(h):
            g=int((PIXELS[i,j][0]+PIXELS[i,j][1]+PIXELS[i,j][2])/3)+10
            r=g+20
            b=int((PIXELS[i,j][0]+PIXELS[i,j][1]+PIXELS[i,j][2])/3)
            IMOUT.putpixel((i,j),(r,g,b))
      affiche()
      IMOUT.save('data\EFFET.png')
   except NameError:
      showerror('Erreur','Vous n\'avez ouvert aucune image. Ouvrez une image avant d\'appliquer un effet')
   except TypeError:
      showerror('Erreur','Effet incompatible sur cette image.')


################## Crée un effet de contraste######################


def contraste():
   try:
      PHOTO=Image.open('data\EFFET.png')
      PIXELS=PHOTO.load()
      m=PHOTO.mode
      l=PHOTO.size[0]
      h=PHOTO.size[1]
      f1,f2,f3,f4,f5,f6,f7,f8,f9=1,-3,1,-3,9,-3,1,-3,1 #coefficients du filtre à appliquer
      f0=1 #diviseur
      for i in range(1,l-1):
             for j in range(1,h-1):
                p1=PIXELS[i-1,j-1]
                p2=PIXELS[i,j-1]
                p3=PIXELS[i+1,j-1]
                p4=PIXELS[i-1,j]
                p5=PIXELS[i,j]
                p6=PIXELS[i+1,j]
                p7=PIXELS[i-1,j+1]
                p8=PIXELS[i,j+1]
                p9=PIXELS[i+1,j+1]
                r=int(f0*(f1*p1[0]+f2*p2[0]+f3*p3[0]+f4*p4[0]+f5*p5[0]+f6*p6[0]+f7*p7[0]+f8*p8[0]+f9*p9[0]))
                g=int(f0*(f1*p1[1]+f2*p2[1]+f3*p3[1]+f4*p4[1]+f5*p5[1]+f6*p6[1]+f7*p7[1]+f8*p8[1]+f9*p9[1]))
                b=int(f0*(f1*p1[2]+f2*p2[2]+f3*p3[2]+f4*p4[2]+f5*p5[2]+f6*p6[2]+f7*p7[2]+f8*p8[2]+f9*p9[2]))
                IMOUT.putpixel((i,j),(r,g,b))
      affiche()
      IMOUT.save('data\EFFET.png')
   except NameError:
      showerror('Erreur','Vous n\'avez ouvert aucune image. Ouvrez une image avant d\'appliquer un effet')
   except TypeError:
      showerror('Erreur','Effet incompatible sur cette image.')


################## Crée un flou moyen######################


def flou_moyen():
   try:
      PHOTO=Image.open('data\EFFET.png')
      PIXELS=PHOTO.load()
      m=PHOTO.mode
      l=PHOTO.size[0]
      h=PHOTO.size[1]
      for i in range(1,l-1):
          for j in range(1,h-1):
           IMOUT.putpixel((i,j),(int((PIXELS[i-1,j-1][0]+PIXELS[i-1,j][0]+PIXELS[i-1,j+1][0]+PIXELS[i,j-1][0]+PIXELS[i,j+1][0]+PIXELS[i+1,j-1][0]+PIXELS[i+1,j][0]+PIXELS[i+1,j+1][0])/8),int((PIXELS[i-1,j-1][1]+PIXELS[i-1,j][1]+PIXELS[i-1,j+1][1]+PIXELS[i,j-1][1]+PIXELS[i,j+1][1]+PIXELS[i+1,j-1][1]+PIXELS[i+1,j][1]+PIXELS[i+1,j+1][1])/8),int((PIXELS[i-1,j-1][2]+PIXELS[i-1,j][2]+PIXELS[i-1,j+1][2]+PIXELS[i,j-1][2]+PIXELS[i,j+1][2]+PIXELS[i+1,j-1][2]+PIXELS[i+1,j][2]+PIXELS[i+1,j+1][2])/8)))
      affiche()
      IMOUT.save('data\EFFET.png')
   except NameError:
      showerror('Erreur','Vous n\'avez ouvert aucune image. Ouvrez une image avant d\'appliquer un effet')
   except TypeError:
      showerror('Erreur','Effet incompatible sur cette image.')


################## Crée un effet accentuation######################

  
def accentuation():
   try:
      PHOTO=Image.open('data\EFFET.png')
      PIXELS=PHOTO.load()
      m=PHOTO.mode
      l=PHOTO.size[0]
      h=PHOTO.size[1]
      f1,f2,f3,f4,f5,f6,f7,f8,f9=0,-1,0,-1,5,-1,0,-1,0
      f0=1
      for i in range(1,l-1):
          for j in range(1,h-1):
             p1=PIXELS[i-1,j-1]
             p2=PIXELS[i,j-1]
             p3=PIXELS[i+1,j-1]
             p4=PIXELS[i-1,j]
             p5=PIXELS[i,j]
             p6=PIXELS[i+1,j]
             p7=PIXELS[i-1,j+1]
             p8=PIXELS[i,j+1]
             p9=PIXELS[i+1,j+1]
             r=int(f0*(f1*p1[0]+f2*p2[0]+f3*p3[0]+f4*p4[0]+f5*p5[0]+f6*p6[0]+f7*p7[0]+f8*p8[0]+f9*p9[0]))
             g=int(f0*(f1*p1[1]+f2*p2[1]+f3*p3[1]+f4*p4[1]+f5*p5[1]+f6*p6[1]+f7*p7[1]+f8*p8[1]+f9*p9[1]))
             b=int(f0*(f1*p1[2]+f2*p2[2]+f3*p3[2]+f4*p4[2]+f5*p5[2]+f6*p6[2]+f7*p7[2]+f8*p8[2]+f9*p9[2]))
             IMOUT.putpixel((i,j),(r,g,b))
      affiche()
      IMOUT.save('data\EFFET.png')
   except NameError:
      showerror('Erreur','Vous n\'avez ouvert aucune image. Ouvrez une image avant d\'appliquer un effet')
   except TypeError:
      showerror('Erreur','Effet incompatible sur cette image.')



################## Crée un effet de difference entre deux images######################

def difference():
   try:
      PHOTO=Image.open('data\EFFET.png')
      PIXELS=PHOTO.load()
      showinfo("Information.","Cet effet a besoin a besoin d'une seconde image, vous allez la choisir.")
      src2=tkinter.filedialog.askopenfilename()
      PHOTO2 = Image.open(src2)
      PHOTOTK2=ImageTk.PhotoImage(PHOTO2)
      L,H,M=PHOTO2.size[0],PHOTO2.size[1],PHOTO2.mode
      DATA2=list(PHOTO2.getdata())
      DATAOUT2=[]
      im1=PHOTO
      im2=PHOTO2
      pixels2=im2.load()
      m1=im1.mode
      l1=im1.size[0]
      h1=im1.size[1]
      m2=im2.mode
      l2=im2.size[0]
      h2=im2.size[1]
      for i in range(l1):
          for j in range(h1):
              r=int(PIXELS[i,j][0]-pixels2[i,j][0])
              g=int(PIXELS[i,j][1]-pixels2[i,j][1])
              b=int(PIXELS[i,j][2]-pixels2[i,j][2])
              IMOUT.putpixel((i,j),(r,g,b))
      affiche()
      IMOUT.save('data\EFFET.png')      
   except NameError:
      showerror('Erreur','Vous n\'avez pas ouvert d\'image avant d\'appliquer l\'effet. Ouvrez une image avant d\'appliquer l\'effet')
   except TypeError:
      showerror('Erreur','Effet incompatible sur cette image.')



################## Crée un effet de rotation vers la gauche######################


def rotation_gauche():
   try:
      PHOTO=Image.open('data\EFFET.png')
      PIXELS=PHOTO.load()
      out = PHOTO.rotate(90)
      out.save('data\ROTATIONG.png')
      ROT = Image.open('data\ROTATIONG.png')
      data2=list(ROT.getdata())
      IMOUT.putdata(data2)
      affiche()
      IMOUT.save('data\EFFET.png')
   except NameError:
      showerror('Erreur','Vous n\'avez ouvert aucune image. Ouvrez une image avant d\'appliquer un effet')
   except ValueError:
      showerror('Erreur','Vous n\'avez pas rentré un nombre. Réessayez en entrant seulement un nombre.')

################## Crée un effet de rotation vers la droite######################


def rotation_droit():
   try:
      PHOTO=Image.open('data\EFFET.png')
      PIXELS=PHOTO.load()
      out = PHOTO.rotate(-90)
      out.save('data\ROTATIOND.png')
      ROT = Image.open('data\ROTATIOND.png')
      data2=list(ROT.getdata())
      IMOUT.putdata(data2)
      affiche()
      IMOUT.save('data\EFFET.png')
   except NameError:
      showerror('Erreur','Vous n\'avez ouvert aucune image. Ouvrez une image avant d\'appliquer un effet')
   except ValueError:
      showerror('Erreur','Vous n\'avez pas rentré un nombre. Réessayez en entrant seulement un nombre.')
      

################## Crée un effet de rotation personnalisé######################


def rotation_perso():
   try:
      PHOTO=Image.open('data\EFFET.png')
      PIXELS=PHOTO.load()
      showinfo("Allez sur la console.","Veuillez aller sur la console, cet effet a besoin d'un paramètre que vous entrerez.")
      val = int(input("Valeur de la rotation ? : "))
      out = PHOTO.rotate(val)
      out.save('data\ROTATIONP.png')
      ROT = Image.open('data\ROTATIONP.png')
      data2=list(ROT.getdata())
      IMOUT.putdata(data2)
      affiche()
      IMOUT.save('data\EFFET.png')
   except NameError:
      showerror('Erreur','Vous n\'avez ouvert aucune image. Ouvrez une image avant d\'appliquer un effet')

################## Convertit une image RGB en niveaux de gris######################
    
def niveaux_de_gris():
   try:
      global IMOUT
      PHOTO=Image.open('data\EFFET.png')
      PIXELS=PHOTO.load()
      m=PHOTO.mode
      l=PHOTO.size[0]
      h=PHOTO.size[1]
      IMOUT=Image.new('L',PHOTO.size)
      for i in range(l):
         for j in range(h):
            IMOUT.putpixel((i,j),(int((PIXELS[i,j][0]+PIXELS[i,j][1]+PIXELS[i,j][2])/3)))
      affiche()
      IMOUT=Image.new(M ,(L,H))
      IMOUT.save('data\EFFET.png')
   except NameError:
      showerror('Erreur','Vous n\'avez ouvert aucune image. Ouvrez une image avant d\'appliquer un effet')
   except TypeError:
      showerror('Erreur','Effet incompatible sur cette image.')


################## Crée un effet qui est aléatoire######################


def random():
   try:
      PHOTO=Image.open('data\EFFET.png')
      PIXELS=PHOTO.load()
      pixels=PIXELS
      im=PHOTO
      m=im.mode
      l=im.size[0]
      h=im.size[1]
      f1=randrange(-20,20,1)
      f2=randrange(-20,20,1)
      f3=randrange(-20,20,1)
      f4=randrange(-20,20,1)
      f5=randrange(-20,20,1)
      f6=randrange(-20,20,1)
      f7=randrange(-20,20,1)
      f8=randrange(-20,20,1)
      f9=randrange(-20,20,1)
      f0=1
      for i in range(1,l-1):
         for j in range(1,h-1):
             p1=pixels[i-1,j-1]
             p2=pixels[i,j-1]
             p3=pixels[i+1,j-1]
             p4=pixels[i-1,j]
             p5=pixels[i,j]
             p6=pixels[i+1,j]
             p7=pixels[i-1,j+1]
             p8=pixels[i,j+1]
             p9=pixels[i+1,j+1]
             r=int(f0*(f1*p1[0]+f2*p2[0]+f3*p3[0]+f4*p4[0]+f5*p5[0]+f6*p6[0]+f7*p7[0]+f8*p8[0]+f9*p9[0]))
             g=int(f0*(f1*p1[1]+f2*p2[1]+f3*p3[1]+f4*p4[1]+f5*p5[1]+f6*p6[1]+f7*p7[1]+f8*p8[1]+f9*p9[1]))
             b=int(f0*(f1*p1[2]+f2*p2[2]+f3*p3[2]+f4*p4[2]+f5*p5[2]+f6*p6[2]+f7*p7[2]+f8*p8[2]+f9*p9[2]))
             IMOUT.putpixel((i,j),(r,g,b))
      affiche()
      IMOUT.save('data\EFFET.png')
   except NameError:
      showerror('Erreur','Vous n\'avez ouvert aucune image. Ouvrez une image avant d\'appliquer un effet')
   except TypeError:
      showerror('Erreur','Effet incompatible sur cette image.')


################## Modifie la lumininosité (multiplié)######################


def luminosité_multi():
   try:
      PHOTO=Image.open('data\EFFET.png')
      PIXELS=PHOTO.load()
      m=PHOTO.mode
      l=PHOTO.size[0]
      h=PHOTO.size[1]
      showinfo("Allez sur la console.","Veuillez aller sur la console, cet effet a besoin d'un paramètre que vous entrerez.")
      k=float(input("Entrez une valeur pour modifier la luminosité :"))
      for i in range(l):
         for j in range(h):
            IMOUT.putpixel((i,j),(int(PIXELS[i,j][0]*k),int(PIXELS[i,j][1]*k),int(PIXELS[i,j][2]*k)))
      affiche()
      IMOUT.save('data\EFFET.png')
   except NameError:
      showerror('Erreur','Vous n\'avez ouvert aucune image. Ouvrez une image avant d\'appliquer un effet')
   except TypeError:
      showerror('Erreur','Effet incompatible sur cette image.')
   except ValueError:
      showerror('Erreur','Vous n\'avez pas rentré un nombre. Réessayez en entrant seulement un nombre.')
      
################## Crée un produit entre deux images######################

def produit():
   try:
      PHOTO=Image.open('data\EFFET.png')
      PIXELS=PHOTO.load()
      showinfo("Information.","Cet effet a besoin a besoin d'une seconde image, vous allez la choisir.")
      src2=tkinter.filedialog.askopenfilename()
      PHOTO2 = Image.open(src2)
      PHOTOTK2=ImageTk.PhotoImage(PHOTO2)
      L,H,M=PHOTO2.size[0],PHOTO2.size[1],PHOTO2.mode
      DATA2=list(PHOTO2.getdata())
      DATAOUT2=[]
      im2=PHOTO2
      pixels2=im2.load()
      im1=PHOTO
      m1=im1.mode
      l1=im1.size[0]
      h1=im1.size[1]
      m2=im2.mode
      l2=im2.size[0]
      h2=im2.size[1]
      for i in range(l1):
         for j in range(h1):
            r=int(PIXELS[i,j][0]*pixels2[i,j][0])
            g=int(PIXELS[i,j][1]*pixels2[i,j][1])
            b=int(PIXELS[i,j][2]*pixels2[i,j][2])
            IMOUT.putpixel((i,j),(r,g,b))
      affiche()
      IMOUT.save('data\EFFET.png')
   except NameError:
      showerror('Vous n\'avez pas ouvert d\'image avant d\'appliquer l\'effet. Ouvrez une image avant d\'appliquer l\'effet')
   except TypeError:
      showerror('Erreur','Effet incompatible sur cette image.')



################## Crée un effet de contraste faible######################

def fcontraste():
   try:
      PHOTO=Image.open('data\EFFET.png')
      PIXELS=PHOTO.load()
      pixels=PIXELS
      m=PHOTO.mode
      l=PHOTO.size[0]
      h=PHOTO.size[1]
      f1,f2,f3,f4,f5,f6,f7,f8,f9=0,-1,0,-1,5,-1,0,-1,0
      f0=1
      for i in range(1,l-1):
          for j in range(1,h-1):
             p1=pixels[i-1,j-1]
             p2=pixels[i,j-1]
             p3=pixels[i+1,j-1]
             p4=pixels[i-1,j]
             p5=pixels[i,j]
             p6=pixels[i+1,j]
             p7=pixels[i-1,j+1]
             p8=pixels[i,j+1]
             p9=pixels[i+1,j+1]
             r=int(f0*(f1*p1[0]+f2*p2[0]+f3*p3[0]+f4*p4[0]+f5*p5[0]+f6*p6[0]+f7*p7[0]+f8*p8[0]+f9*p9[0]))
             g=int(f0*(f1*p1[1]+f2*p2[1]+f3*p3[1]+f4*p4[1]+f5*p5[1]+f6*p6[1]+f7*p7[1]+f8*p8[1]+f9*p9[1]))
             b=int(f0*(f1*p1[2]+f2*p2[2]+f3*p3[2]+f4*p4[2]+f5*p5[2]+f6*p6[2]+f7*p7[2]+f8*p8[2]+f9*p9[2]))
             IMOUT.putpixel((i,j),(r,g,b))
      affiche()
      IMOUT.save('data\EFFET.png')
   except NameError:
      showerror('Erreur','Vous n\'avez ouvert aucune image. Ouvrez une image avant d\'appliquer un effet')
   except TypeError:
      showerror('Erreur','Effet incompatible sur cette image.')



################## Crée un effet de contour######################

def contour():
   try:
      PHOTO=Image.open('data\EFFET.png')
      PIXELS=PHOTO.load()
      im=PHOTO
      pixels=PIXELS
      m=im.mode
      l=im.size[0]
      h=im.size[1]
      f1,f2,f3,f4,f5,f6,f7,f8,f9=0,1,0,1,-4,0,0,1,0 #coefficients du filtre à appliquer
      f0=1 #diviseur
      imout=Image.new(im.mode,im.size)
      for i in range(1,l-1):
          for j in range(1,h-1):
             p1=pixels[i-1,j-1]
             p2=pixels[i,j-1]
             p3=pixels[i+1,j-1]
             p4=pixels[i-1,j]
             p5=pixels[i,j]
             p6=pixels[i+1,j]
             p7=pixels[i-1,j+1]
             p8=pixels[i,j+1]
             p9=pixels[i+1,j+1]
             r=int(f0*(f1*p1[0]+f2*p2[0]+f3*p3[0]+f4*p4[0]+f5*p5[0]+f6*p6[0]+f7*p7[0]+f8*p8[0]+f9*p9[0]))
             g=int(f0*(f1*p1[1]+f2*p2[1]+f3*p3[1]+f4*p4[1]+f5*p5[1]+f6*p6[1]+f7*p7[1]+f8*p8[1]+f9*p9[1]))
             b=int(f0*(f1*p1[2]+f2*p2[2]+f3*p3[2]+f4*p4[2]+f5*p5[2]+f6*p6[2]+f7*p7[2]+f8*p8[2]+f9*p9[2]))
             IMOUT.putpixel((i,j),(r,g,b))
      affiche()
      IMOUT.save('data\EFFET.png')

   except NameError:
      showerror('Erreur','Vous n\'avez ouvert aucune image. Ouvrez une image avant d\'appliquer un effet')
   except TypeError:
      showerror('Erreur','Effet incompatible sur cette image.')



################## Crée un effet laplacien######################

def laplacien():
   try:
      PHOTO=Image.open('data\EFFET.png')
      PIXELS=PHOTO.load()
      pixels=PIXELS
      im=PHOTO
      m=im.mode
      l=im.size[0]
      h=im.size[1]
      f1,f2,f3,f4,f5,f6,f7,f8,f9=0,1,0,1,-4,1,0,1,0 #coefficients du filtre à appliquer
      f0=1 #diviseur
      for i in range(1,l-1):
          for j in range(1,h-1):
             p1=pixels[i-1,j-1]
             p2=pixels[i,j-1]
             p3=pixels[i+1,j-1]
             p4=pixels[i-1,j]
             p5=pixels[i,j]
             p6=pixels[i+1,j]
             p7=pixels[i-1,j+1]
             p8=pixels[i,j+1]
             p9=pixels[i+1,j+1]
             r=int(f0*(f1*p1[0]+f2*p2[0]+f3*p3[0]+f4*p4[0]+f5*p5[0]+f6*p6[0]+f7*p7[0]+f8*p8[0]+f9*p9[0]))
             g=int(f0*(f1*p1[1]+f2*p2[1]+f3*p3[1]+f4*p4[1]+f5*p5[1]+f6*p6[1]+f7*p7[1]+f8*p8[1]+f9*p9[1]))
             b=int(f0*(f1*p1[2]+f2*p2[2]+f3*p3[2]+f4*p4[2]+f5*p5[2]+f6*p6[2]+f7*p7[2]+f8*p8[2]+f9*p9[2]))
             IMOUT.putpixel((i,j),(r,g,b))
      affiche()
      IMOUT.save('data\EFFET.png')
   except NameError:
      showerror('Erreur','Vous n\'avez ouvert aucune image. Ouvrez une image avant d\'appliquer un effet')
   except TypeError:
      showerror('Erreur','Effet incompatible sur cette image.')



################## Crée un effet sobel######################

def sobel():
   try:
      PHOTO=Image.open('data\EFFET.png')
      PIXELS=PHOTO.load()
      pixels=PIXELS
      im=PHOTO
      m=im.mode
      l=im.size[0]
      h=im.size[1]
      f1,f2,f3,f4,f5,f6,f7,f8,f9=-1,0,1,-2,0,2,-1,0,1 #coefficients du filtre à appliquer
      f0=1 #diviseur
      for i in range(1,l-1):
          for j in range(1,h-1):
             p1=pixels[i-1,j-1]
             p2=pixels[i,j-1]
             p3=pixels[i+1,j-1]
             p4=pixels[i-1,j]
             p5=pixels[i,j]
             p6=pixels[i+1,j]
             p7=pixels[i-1,j+1]
             p8=pixels[i,j+1]
             p9=pixels[i+1,j+1]
             r=int(f0*(f1*p1[0]+f2*p2[0]+f3*p3[0]+f4*p4[0]+f5*p5[0]+f6*p6[0]+f7*p7[0]+f8*p8[0]+f9*p9[0]))
             g=int(f0*(f1*p1[1]+f2*p2[1]+f3*p3[1]+f4*p4[1]+f5*p5[1]+f6*p6[1]+f7*p7[1]+f8*p8[1]+f9*p9[1]))
             b=int(f0*(f1*p1[2]+f2*p2[2]+f3*p3[2]+f4*p4[2]+f5*p5[2]+f6*p6[2]+f7*p7[2]+f8*p8[2]+f9*p9[2]))
             IMOUT.putpixel((i,j),(r,g,b))
      affiche()
      IMOUT.save('data\EFFET.png')      
   except NameError:
      showerror('Erreur','Vous n\'avez ouvert aucune image. Ouvrez une image avant d\'appliquer un effet')
   except TypeError:
      showerror('Erreur','Effet incompatible sur cette image.')



################## Crée un effet gradient oblique######################

def gradient_oblique():
   try:
      PHOTO=Image.open('data\EFFET.png')
      PIXELS=PHOTO.load()
      pixels=PIXELS
      im=PHOTO
      m=im.mode
      l=im.size[0]
      h=im.size[1]
      f1,f2,f3,f4,f5,f6,f7,f8,f9=-1,-1,0,-1,0,1,0,1,1 #coefficients du filtre à appliquer
      f0=1 #diviseur
      for i in range(1,l-1):
          for j in range(1,h-1):
             p1=pixels[i-1,j-1]
             p2=pixels[i,j-1]
             p3=pixels[i+1,j-1]
             p4=pixels[i-1,j]
             p5=pixels[i,j]
             p6=pixels[i+1,j]
             p7=pixels[i-1,j+1]
             p8=pixels[i,j+1]
             p9=pixels[i+1,j+1]
             r=int(f0*(f1*p1[0]+f2*p2[0]+f3*p3[0]+f4*p4[0]+f5*p5[0]+f6*p6[0]+f7*p7[0]+f8*p8[0]+f9*p9[0]))
             g=int(f0*(f1*p1[1]+f2*p2[1]+f3*p3[1]+f4*p4[1]+f5*p5[1]+f6*p6[1]+f7*p7[1]+f8*p8[1]+f9*p9[1]))
             b=int(f0*(f1*p1[2]+f2*p2[2]+f3*p3[2]+f4*p4[2]+f5*p5[2]+f6*p6[2]+f7*p7[2]+f8*p8[2]+f9*p9[2]))
             IMOUT.putpixel((i,j),(r,g,b))
      affiche()
      IMOUT.save('data\EFFET.png')      
   except NameError:
      showerror('Erreur','Vous n\'avez ouvert aucune image. Ouvrez une image avant d\'appliquer un effet')
   except TypeError:
      showerror('Erreur','Effet incompatible sur cette image.')


################## Crée un négatif couleur ############################################

def negatifcouleur():
   "Crée un  négatif  couleur"
   try:
      PHOTO=Image.open('data\EFFET.png')
      PIXELS=PHOTO.load()
      for i in range(L):          
          for j in range(H):
                 IMOUT.putpixel((i,j),(255-PIXELS[i,j][0],255-PIXELS[i,j][1],255-PIXELS[i,j][2]))
      affiche()
      IMOUT.save('data\EFFET.png')
   except NameError:
      showerror('Erreur','Vous n\'avez ouvert aucune image. Ouvrez une image avant d\'appliquer un effet')
   except TypeError:
      showerror('Erreur','Effet incompatible sur cette image.')


################### Crée un négatif ############################################

def neg():
   try:
      if M=='L' or M=='P':
         negatif()
      elif M=='RGB' or M=='RGBA':
         negatifcouleur()
      else :
         pass
   except NameError:
      showerror('Erreur','Vous n\'avez ouvert aucune image. Ouvrez une image avant d\'appliquer un effet')

   
################################ Fonction qui affiche le résultat ######################

def affiche():
   global PHOTOTK,IMOUT
   PHOTOTK=ImageTk.PhotoImage(IMOUT) 
   c1.itemconfig(REFRESH,image=PHOTOTK)
   
################################ Fonction qui réinitialise L'affichage #################

def init():
   winsound.PlaySound('data\Audio\clic.wav',winsound.SND_FILENAME)
   try:
      global PHOTOTK
      os.remove('data\EFFET.png')
      PHOTO=Image.open('data\EFFET2.png')
      PHOTO.save('data\EFFET.png')
      PHOTO=Image.open('data\EFFET.png')
      PHOTOTK=ImageTk.PhotoImage(PHOTO) 
      c1.itemconfig(REFRESH,image=PHOTOTK)
   except NameError:
      showerror('Erreur','Vous n\'avez ouvert aucune image. Vous ne pouvez pas réinitialiser sans aucune image ouverte.')


################################ Fonction qui quitte le logiciel #################

def quit():
    winsound.PlaySound('data\Audio\clic.wav',winsound.SND_FILENAME)
    try:
       os.remove('data\ROTATIONG.png')
    except FileNotFoundError:
       pass
    try:
       os.remove('data\ROTATIOND.png')
    except FileNotFoundError:
       pass
    try:
       os.remove('data\ROTATIONP.png')
    except FileNotFoundError:
       pass
    try:
       os.remove('data\EFFET.png')
    except FileNotFoundError:
       pass
    try:
       os.remove('data\EFFET2.png')
    except FileNotFoundError:
       pass
    f1.destroy()
      
################################ Fonction importe toutes les valeurs du bouton de défilemment #################

def print_file () :
    winsound.PlaySound('data\Audio\clic.wav',winsound.SND_FILENAME)
    vall = o.get()
    if vall == "Négatif":
        neg()
    if vall == "Luminosité additive":
       lumino()
    if vall == "Flou gaussien":
       flou_gaussien()
    if vall == "Sépia":
       sepia()
    if vall == "Contraste":
       contraste()
    if vall == "Flou moyen":
       flou_moyen()
    if vall == "Accentuation":
       accentuation()
    if vall == "Différence":
       difference()
    if vall == "Rotation droite":
       rotation_droit()
    if vall == "Rotation gauche":
       rotation_gauche()
    if vall == "Rotation personnalisée":
       rotation_perso()
    if vall == "Niveaux de gris":
       niveaux_de_gris()
    if vall == "Luminosité multi":
       luminosité_multi()
    if vall == "Produit":
       produit()
    if vall == "Faible contraste":
       fcontraste()
    if vall == "Contour":
       contour()
    if vall == "Laplacien":
       laplacien()
    if vall == "Sobel":
       sobel()
    if vall == "Gradient oblique":
       gradient_oblique()
    if vall == "Random":
       random()
    if vall == "":
       showerror('Erreur','Vous n\'avez sélectionné aucun effet. Sélectionnez un effet puis réessayez.')


################## Permet de dessiner sur l'image######################

       
def clic(event):
    X,Y=event.x,event.y
    c1.create_oval(X-2,Y-2,X+2,Y+2,outline='black',fill='black')

################## Demende confirmation de quitter le logiciel######################

def callback1():
    winsound.PlaySound('data\Audio\clic.wav',winsound.SND_FILENAME)
    if askyesno('Confirmation de sortie du logiciel', 'Êtes-vous sûr de vouloir quitter Radaan ?'):
        quit()
    else:
        pass


################## Donne des informations à propos du logiciel######################

def infos():
    winsound.PlaySound('data\Audio\ding.wav',winsound.SND_FILENAME)
    showinfo("A propos de Raddan", """Logiciel crée par Rayan GRIB & Dany REVILLARD et Anthony MARLIN.

    Version : 1.0      Projet d'ISN""")
    
################## Permet d'enregistrer les modifications d'une image######################

def enregistrer():
   winsound.PlaySound('data\Audio\clic.wav',winsound.SND_FILENAME)
   try:
      scre = tkinter.filedialog.asksaveasfilename()
      IMOUT.save(scre)
      showinfo("Image sauvgardée !","L'image a bien été sauvgardée.")
   except NameError:
      showerror('Erreur','Vous n\'avez ouvert aucune image. Vous ne pouvez pas enregistrer sans aucune image ouverte.')


  
####################Interface graphique###############################################
      
DEBUT=Image.open('icons\debut.gif')
L,H=DEBUT.size[0],DEBUT.size[1]
f1=tkinter.Tk()
icon = PhotoImage(file='icons\Radaan.gif')
f1.tk.call('wm', 'iconphoto', f1._w, icon)
f1.resizable(width=False, height=False)
f1.title('R A D A A N  Éditeur d\'images')
image = Image.open("icons\Raadon.png") 
photo = tkinter.PhotoImage(file ='icons\Raadon.png')
c = tkinter.Canvas(f1, width = image.size[0], height = image.size[1])
c.create_image(0, 0, anchor = tkinter.NW, image=photo)
c.pack()
tex1 = tkinter.Label(f1, text='Pour sélectionner un effet, veuillez cliquer sur la liste Effets et choissiez celui qui est voulu.', fg='black')
tex1.pack()
cadre1 = tkinter.Frame(f1, width=768, height=576, borderwidth=1,relief='groove',bg='grey')
cadre1.pack(fill=tkinter.BOTH)
c1=tkinter.Canvas(cadre1,width=500, height=500,bg='grey',cursor="pencil")#
DEBU2T=PhotoImage(file='icons\debut.gif')
c1.create_image(L/2,H/2,image=DEBU2T)
n = -1
def update(delay=200):
    global n
    n += 1
    if n == 4: n = 0
    DEBU2T.configure(format="gif -index " + str(n))
    f1.after(delay, update)
update()
c1.bind('<B1-Motion>',clic)
c1.pack()
textdessin = tkinter.Label(f1, text='Cliquez sur l\'image pour dessiner !', fg='brown')
textdessin.pack()
cadre = tkinter.Frame(f1, width=768, height=576, borderwidth=1,relief='groove')
cadre.pack(fill=tkinter.BOTH)
cadre2 = tkinter.Frame(f1, width=768, height=576, borderwidth=1,relief='ridge')
cadre2.pack(fill=tkinter.BOTH)
b1=tkinter.Button(cadre,text='Ouvrir',command=loadf,cursor="hand2")#
im = tkinter.PhotoImage(file="icons\Ouvrir.png")
b1.config(image=im)
b1.pack(side="left")
b5=tkinter.Button(cadre,text="Enregistrer", command=enregistrer,cursor="hand2")
im5 = tkinter.PhotoImage(file="icons\Enregistrer.png")
b5.config(image=im5)
b5.pack(side="left")
b2=tkinter.Button(cadre,text='Quitter',command=callback1,cursor="hand2") #
im2 = tkinter.PhotoImage(file="icons\Quitter.png")
b2.config(image=im2)
b2.pack(side="right")
b3=tkinter.Button(cadre2,text='Réinitialiser',command=init,cursor="hand2")#
im3 = tkinter.PhotoImage(file="icons\Réinisialiser.png")
b3.config(image=im3)
b3.pack(side="right")
tex1 = tkinter.Label(cadre2, text=' Effets ', fg='black')
tex1.pack(side="left")
o=tkinter.ttk.Combobox(cadre2,text='Effets',values=["Négatif","Luminosité additive","Flou gaussien","Sépia","Contraste","Flou moyen","Accentuation","Différence","Rotation droite","Rotation gauche","Rotation personnalisée","Niveaux de gris","Luminosité multi","Produit","Faible contraste","Contour","Laplacien","Sobel","Gradient oblique","Random"])
o.pack(side="left")
b=tkinter.Button(cadre2,text="Appliquer",cursor="hand2")
im4 = tkinter.PhotoImage(file="icons\Appliquer.png")
b.config(image=im4)
b.config(command=print_file)
b.pack(side="left")
menubar = tkinter.Menu(f1)
menu1 = tkinter.Menu(menubar, tearoff=0)
menu1.add_command(label="A propos", command=infos)
menubar.add_cascade(label="Aide", menu=menu1)
f1.config(menu=menubar)
tex2 = tkinter.Label(f1, text='Éditeur d\'images pour Windows.', fg='gray')
tex2.pack()    
f1.mainloop()
