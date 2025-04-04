import random

class PacMan:
    def __init__(self, env):
        self.env = env
        self.x, self.y = env.get_position("P")
        
    def move(self):
        moves = [(0, -1), (-1, 0), (0,1), (1, 0)]  #Cima, Esquerda, 
        #Baixo, Direita
        random.shuffle(moves)# Mistura os movimentos
        
        for dx, dy in moves:
            new_x, new_y = self.x + dx, self.y + dy
            
            if self.env.map[new_y][new_x] != "#": # Não atravessar paredes
                self.env.map[self.y][self.x] = " " # Remove Pac-Man da posição 
                #anterior
                self.x, self.y = new_x, new_y
                self.env.map[self.y][self.x] = "P" # Atualiza nova posição
                break

class Ghost:
    def __init__(self, env):
        self.env = env
        self.x, self.y = env.get_position("G")
        self.previous_tile = " "  # Guarda o que tinha no mapa antes do fantasma
        
    def move(self):
        """Movimento aleatório do Fantasma, incluindo detectar o Pac-Man."""
        moves = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        random.shuffle(moves)

        pac_x, pac_y = self.env.get_position("P")

        for dx, dy in moves:
            new_x, new_y = self.x + dx, self.y + dy
            tile = self.env.map[new_y][new_x]

            if (new_x, new_y) == (pac_x, pac_y) or tile in [" ", "."]:
                if (new_x, new_y) == (pac_x, pac_y):
                    self.env.pacman_caught = True
                    self.env.map[pac_y][pac_x] = " "  # Remove Pac-Man do mapa

                self.env.map[self.y][self.x] = self.previous_tile
                self.previous_tile = tile
                self.x, self.y = new_x, new_y
                self.env.map[self.y][self.x] = "G"
                break



