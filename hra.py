import random
# TO DO:
# pouze jeden směr pro každého hráče
# střídání hráčů
# ●○

class Player:
    def __init__(self, name, stone_symbol, direction):
        self.name = name
        self.stone_symbol = stone_symbol
        self.on_turn = False
        self.from_pos = None
        self.to_pos = None
        self.direction = direction

    def get_player_moves(self):
        game.current_player.from_pos = int(input("Z jaké pozice chceš hrát? "))
        game.current_player.to_pos = int(input("Kam chceš kameny přesunout? "))


class Game:
    def __init__(self):
        self.is_game_over = False
        self.players = [player1, player2]
        self.current_player = None
        self.current_stone = None

    def greet(self):
        print("Ahoj, Vítej ve hře vrhcáby. Hra se hraje následovně... Vyber z které pozice na kterou se chceš přesunout.")

    def get_initial_player(self):
        self.current_player = random.choice(self.players)
        self.current_player.on_turn = True
        print(f"Začíná {self.current_player.name}.")

    def switch_player(self):
        for player in self.players:
            #změna hráče
            player.on_turn = not player.on_turn
            #pokud je hráč na tahu, tak ho nastavit jako aktuálního hráče
            if player.on_turn:
                self.current_player = player
                break

    def get_current_stone(self):
        if game.current_player == player1:
            self.current_stone = stone1
        elif game.current_player == player2:
            self.current_stone = stone2

    def check_valid_move(self):
        #kontrola pohybu pro hráče1
        for t in stone1.memory:
            for i in range(len(t)-1):
                if t[i] > t[i+1]:
                    print("Špatný směr pohybu")
                    return False
        
        #kontrola pohybu pro hráče2
        for t in stone2.memory:
            for i in range(len(t)-1):
                if t[i] < t[i+1]:
                    print("Špatný směr pohybu")
                    return False
                 
        return True
        


    def check_wins(self):
        ...

    def find_available_moves(self):
        ...

class Board:
    def __init__(self):
        self.board = [Tile() for _ in range(24)]

    def set_initial_board_layout(self):
        ...

    def print_board(self):
        print("  ", end="")
        for i in range(12, 0, -1):
            print(f"{i:2}", end=" ")
        print()
        print("+-" + "--+" * 12)

        for row in range(10):
            for i in range(12, -1, -1):
                if row < len(self.board[i].stones):
                    stone = self.board[i].stones[row]
                    player_stone_symbol = None
                    for player in game.players:
                        if stone.owner == player:
                            player_stone_symbol = player.stone_symbol

                    print(player_stone_symbol, end=" ") if player_stone_symbol else print("  ", end=" ")
                else:
                    # Prázdný prostor, pokud řádek neobsahuje kámen
                    print("  ", end=" ")
            print()

        for row in range(10, -1, -1):  # -1, protože chceme aby nahoře byl poslední daný kámen
            for i in range(12, 24):
                if row < len(self.board[i].stones):
                    stone = self.board[i].stones[row]
                    player_stone_symbol = None
                    for player in game.players:
                        if stone.owner == player:
                            player_stone_symbol = player.stone_symbol

                    print(player_stone_symbol, end=" ") if player_stone_symbol else print("  ", end=" ")
                else:
                    print("  ", end=" ")
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
    def __init__(self, player):
        self.memory = []
        self.owner = player
        self.from_pos = None
        self.to_pos = None
        self.symbol = player.stone_symbol


class Tile:
    def __init__(self):
        self.stones = []

    def add_stone(self, stone: Stone):
        self.stones.append(stone) 
        if game.current_player == player1:
            stone1.memory.append((game.current_player.from_pos, game.current_player.to_pos))
        elif game.current_player == player2:
            stone2.memory.append((game.current_player.from_pos, game.current_player.to_pos))

    def remove_stone(self):
        self.stones.pop()

    def print_stones(self):
        print(self.stones)
    
    def count_stones_in_tile(self, tile):
        ...


# Inicializace hry
player1 = Player("Hráč 1", "●", True) # True -> hráč začínající od zhora doleva
player2 = Player("Hráč 2", "○", False) # False -> hráč začínající zespoda doleva
game = Game()
board = Board()
dice = Dice()
stone1 = Stone(player1)
stone2 = Stone(player2)


#testing...
board.board[6].add_stone(stone1)
board.board[15].add_stone(stone2)
game.get_initial_player()
while game.check_valid_move():        
    print(game.current_player.name)
    board.print_board()
    print(dice.throw())
    game.get_current_stone()
    game.current_player.get_player_moves()
    #pokud stone který chceme položit není current_player a nebo to není pouze jeden kámen, opačného hráče, tak tah nepovolit!
    if game.current_stone != board.board[game.current_player.from_pos].stones[0]:
        print("Nemůžete operovat s kameny druhého hráče!")
        continue
    
    #pokud je kámen jiného hráče a zároveň se délka dlaždice, na kterou chceme umístit kámen 1, tak pak provedeme výhoz
    if game.current_stone != board.board[game.current_player.to_pos] and len(board.board[game.current_player.to_pos].stones) == 1: 
        board.board[game.current_player.to_pos].remove_stone()
        print(f"Hráč na pozici {game.current_player.to_pos} byl vyhozen...")
        #dodělat logiku pro vyhazování...- implementovat výhoz
        continue
    board.board[game.current_player.from_pos].remove_stone()
    board.board[game.current_player.to_pos].add_stone(game.current_stone)
    game.switch_player()
