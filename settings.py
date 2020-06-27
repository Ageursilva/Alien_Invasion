class Settings():
    """ Uma classe para armazenar todas as configurações da Invasão Alien"""

    def __init__(self):
        """Inicializa as configuraçoões do jogo."""
        #configurações da tela
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230)

        #Configuraçõoes da espaçonave
        self.ship_speed_factor = 1.5

        # Configuração dos projéteis
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 5