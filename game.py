import os
import time
from environment import Environment
from agent import PacMan, Ghost

class Game:
    def __init__(self):
        self.env = Environment()
        self.pacman = PacMan(self.env)
        self.ghost = Ghost(self.env)
        
    def check_victory(self):
        """Verifica se ainda há pontos para coletar."""
        for row in self.env.map:
            if "." in row:
                return False
        return True
    
    def check_defeat(self):
        """Verifica se o Fantasma pegou o Pac-Man."""
        return self.env.pacman_caught 
    
    def run(self):
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            self.env.render()

            if self.check_victory():
                print("🎉 Pac-Man venceu! 🎉")
                break

            if self.check_defeat():
                break  # Sai sem imprimir mensagem aqui

            self.pacman.move()

            if self.check_defeat():
                break

            self.ghost.move()

            if self.check_defeat():
                break

            time.sleep(1)

        # Mostra o estado final do mapa e a mensagem após o jogo acabar
        os.system("cls" if os.name == "nt" else "clear")
        self.env.render()

        if self.check_victory():
            print("🎉 Pac-Man venceu! 🎉")
        elif self.check_defeat():
            print("💀 O Fantasma pegou o Pac-Man! 💀")


