import pygame, random, time 
pygame.init()

tama = (400, 460)
screen = pygame.display.set_mode(tama)
reloj = pygame.time.Clock()
a= 0.9

#importar imagenes
personaje= pygame.image.load('personaje.jpg')
personaje2= pygame.image.load('personaje2.jpg')
comer1=pygame.image.load('spriteC1.jpg')
comer2=pygame.image.load('spriteC2.jpg')

#ubicacion personaje
x= 130
y= 140

#para botones
red=(205,30,0)
red_on= (250,40,1)

#boton
m= 300
n= 410
boton=pygame.draw.circle(screen, red,(m,n), 20)

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
        self.energia +=10
        self.lleno += 20
        self.felicidad += 5
        if boton.collidepoint (pygame.mouse.get_pos()):
            screen.blit(comer1,(x,y+5))
            pygame.display.update()
            screen.blit(comer2,(x,y+5))
            pygame.display.update()
            reloj.tick(a)  
            screen.blit(comer1,(x,y+5))
            pygame.display.update()
            reloj.tick(a)
            pygame.display.flip()
        if boton.collidepoint (pygame.mouse.get_pos()):
            pygame.draw.circle(screen,(red_on),(m,n),20)

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

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            tamama.comer()
            tamama.limite()
            print(tamama.lleno, tamama.felicidad)
    screen.fill((255,255,255))

       

    boton=pygame.draw.circle(screen, red,(m,n), 20)
    pygame.draw.rect(screen, (0, 0, 0), [9, 9, 102, 12])
    pygame.draw.rect(screen, (0, 0, 0), [9, 29, 102, 12])
    pygame.draw.rect(screen, (0, 0, 0), [9, 49, 102, 12])
    pygame.draw.rect(screen, (0, 0, 0), [9, 69, 102, 12])
   
 
    pygame.draw.rect(screen, (0,255,0), [10, 10, tamama.salud, 10])
    pygame.draw.rect(screen, (0, 128, 128), [10, 30, tamama.energia, 10])
    pygame.draw.rect(screen, (128, 128, 128), [10, 50, tamama.lleno, 10])
    pygame.draw.rect(screen, (50,0,255), [10, 70, tamama.felicidad, 10])

    pygame.display.flip()    
   
    screen.blit(personaje,(x,y))
    pygame.display.update()
    reloj.tick(a)
    screen.blit(personaje2,(x,y))
    pygame.display.update()
    reloj.tick(a)  
