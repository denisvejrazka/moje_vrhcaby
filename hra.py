import random
#TO DO:
    #které kameny jsou kterého hráče

class Player:
    def __init__(self, name, stone_symbol):
        self.name = name
        self.stone_symbol = stone_symbol
        self.on_turn = False
        self.move = 0

class Game:
    def __init__(self):
        self.is_game_over = False
        self.players = [player1, player2]
        self.current_player = None

    def greet(self):
        print("Ahoj, Vítej ve hře vrhcáby. Hra se hraje následovně... Vyber z které pozice na kterou se chceš přesunout.")

    def get_initial_player(self):
        self.current_player = random.choice(self.players)
        self.current_player.on_turn = True

    def switch_player(self):
        for player in self.players:
            player.on_turn = not player.on_turn
            if player.on_turn:
                self.current_player = player
                break

    def check_valid_move(self):
        ...

    def check_wins(self):
        ...                
    

class Board:
    def __init__(self):
        self.board = [Tile() for _ in range(24)]  # Vytvoření 24 zásobníků (sloupců) na herní desce

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

        for row in range(10, -1, -1): #-1, protože chceme aby nahoře byl poslední daný kámen
            for i in range(12, 24):  
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
        self.memory = []

    def move_stone(self, old_pos, new_pos):
        #board.board[old_pos].remove_stone()
        #board.board[new_pos].add_stone()
        #self.memory.append()
        pass



class Tile:
    def __init__(self):
        self.stones = []

    def add_stone(self, stone):
        self.stones.append(stone)

    def remove_stone(self):
        self.stones.pop()


# Inicializace herní desky a kamene
player1 = Player("Hráč 1", "●")
player2 = Player("Hráč 2", "○")
game = Game()
board = Board()
tile = Tile()
dice = Dice()


#start hry
print(dice.throw())
board.print_board()

