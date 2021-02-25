import pygame
#Inicializando o mixer
pygame.mixer.init()

#iniciando o pygame
pygame.init()

pygame.mixer.music.load('ex021 - Creedence.mp3')
pygame.mixer.music.play(loops=0, start=0.0)
input()
pygame.event.wait()