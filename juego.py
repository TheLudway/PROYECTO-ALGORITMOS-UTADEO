import pygame, random, time, musica
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
dormir1=pygame.image.load('dormir_1.jpg')
dormir2=pygame.image.load('dormir_2.jpg')
dormir3=pygame.image.load('dormir_3.jpg')
pelota1=pygame.image.load('pelota1.jpg')
pelota2=pygame.image.load('pelota2.jpg')
pelota3=pygame.image.load('pelota3.jpg')



#ubicacion personaje
x= 130
y= 140

#para botones
red=(205,30,0)
red_on= (250,40,1)
blue=(0,0,205)
blue_on=(135, 206, 250)
gold=(255, 215, 0)
gold_on=(218, 165, 32)


#boton
m= 200
n= 410
az= 100
azo= 410
ad= 300
do= 410
class gochi:
    def __init__(self):
        with open("datos.txt", "r") as dato:
            self.salud = int(dato.readline())
            self.energia = int(dato.readline())
            self.lleno = int(dato.readline())
            self.felicidad = int(dato.readline())
            self.vivo = True

    def comer(self):
        if boton.collidepoint (pygame.mouse.get_pos()):
            pygame.draw.circle(screen,(red_on),(m,n),20)
        if boton.collidepoint (pygame.mouse.get_pos()):
            musica.comer_sound()
            screen.blit(comer1,(x,y+5))
            pygame.display.update()
            reloj.tick(a)
            screen.blit(comer2,(x,y+5))
            pygame.display.update()
            reloj.tick(a)
            screen.blit(comer1,(x,y+5))
            pygame.display.update()
            reloj.tick(a)
            screen.blit(comer1,(x,y+5))
            pygame.display.update()
            reloj.tick(a)
            screen.blit(comer2,(x,y+5))
            pygame.display.update()
            
                       
            self.salud +=10  
            self.lleno += 40
            self.felicidad += 5

    def jugar(self):
        if boton2.collidepoint (pygame.mouse.get_pos()):
            pygame.draw.circle(screen,(gold_on),(ad,do),20)
        if boton2.collidepoint (pygame.mouse.get_pos()) and self.energia > 10:
            screen.blit(pelota1,(x,y+5))
            pygame.display.update()
            reloj.tick(a)
            screen.blit(pelota2,(x,y+5))
            pygame.display.update()
            reloj.tick(a+2)
            screen.blit(pelota3,(x,y+5))
            pygame.display.update()
            reloj.tick(a+2)
            screen.blit(pelota2,(x,y+5))
            pygame.display.update()
            reloj.tick(a+2)
            pygame.display.update()
            reloj.tick(a+2)
            
            self.energia -= 10
            self.felicidad += 20
            self.lleno -=10


    def dormir(self):
        if boton1.collidepoint (pygame.mouse.get_pos()):
            pygame.draw.circle(screen,(blue_on),(az,azo),20)
        if boton1.collidepoint (pygame.mouse.get_pos()):
            for i in range(1):
                screen.blit(dormir1,(x,y+5))
                pygame.display.update()
                musica.mimir_sound()
                screen.blit(dormir2,(x,y+5))
                pygame.display.update()
                musica.mimir_sound()
                screen.blit(dormir3,(x,y+5))
                pygame.display.update()
                musica.mimir_sound()
               
                self.energia += 35
                self.lleno -= 10
       

    def limite(self):
        if self.salud > 100:
            self.salud = 100
        if self.energia > 100:
            self.energia = 100
        if self.lleno > 100:
            self.lleno = 100
        if self.felicidad >= 100:
            self.felicidad = 100

        if self.salud < 0:
            self.salud = 0
        if self.energia < 0:
            self.energia = 0
        if self.lleno < 0:
            self.lleno = 0
        if self.felicidad < 0:
            self.felicidad = 0
           
acti = True
tamama = gochi()
golpe = 0
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
            tamama.dormir()
            tamama.jugar()
            tamama.limite()
            print(tamama.salud, tamama.energia, tamama.lleno, tamama.felicidad)
    screen.fill((255,255,255))

       

    boton=pygame.draw.circle(screen, red,(m,n), 20)
    boton1=pygame.draw.circle(screen, blue,(az,azo), 20)
    boton2=pygame.draw.circle(screen, gold,(ad,do), 20)
    pygame.draw.rect(screen, (0, 0, 0), [9, 9, 102, 12])
    pygame.draw.rect(screen, (0, 0, 0), [9, 29, 102, 12])
    pygame.draw.rect(screen, (0, 0, 0), [9, 49, 102, 12])
    pygame.draw.rect(screen, (0, 0, 0), [9, 69, 102, 12])

    pygame.draw.rect(screen, (0,255,0), [10, 10, tamama.salud, 10])
    pygame.draw.rect(screen, (0, 191, 255), [10, 30, tamama.energia, 10])
    pygame.draw.rect(screen, (178, 34, 34), [10, 50, tamama.lleno, 10])
    pygame.draw.rect(screen, (255, 215, 0), [10, 70, tamama.felicidad, 10])

    pygame.display.flip()    
   
    screen.blit(personaje,(x,y))
    pygame.display.update()
    reloj.tick(a)
    screen.blit(personaje2,(x,y))
    pygame.display.update()
    reloj.tick(a)
    golpe += 1
    if golpe == 10:
        golpe = 0
        tamama.lleno -=10
        tamama.energia -=5
        tamama.felicidad -=5
    if tamama.lleno < 10:
        tamama.salud -= 5    
