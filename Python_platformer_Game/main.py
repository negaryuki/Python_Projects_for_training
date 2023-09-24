#------------------ IMPORTS -------------------
import os
import random
import pygame
import math 
from os import listdir
from os.path import isfile, join

#-----------------------------------------------

pygame.init()

pygame.display.set_caption("Platformer")

#------------------ CONSTANTS -------------------

BG_Color = (255,255,255)
WIDTH, HEIGHT = 1000 , 800
FPS = 60     #Frame per second
PLAYER_VEL = 5  #Speed of player

#------------------ SETUP WINDOW -------------------

window = pygame.display.set_mode(WIDTH, HEIGHT)

def main(window):    #to run the game
  clock = pygame.time.Clock()
  
  run= True
  while run:
    clock.tick(FPS)
    
    for event in pygme.event.get():
      if event.type = pygame.QUIT:
        run = False
        break
  pygame.quit()
  quit()    
   
  
if __name__ =="__main__":      # Only run the game if it was launched directly
  main(window)
