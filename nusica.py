"""MUSICA PARA EL JUEGO"""
import pygame

pygame.init()
def default_music():
    """La música de ambiente por 12 horas"""
    pygame.mixer.music.load('Música_Default.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.stop()


def comer_sound(): 
    """Reproduce por 9 segundos el efecto de comer de minecraft"""
    a = pygame.mixer.Sound('Comer.mp3')
    pygame.mixer.Sound.play(a)
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.pause()


def mimir_sound():
    """Reproduce por 7 segundos el sonido de dormir"""
    pygame.mixer.music.load('Mimir.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.stop()


def morir_sound():
    """Reproduce por 10 segundos plin plin plon"""
    pygame.mixer.music.load('Morir.mp3')
    pygame.mixer.music.play()
    pygame.time.wait(10000)
    pygame.mixer.music.stop()

