import pygame
import time

pygame.init()
pygame.mixer.music.load('Bakemonogatari - OP1 [HD] -subs.mp3')
pygame.mixer.music.play()

# Mantém o programa rodando enquanto a música estiver tocando
while pygame.mixer.music.get_busy():
    time.sleep(1)  # Espera um pouco para evitar uso excessivo da CPU