"""MUSICA PARA EL JUEGO"""
import pygame

pygame.init()
def default_music():
    """Reproduce música de ambiente"""
    canciones = ["Música_Default_1.mp3", "Música_Default_2.mp3", "Música_Default_3.mp3"]
    for cancion in canciones:
        pygame.mixer.Sound(cancion)
        pygame.mixer.Sound.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)


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
        pygame.time.Clock().tick(5)
    pygame.mixer.music.stop()


def morir_sound():
    """Reproduce por 10 segundos plin plin plon"""
    pygame.mixer.music.load('Morir.mp3')
    pygame.mixer.music.play()
    pygame.time.wait(10000)
    pygame.mixer.music.stop()

