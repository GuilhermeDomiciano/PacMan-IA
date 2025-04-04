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
        """Movimento aleatório do Fantasma sem comer os pontos."""
        moves = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        random.shuffle(moves)

        for dx, dy in moves:
            new_x, new_y = self.x + dx, self.y + dy
            
            if self.env.map[new_y][new_x] in [" ", "."]:  # Só anda em espaços vazios ou comida
                self.env.map[self.y][self.x] = self.previous_tile  # Restaura o que estava antes
                self.previous_tile = self.env.map[new_y][new_x]  # Guarda o próximo tile
                
                self.x, self.y = new_x, new_y
                self.env.map[self.y][self.x] = "G"  # Atualiza nova posição
                break