import pygame as py


py.init()
screen = py.display.set_mode((400, 460))
py.display.set_caption('Tamagochi')

#cargar imagenes
personaje= py.image.load('personaje.jpg')
personaje2= py.image.load('personaje2.jpg')
comer1=py.image.load('spriteC1.jpg')
comer2=py.image.load('spriteC2.jpg')

#ubicacion personaje
x= 130
y= 140

#para botones
red=(205,30,0)
red_on= (250,40,1)


#boton
m= 300
n= 410
boton=py.draw.circle(screen, red,(m,n), 20)

#clock
reloj = py.time.Clock()
a= 0.9



estado=  True
while estado:
    for event in py.event.get():
        if event.type == py.QUIT:
            estado = False
        if event.type == py.MOUSEBUTTONDOWN and event.button ==1:
            if boton.collidepoint (py.mouse.get_pos()):

                    screen.blit(comer1,(x,y+5))
                    py.display.update()
                    reloj.tick(a+0.4)
                    screen.blit(comer2,(x,y+5))
                    py.display.update()
                    reloj.tick(a)  
                    screen.blit(comer1,(x,y+5))
                    py.display.update()
                    reloj.tick(a)
                    py.display.flip()
                   

    screen.fill((255,255,255))
    screen.blit(personaje,(x,y))
    boton=py.draw.circle(screen, red,(m,n), 20)
       
    if boton.collidepoint (py.mouse.get_pos()):
        py.draw.circle(screen,(red_on),(m,n),20)
   
   
   
    py.display.update()
    reloj.tick(a)
    screen.blit(personaje2,(x,y))
    py.display.update()
    reloj.tick(a)  
    py.display.flip()