import sys

import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf 


def run_game():
    #Inicializa o  pygame, as configurações e objeto screen
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    #cria uma espaçonave
    ship = Ship(ai_settings, screen)
    #cria uma alien
    alien = Alien(ai_settings, screen)
    #cria um grupo no qual serão armazenado os projéteis
    bullets = Group()
    aliens = Group()
    
    #Cria a frota de alien
    gf.create_fleet(ai_settings,screen, aliens)
    #Inicia o laço princiapl do jogo
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship ,alien, bullets)
        
run_game()