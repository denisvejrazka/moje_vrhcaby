import random
# TO DO:
# JSON
# rozpoznat, kdy může hráč vstupovat do domečku + domeček
# roztridit kod do metod

class Bar:
    def __init__(self):
        self.bar_stones = []

    def add_stone_to_bar(self, position):
        self.bar_stones.append(board.board[position].stones[0])
        board.board[position].remove_stone()
        print(f"Hráč na pozici {position} byl vyhozen!")

    def count_stones_for_player(self, player):
        count = sum(1 for stone in self.bar_stones if stone.owner == player)
        return count
            

class Player:
    def __init__(self, name, stone_symbol):
        self.name = name
        self.stone_symbol = stone_symbol
        self.on_turn = False
        self.from_pos = 0
        self.to_pos = 0
        self.home_tile = []

    def get_player_from(self):
        game.current_player.from_pos = int(input("Z jaké pozice chceš hrát? "))

    def get_player_to(self):
        game.current_player.to_pos = int(input("Na jakou pozici se chceš přesunout? "))

class Game:
    def __init__(self):
        self.is_game_over = False
        self.players = [player1, player2]
        self.current_player = None
        self.current_stone = None
        self.positions = []
        self.player1_home_tile_stone_count = 0
        self.player2_home_tile_stone_count = 0

    def greet(self):
        print("Ahoj, Vítej ve hře vrhcáby. Hra se hraje následovně... Vyber z které pozice na kterou se chceš přesunout.")

    def get_initial_player(self):
        self.current_player = random.choice(self.players)
        self.current_player.on_turn = True
        print(f"Začíná {self.current_player.name}.")

    def switch_player(self):
        if player1.on_turn:
            player1.on_turn = False
            player2.on_turn = True
            game.current_player = player2
        elif player2.on_turn:
            player2.on_turn = False
            player1.on_turn = True
            game.current_player = player1

    def get_current_stone(self):
        if game.current_player == player1:
            self.current_stone = stone1
        elif game.current_player == player2:
            self.current_stone = stone2

    def check_valid_move(self):
        #teoreticky nemusí být, protože se tah musí nacházet v možných pozicích (sekce pod tím)
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
           
        if player1 == game.current_player and player1.to_pos not in [player1.from_pos+dice.values[0], player1.from_pos+dice.values[1], player1.from_pos+(dice.values[0]+dice.values[1])]:
            print("Nevhodný tah")
            return False
        elif player2 == game.current_player and player2.to_pos not in [player2.from_pos-dice.values[0], player2.from_pos-dice.values[1], player2.from_pos-(dice.values[0]+dice.values[1])]:
            print("Nevhodný tah")
            return False
        
        return True
    
    def count_home_tile_stones(self):
        self.player1_home_tile_stone_count = 0
        for col in board.board[19:]:
            for stone in col.stones:
                if stone.owner == player1:
                    self.player1_home_tile_stone_count += 1
        if self.player1_home_tile_stone_count == 15:
            return True

        self.player2_home_tile_stone_count = 0
        for col in board.board[6:]:
            for stone in col:
                if stone.owner == player2:
                    self.player2_home_tile_stone_count += 1
        if self.player2_home_tile_stone_count == 15:
            True
        
    def check_wins(self):
        ...
    
    #rekurze mozna??
    def handle_player_moves(self):
        if player1.from_pos+dice.values[0] == player1.to_pos:
            game.positions.clear()
            game.positions.append(player1.from_pos+dice.values[1]) 
            return True
        
        elif player1.from_pos+dice.values[1] == player1.to_pos:
            game.positions.clear()
            game.positions.append(player1.from_pos+dice.values[0])
            return True

        elif player2.from_pos-dice.values[0] == player2.to_pos:
            game.positions.clear()
            game.positions.append(player2.from_pos-dice.values[1])
            return True

        elif player2.from_pos-dice.values[1] == player2.to_pos:
            game.positions.clear()
            game.positions.append(player2.from_pos-dice.values[0])
            return True
        
        elif (player1.from_pos+(dice.values[0]+dice.values[1]) == player1.to_pos) or player2.from_pos-(dice.values[0]+dice.values[1]) == player2.to_pos:
            return False

    def find_available_moves(self):
        if game.current_player == player1:
            self.positions.clear()
            player1_free_positions = [player1.from_pos+dice.values[0], player1.from_pos+dice.values[1], player1.from_pos+(dice.values[0]+dice.values[1])]
            for pos in player1_free_positions:
                if pos in range(24):
                    #hledání možných pozic pro hráče 1
                    if (len(board.board[pos].stones) >= 1 and board.board[pos].stones[0].owner == game.current_player) or (not board.board[pos].stones) or (len(board.board[pos].stones) == 1 and board.board[pos].stones[0].owner != game.current_player):
                        self.positions.append(pos)
                elif pos in range(25) and game.count_home_tile_stones():
                    if game.current_player == player1:
                        self.positions.clear()
                        self.positions.append(pos)
                        print(self.positions)
        elif game.current_player == player2:
            self.positions.clear()
            player2_free_positions = [player2.from_pos-dice.values[0], player2.from_pos-dice.values[1], player2.from_pos-(dice.values[0]+dice.values[1])]
            for pos in player2_free_positions:
                if pos in range(24):
                     if (len(board.board[pos].stones) >= 1 and board.board[pos].stones[0].owner == game.current_player) or (not board.board[pos].stones) or (len(board.board[pos].stones) == 1 and board.board[pos].stones[0].owner != game.current_player):
                        self.positions.append(pos)
                elif pos not in range(25) and game.count_home_tile_stones():
                    if game.current_player == player1:
                        self.positions.clear()
                        self.positions.append(pos)
                        print(self.positions)
                
    def check_if_players_stone(self):
        #nepovoli hraci hrat za kamen, ktery neni jeho
        if board.board[game.current_player.from_pos].stones[0].owner != game.current_player:
            print("Nemůžete operovat s kameny druhého hráče!")
            return False 

    def out_of_game(self):
        if len(board.board[game.current_player.to_pos].stones) == 1 and board.board[game.current_player.from_pos].stones[0].owner != board.board[game.current_player.to_pos].stones[0].owner: 
            bar.add_stone_to_bar(game.current_player.to_pos)
            board.board[game.current_player.to_pos].add_stone(game.current_stone)
            return True
        return False    

    def check_if_player_able_to_play(self):
        for stone in bar.bar_stones:
            if stone.owner == player1 and bar.stones.count(stone1) > 0:
                # !!
                if ((dice.values[0]+dice.values[1] or dice.values[0] or dice.values[1] not in board.board[6:]) and not (len(board.board[0 + (dice.values[0]+dice.values[1] or dice.values[0] or dice.values[1] in board.board[6:]) and (board.board[6:].stones[0].owner != player1)]))) and (len(board.board[6:].stones) > 0):
                    print(f"Nemůžete hrát, Váš kámen {player1.stone_symbol} je na Baru")
                    game.switch_player()
                else:
                    print("Zpátky ve hře")
                    board.board[1].add_stone(stone1)
                return False
