import pygame

class Ship():

    def __init__(self, screen):
        """ Inicializa a espaçonave e define sua posição inicial"""
        self.screen =  screen

        #Carrega a imagem da espaçonave e obtém seu rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #inicializa cda nova espaçonave na parte inferior central da tela
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """ desenha a nave na posição atual """
        self.screen.blit(self.image, self.rect)