import pygame, cabo, tamama
pygame.init()
size = 800, 600
screen = pygame.display.set_mode(size)

# Comenzamos el bucle del juego
run=True



while run:
    # Capturamos los eventos que se han producido
    for event in pygame.event.get():
    	# Si el evento es salir de la ventana, terminamos
        if event.type == pygame.QUIT: 
            run = False
    #se crean dos botones, uno para cada personaje
    botonazo=pygame.draw.circle(screen, (255,0,0),(200,200), 150)    
    botonazo_cabo=pygame.draw.circle(screen, (0,0,255),(550,200), 150)    
    pygame.display.flip()
    
    #se 
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        if botonazo.collidepoint(pygame.mouse.get_pos()):
            tamama.tamama_mascota()
            run = False
        if botonazo_cabo.collidepoint(pygame.mouse.get_pos()):
            cabo.cabo_mascota()
            run = False
# Salgo de pygame
pygame.quit()
