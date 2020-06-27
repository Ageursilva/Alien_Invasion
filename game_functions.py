import sys
import pygame
from alien import Alien

from bullet import Bullet

def check_keydown_events(event, ai_senttings, screen, ship, bullets): 
    """ Responde a pressionamentos de tecla"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_senttings, screen, ship, bullets)
    elif event.key== pygame.K_ESCAPE:
         sys.exit()

def create_fleet(ai_senttings, screen, aliens):
    """Cria uma frota de alien"""
    #Cira uma alien e calcula o número de alien em uma linha
    #o espaço entre os aliens é igual a largura de um alien

def fire_bullet(ai_senttings, screen, ship, bullets):
    """Dispara um projétil se ao limite ainda não for alcançado """
    #cria um novo projétil e adiciona ao grupo de projérteis
    if len(bullets) < ai_senttings.bullets_allowed:
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
              check_keydown_events(event, ai_senttings, screen, ship, bullets)
          elif event.type == pygame.KEYUP:
              check_keyup_events(event, ship)
     
def update_screen(ai_settings, screen, ship,alien, bullets):
    """ Atualiza as imagens da tela e alterna para um nova tela"""
    screen.fill(ai_settings.bg_color)
    #Redesenha todos os porjéteis atrás da espaçonave e dos aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    alien.blitme()
    alien.draw(screen)
    
    #Deixa a tela mais recente visivel
    pygame.display.flip()
    
def update_bullets(bullets):
    """ Atualiza a posição dos projéteis e se livra dos projéteis antigo"""
    #Atualiza as posições dos projéteis
    bullets.update()
    # Livras-se dos projéteis que desaparecem
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0:
            bullets.remove(bullet)