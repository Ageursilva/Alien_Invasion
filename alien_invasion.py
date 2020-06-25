import sys

import pygame


def run_game():
    #Inicializa o jogo e cria um objeto para a tela
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Alien Invasion")

    #Inicia o laço princiapl do jogo
    while True:

        #Observa eventos de teclado e mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

         #Deixa a tela mais recente visivel
        pygame.display.flip()

run_game()