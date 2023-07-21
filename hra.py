import random

class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color

class Board:
    def __init__(self):
        self.board = [Tile() for _ in range(24)]  # Vytvoření 24 zásobníků (sloupců) na herní desce
        self.players = [Player("Hráč 1", "●"), Player("Hráč 2", "○")]

    def print_board(self):
        print("  ", end="")
        for i in range(12, 0, -1):
            print(f"{i:2}", end=" ")
        print()
        print("+-" + "--+" * 12)

        for row in range(10): 
            for i in range(12, -1, -1):  
                if row < len(self.board[i].stones):  # Pokud řádek ještě obsahuje kámen
                    print(self.board[i].stones[row], end=" ")  # Výpis kamene
                else:
                    print("  ", end=" ")  # Prázdný prostor, pokud řádek neobsahuje kámen
            print()


        for row in range(10, 1, -1): #-1, protože chceme aby nahoře byl poslední daný kámen
            for i in range(11, 24):  
                if row < len(self.board[i].stones):  # Pokud řádek ještě obsahuje kámen
                    print(self.board[i].stones[row], end=" ")  # Výpis kamene
                else:
                    print("  ", end=" ")  # Prázdný prostor, pokud řádek neobsahuje kámen
            print()
        print("+-" + "--+" * 12) 
        print("  ", end="")
        for i in range(13, 25, 1): 
            print(f"{i:2}", end=" ")
        print()

class Dice:
    def __init__(self):
        self.values = []

    def throw(self):
        self.values = [random.randint(1, 6), random.randint(1, 6)]
        return self.values

class Stone:
    def __init__(self, color):
        self.color = color
        self.memory = []

    def move_stone(self, old_pos, new_pos):
        # Implementace pohybu kamene, pokud je tah validní
        ...

class Tile:
    def __init__(self):
        self.stones = []

    def add_stone(self, stone):
        self.stones.append(stone)

    def remove_stone(self):
        self.stones.pop()


# Inicializace herní desky a kamene
board = Board()
tile = Tile()
dice = Dice()

# Přidání kamenů
board.board[0].add_stone("●")


board.print_board()
