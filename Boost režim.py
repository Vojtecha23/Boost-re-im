import sys
import pygame

pygame.init()

rozliseni_okna = (1600, 600)
šířka = 1600
výška = 600
okno = pygame.display.set_mode(rozliseni_okna)
název = pygame.display.set_caption("Boost režim")
screen = pygame.display.set_mode((rozliseni_okna))

doleva = False
doprava = False
nahoru = False
dolů = False

Boostnutí = False
trvání_boostu = 200
boost_counter = 0

pozice_ctverecku_x = 10
pozice_ctverecku_y = 10
rychlost_ctverecku_x = 10
rychlost_ctverecku_y = 10

pozice_hrace = 10
velikost_hrace = 100
pozice_hrace_x = 200
pozice_hrace_y = 100
rychlost_hrace = 0.1

while True:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Klávesy
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and pozice_hrace_x > 0:
        pozice_hrace_x -= rychlost_hrace
        doleva = True
        doprava = False
        dolů = False
        nahoru = False
            
    if keys[pygame.K_RIGHT] and pozice_hrace_x < šířka - velikost_hrace:
        pozice_hrace_x += rychlost_hrace
        doleva = False
        doprava = True
        dolů = False
        nahoru = False
        
    
    if keys[pygame.K_UP] and pozice_hrace_y > 0:
        pozice_hrace_y -= rychlost_hrace
        doleva = False
        doprava = False
        dolů = False
        nahoru = True
    
    if keys[pygame.K_DOWN] and pozice_hrace_y < výška - velikost_hrace:
        pozice_hrace_y += rychlost_hrace
        doleva = False
        doprava = False
        dolů = True
        nahoru = False

    if keys[pygame.K_SPACE] and not Boostnutí and doprava:
        Boostnutí = True
        boost_counter = trvání_boostu
     
    if keys[pygame.K_SPACE] and not Boostnutí and doleva:
        Boostnutí = True
        boost_counter = trvání_boostu
    
    if keys[pygame.K_SPACE] and not Boostnutí and nahoru:
        Boostnutí = True
        boost_counter = trvání_boostu    
    
    if keys[pygame.K_SPACE] and not Boostnutí and dolů:
        Boostnutí = True
        boost_counter = trvání_boostu
        
    
    # Úprava boostu
    if Boostnutí:
        rychlost_hrace = 10
        boost_counter -= 1
        
        if boost_counter == 0:
            Boostnutí = False
            rychlost_hrace = 5

    # Obraz
    white = (255, 255, 255)
    red = (255, 0, 0)
    screen.fill(white)
    pygame.draw.rect(screen, red, (pozice_hrace_x, pozice_hrace_y, velikost_hrace, velikost_hrace))
    pygame.display.flip()

    
    if not keys[pygame.K_SPACE] and rychlost_hrace == 5:
        Boostnutí = False
        rychlost_hrace = 0.1
        
        