#herní deska
class Board:
    def __init__(self):
        self.board = [Tile() for _ in range(26)]

    def set_initial_board_layout(self):
        board.board[1].add_stone(stone2)
        board.board[15].add_stone(stone1)
        board.board[15].add_stone(stone1)
        board.board[15].add_stone(stone1)
        board.board[15].add_stone(stone1)
        board.board[18].add_stone(stone2)
        board.board[18].add_stone(stone2)
        board.board[18].add_stone(stone2)
        board.board[18].add_stone(stone2)
        board.board[18].add_stone(stone2)
        board.board[18].add_stone(stone2)
        board.board[18].add_stone(stone2)
        board.board[20].add_stone(stone1)
        board.board[20].add_stone(stone1)
        board.board[20].add_stone(stone1)
        board.board[23].add_stone(stone1)
        board.board[23].add_stone(stone1)
        board.board[13].add_stone(stone1)
        board.board[16].add_stone(stone2)
        board.board[7].add_stone(stone1)
        board.board[12].add_stone(stone1)
        board.board[12].add_stone(stone1)
        board.board[6].add_stone(stone2)
        board.board[6].add_stone(stone2)
        board.board[6].add_stone(stone2)
        board.board[6].add_stone(stone2)
        board.board[6].add_stone(stone2)
        board.board[10].add_stone(stone2)
        board.board[10].add_stone(stone1)
        board.board[10].add_stone(stone1)
        board.board[3].add_stone(stone2)
        board.board[3].add_stone(stone2)
        

    def print_board(self):
        print(f"   Aktuální počet {player1.stone_symbol} na baru: {bar.count_stones_for_player(player1)}       {[]}")

        #výpis pozic
        for i in range(12, 0, -1):
            #spacing
            print(f"{i:2}", end=" ")
        print()
        print("+" + "--+" * 11)                         

        for row in range(10): #prochází kameny (řádky)
            for i in range(12, 0, -1): #prochází sloupce
                if row < len(self.board[i].stones): #kontroluje, zda v dané pozici na desce je nějaký kámen, Pokud ano, vezme se kámen a zjistí se, komu patří a přiřadí se symbol hráče (player_stone_symbol)
                    stone = self.board[i].stones[row] #definice stone
                    player_stone_symbol = None
                    #rozpoznává, který stone symbol bude vytisknut
                    for player in game.players: 
                        if stone.owner == player: 
                            player_stone_symbol = player.stone_symbol
                    print(player_stone_symbol, end="  ") if player_stone_symbol else print("  ", end=" ")
                else:
                    # Prázdný prostor, pokud řádek neobsahuje kámen
                    print("  ", end=" ")
            print()

        for row in range(10, -1, -1):  # -1, protože chceme aby nahoře byl poslední daný kámen
            for i in range(13, 25):
                if row < len(self.board[i].stones):
                    stone = self.board[i].stones[row]
                    player_stone_symbol = None
                    for player in game.players:
                        if stone.owner == player:
                            player_stone_symbol = player.stone_symbol

                    print(player_stone_symbol, end="  ") if player_stone_symbol else print("  ", end=" ")
                else:
                    # Prázdný prostor, pokud řádek neobsahuje kámen
                    print("  ", end=" ")
            print()
        
        #výpis pozic
        print("+" + "--+" * 11)
        for i in range(13, 25, 1):
            print(f"{i:2}", end=" ")
        print()

        print(f"   Aktuální počet {player2.stone_symbol} na baru: {bar.count_stones_for_player(player2)}     {[]}")

