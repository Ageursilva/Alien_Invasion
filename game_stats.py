class GameStats():
    """ Armazena dados estatísticos da invasão alien."""
    def __init__(self, ai_settings):
        """Inicializa os dados estatisticos """
        self.ai_settings = ai_settings
        self.reset_stats()
        #Inicia  a invasão em um estado ativo
        self.game_active = True

    def reset_stats(self):
        """Inicializa os dados esta. e podem que podem mudar com o jogo"""
        self.ships_left = self.ai_settings.ship_limit

