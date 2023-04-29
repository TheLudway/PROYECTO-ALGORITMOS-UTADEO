import pygame, random, time 
pygame.init()
tama = (500, 500)
pantalla = pygame.display.set_mode(tama)
relolo = pygame.time.Clock()
class gochi:
    def __init__(self):
        with open("datos.txt", "r") as dato:
            self.salud = int(dato.readline())
            self.energia = int(dato.readline())
            self.lleno = int(dato.readline())
            self.felicidad = int(dato.readline())
            self.vivo = True
    def comer(self):
        self.salud +=10
        self.lleno += 20
        self.felicidad += 5
    def jugar(self):
        self.energia -= 10
        self.felicidad += 20
        
    def limite(self):
        if tamama.salud > 100:
            tamama.salud = 100
        if tamama.energia > 100:
            tamama.energia = 100
        if tamama.lleno > 100:
            tamama.lleno = 100
        if tamama.felicidad >= 100:
            tamama.felicidad = 100
            
acti = True
tamama = gochi()
while acti:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            with open("datos.txt", "w+") as actu:
                actu.write(f"{tamama.salud}\n")
                actu.write(f"{tamama.energia}\n")
                actu.write(f"{tamama.lleno}\n")
                actu.write(f"{tamama.felicidad}\n")
            acti = False 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                tamama.comer()
                tamama.limite()
                print(tamama.lleno, tamama.felicidad)
    pantalla.fill((113, 138, 46))
    pygame.draw.rect(pantalla, (0, 0, 0), [9, 9, 102, 12])
    pygame.draw.rect(pantalla, (0, 0, 0), [9, 29, 102, 12])
    pygame.draw.rect(pantalla, (0, 0, 0), [9, 49, 102, 12])
    pygame.draw.rect(pantalla, (0, 0, 0), [9, 69, 102, 12])
 
    pygame.draw.rect(pantalla, (0,255,0), [10, 10, tamama.salud, 10])
    pygame.draw.rect(pantalla, (0, 128, 128), [10, 30, tamama.energia, 10])
    pygame.draw.rect(pantalla, (128, 128, 128), [10, 50, tamama.lleno, 10])
    pygame.draw.rect(pantalla, (50,0,255), [10, 70, tamama.felicidad, 10])

    pygame.display.flip()    
