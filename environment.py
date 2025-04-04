class Environment:
    def __init__(self):
        self.pacman_caught = False
        # Mapa do jogo: # = Parede, . = Comida, P = Pac-Man, G = Fantasma
        self.map = [
            ["#", "#", "#", "#", "#", "#", "#"],
            ["#", ".", ".", ".", ".", ".", "#"],
            ["#", ".", "#", "#", ".", ".", "#"],
            ["#", ".", ".", "P", ".", "G", "#"],
            ["#", ".", "#", "#", ".", ".", "#"],
            ["#", ".", ".", ".", ".", ".", "#"],
            ["#", "#", "#", "#", "#", "#", "#"]
        ]
    
    def render(self):
        """Mostra o ambiente no console."""
        for row in self.map:
            print(" ".join(row))
        print()

    def get_position(self, char):
        """Retorna a posição (x, y) de um caractere no mapa."""
        for y, row in enumerate(self.map):
            for x, cell in enumerate(row):
                if cell == char:
                    return x, y
        return None
