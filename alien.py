import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Uma classe que representa um único alienígena da frota """

    def __init__(self, ai_settings, screen):
        """Inicializa o alien e define sua posição inicial """
        super(Alien, self).__init__()
        self.screen =  screen
        self.ai_senttings =  ai_settings

        #carerga a imagem do alien e define o atributo rect
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()

        #inicia cada novo alien proximo a parte superior esquerda da tela
        self.rect.x =  self.rect.width
        self.rect.y = self.rect.height

        #armazena a posição exata do alien
        self.x =  float (self.rect.x)

    def blitme(self):
        """ Desenha o alin e sua posição atual"""
        self.screen.blit(self.image, self.rect)