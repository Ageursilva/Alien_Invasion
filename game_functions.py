import sys
import pygame

from bullet import Bullet

def check_keydown_events(event,ai_senttings, screen, ship, bullets): 
    """ Responde a pressionamentos de tecla"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        #cria um novo projétil e adiciona ao grupo de projérteis
        new_bullet = Bullet(ai_senttings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship): 
    """ Responde a solturas de tecla"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right =  False
    elif event.key == pygame.K_LEFT:
        ship.moving_left =  False


def check_events(ai_senttings, screen, ship, bullets):
     #Observa e responde eventos de teclado e mouse
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              sys.exit()
          elif event.type == pygame.KEYDOWN:
              check_keydown_events(event, ship)
          elif event.type == pygame.KEYUP:
              check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship):
    """ Atualiza as imagens da tela e alterna para um nova tela"""
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    
    #Deixa a tela mais recente visivel
    pygame.display.flip()
    