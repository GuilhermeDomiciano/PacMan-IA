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
        return self.pacman.x == self.ghost.x and self.pacman.y == self.ghost.y
    
    def run(self):
        """Loop principal do jogo."""
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            self.env.render()

            if self.check_victory():
                print("🎉 Pac-Man venceu! 🎉")
                break

            if self.check_defeat():
                print("💀 O Fantasma pegou o Pac-Man! 💀")
                break

            self.pacman.move()  # Pac-Man se move sozinho
            self.ghost.move()  # Fantasma também se move sozinho

            time.sleep(0.5)