import sys
import pygame
from alien import Alien

from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets): 
    """ Responde a pressionamentos de tecla"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key== pygame.K_ESCAPE:
         sys.exit()

def get_number_aliens_x(ai_settings, alien_width):
    """" Determina o número de aliens que cabem em uma linha """
    availabre_space_x = ai_settings.screen_width - 2 * alien_width
    number_alien_x = int(availabre_space_x / (2 * alien_width))
    return number_alien_x
    
def create_alien(ai_settings, screen,aliens, alien_number, row_number):
    #cria um alien e posiciona na linha
    alien= Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x =  alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)
    
def create_fleet(ai_settings, screen, ship, aliens):
    """Cria uma frota de alien"""
    #Cira uma alien e calcula o número de alien em uma linha
    #o espaço entre os aliens é igual a largura de um alien
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    #Cria  uma frota de alien
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
             create_alien(ai_settings, screen, aliens, alien_number, row_number)   

def get_number_rows(ai_settings, ship_height, alien_height):
    """Determina o numero de linhas com aliens que cabemna ela """
    avaliable_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(avaliable_space_y / (2 * alien_height))
    return number_rows

def fire_bullet(ai_settings, screen, ship, bullets):
    """Dispara um projétil se ao limite ainda não for alcançado """
    #cria um novo projétil e adiciona ao grupo de projérteis
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship): 
    """ Responde a solturas de tecla"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right =  False
    elif event.key == pygame.K_LEFT:
        ship.moving_left =  False

def check_events(ai_settings, screen, ship, bullets):
     #Observa e responde eventos de teclado e mouse
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              sys.exit()
          elif event.type == pygame.KEYDOWN:
              check_keydown_events(event, ai_settings, screen, ship, bullets)
          elif event.type == pygame.KEYUP:
              check_keyup_events(event, ship)
     
def update_screen(ai_settings, screen, ship,aliens, bullets):
    """ Atualiza as imagens da tela e alterna para um nova tela"""
    screen.fill(ai_settings.bg_color)
    #Redesenha todos os porjéteis atrás da espaçonave e dos aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    #alien.blitme()
    aliens.draw(screen)
    
    #Deixa a tela mais recente visivel
    pygame.display.flip()
    
def update_bullets(ai_settings,screen,ship,  aliens,bullets):
    """ Atualiza a posição dos projéteis e se livra dos projéteis antigo"""
    #Atualiza as posições dos projéteis
    bullets.update()
    # Livras-se dos projéteis que desaparecem
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0:
            bullets.remove(bullet)
  

def check_bullet_alien_collision(ai_settings, screen, ship, aliens, bullets):
    """Responde a colião de alin - projétiçl """
      #Verifica se algum projétil atingiu os alien
    # case sim, le livra do aline do projétil
    collisons = pygame.sprite.groupcollide(bullets, aliens, True, True )

    if len(aliens) == 0:
        #destroi os projéteis existentes e cria uma nova frota
        bullets.empty()
        create_fleet(ai_settings, screen,ship, aliens )

def check_fleet_edges(ai_settings, aliens):
    """Responde apropriadamente se algum alienígena alcançou uma
borda."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """ Faz toda a frota descer e muda sua direção"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def update_aliens(ai_settings, ship, aliens):
    """Verifica se a frota está em uma das bordas e então atualiza as posiçoes de todos os aliens da frota"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # Verifica se houve colissões entre alien e espaçonave
    if pygame.sprite.spritecollideany(ship, aliens):
        print('Ship hit!!!')