from sys import exit
from ajustes import *
from mundo import Mundo
from jugador import Jugador
from camara import Camara
import herramientas_imagen as hi
import pygame

#Iniciar pygame
pygame.init()
pygame.display.set_caption("Juego Ninjas")

#Crear pantalla y mundo
reloj = pygame.time.Clock()
pantalla = pygame.display.set_mode(RESOLUCION)

mundo = Mundo()

mapa = mundo.mapas["mundo"]

#Icono de la ventana
icono = pygame.image.load("res/Actor/Animals/Cat/Faceset.png").convert_alpha()
pygame.display.set_icon(icono)

personaje = Jugador(mapa)

mapa.entidades.append(personaje)

camara = Camara(personaje)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
                  
     #Limpiar la pantalla
    pantalla.fill((0, 0, 0))       
    
    mundo.actualizar()
    
    camara.actualizar()
    camara.render(pantalla)
    
    surface = hi.redimensionar_imagen(pygame.Surface((personaje.caja_colision.width, personaje.caja_colision.height)), ESCALA_ZOOM)
    
    camara.render_imagen(pantalla, surface, (personaje.caja_colision.x, personaje.caja_colision.y))
    
    
    pygame.display.update()
    reloj.tick(60)