#kostka 
class Dice:
    def __init__(self):
        self.values = []

    def throw(self):
        self.values = [random.randint(1, 6), random.randint(1, 6)]
        return self.values

#kámen
class Stone:
    def __init__(self, player):
        self.memory = []
        self.owner = player
        self.from_pos = None
        self.to_pos = None
        self.symbol = player.stone_symbol

#Herní políčko
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


# Inicializace hry / vytváření instancí
bar = Bar()
player1 = Player("Hráč 1", "●") # hráč začínající od zhora doleva
player2 = Player("Hráč 2", "○") # hráč začínající zespoda doleva
game = Game()
board = Board()
dice = Dice()
stone1 = Stone(player1)
stone2 = Stone(player2)
tile = Tile()

#inicialization
board.set_initial_board_layout()

#testing
game.current_player = player1
player1.on_turn = True
while True:
    print(game.current_player.name)
    board.print_board()
    print(dice.throw())
    game.get_current_stone()
    if game.check_if_player_able_to_play() == False:
        continue
    game.current_player.get_player_from()
    game.check_if_players_stone()
    game.find_available_moves()
    game.current_player.get_player_to()
    game.check_valid_move()
    if game.out_of_game() == False:
            board.board[game.current_player.from_pos].remove_stone()
            board.board[game.current_player.to_pos].add_stone(game.current_stone)
    if game.handle_player_moves():
        game.current_player.get_player_from()
        game.current_player.get_player_to()
        game.check_valid_move()
        game.find_available_moves()
        game.handle_player_moves()
        if game.out_of_game() == False:
            board.board[game.current_player.from_pos].remove_stone()
            board.board[game.current_player.to_pos].add_stone(game.current_stone)
    else:
        board.board[game.current_player.from_pos].remove_stone()
        board.board[game.current_player.to_pos].add_stone(game.current_stone)   
    game.switch_player()